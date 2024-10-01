import os
import re
import sys
import time
import requests
from colorama import Fore, init

# Init Colorama
init(autoreset=True)

# Regular expression for the Calendly API token
# https://stackoverflow.com/questions/49517324/why-header-and-payload-in-the-jwt-token-always-starts-with-eyj
'''
JWTs consist of base64url encoded JSON, and a JSON structure just starts with {"..., which becomes ey... when encoded with a base64 encoder. The JWT header often (not always) starts with {"alg":..., which then becomes eyJ...
'''
TOKEN_REGEX = r'eyJ[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+'

def is_valid_token(token):
    # Filtering rules for invalid tokens
    # Rule 1: No repetitive characters, i.e., more than 5 consecutive identical characters
    if re.search(r'(.)\1{4,}', token):
        return False
    
    # Rule 2: Ensure token has a mix of characters (upper, lower, digits, special chars)
    char_types = {
        'upper': any(c.isupper() for c in token),
        'lower': any(c.islower() for c in token),
        'digit': any(c.isdigit() for c in token),
        'special': any(c in '-_' for c in token)
    }
    
    if sum(char_types.values()) < 3:
        return False
    
    # Rule 3: Check segment lengths
    segments = token.split('.')
    if len(segments) != 3:
        return False  # Not a valid JWT structure as the token is a JWT here

    # Validate individual segment lengths
    header_length = len(segments[0])
    payload_length = len(segments[1])
    signature_length = len(segments[2])

    # Can be changed according to the JWT specification, but these are laxer limits
    if not (20 <= header_length <= 1000):
        return False
    if not (20 <= payload_length <= 5000):
        return False
    if not (20 <= signature_length <= 500):
        return False
    
    return True

def validate_calendly_token(api_token):
    url = "https://api.calendly.com/users/me"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 401:
        return False, "Token is invalid or expired."
    elif response.status_code == 403:
        return False, "Token is valid but does not have permission."
    elif response.status_code == 429:
        return False, "Rate limit exceeded. Please try again later."
    else:
        return False, f"Unexpected error: {response.status_code} - {response.text}"

def detect_tokens(directory):
    # ASCII art lol
    print("""
___________     __               ___________                     __                 
\\__    ___/___ |  | __ ____   ___\\__    ___/___________    ____ |  | __ ___________ 
  |    | /  _ \\|  |/ // __ \\ /    \\|    |  \\_  __ \\__  \\ _/ ___\\|  |/ // __ \\_  __ \\
  |    |(  <_> )    <\\  ___/|   |  \\    |   |  | \\/ __ \\\\  \\___|    <\\  ___/|  | \\/
  |____| \\____/|__|_ \\\\___  >___|  /____|   |__|  (____  /\\___  >__|_ \\\\___  >__|   
                    \\/    \\/     \\/                    \\/     \\/     \\/    \\/        
""")
    print("v0.3, made with ❤️ by Hritesh Sonawane")
    print("-" * 50)
    print(Fore.CYAN + "🚀 Scanning directory:", directory)
    print("=" * 50)

    if not os.path.isdir(directory):
        print(Fore.RED + f"❌ Error: The directory '{directory}' does not exist or is not accessible.")
        return

    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, 'r', errors='ignore') as file:
                    lines = file.readlines()
                    if not lines:
                        print(Fore.YELLOW + f"❗️ Warning: The file '{filepath}' is empty.")
                        continue
                    
                    for line_number, line in enumerate(lines):
                        token_match = re.search(TOKEN_REGEX, line)
                        if token_match:
                            found_token = token_match.group()
                            
                            if is_valid_token(found_token):
                                # Validate the found token with Calendly API
                                response_valid, user_info_or_message = validate_calendly_token(found_token)
                                
                                if response_valid:
                                    # Get the surrounding lines
                                    context_lines = []
                                    if line_number > 0:  # Include line -1 if it exists
                                        context_lines.append(f"{line_number}: {lines[line_number - 1].rstrip()}")
                                    context_lines.append(f"{line_number + 1}: {line.rstrip()}")  # Current line
                                    if line_number < len(lines) - 1:  # Include line +1 if it exists
                                        context_lines.append(f"{line_number + 2}: {lines[line_number + 1].rstrip()}")

                                    # Print the results
                                    print(Fore.GREEN + "🎉 Token found!")
                                    print(Fore.BLUE + f"📂 File: {filepath}")
                                    print(Fore.BLUE + f"🔍 Line: {line_number + 1}")
                                    print(Fore.MAGENTA + f"💡 Found Token: {found_token}")
                                    print(Fore.YELLOW + "📜 Context:")
                                    print("\n".join(context_lines))
                                    print("-" * 50)
                                else:
                                    print(Fore.RED + "🚫 Token found but invalid:")
                                    print(Fore.BLUE + f"📂 File: {filepath}")
                                    print(Fore.BLUE + f"🔍 Line: {line_number + 1}")
                                    print(Fore.MAGENTA + f"💡 Found Token: {found_token}")
                                    
                                    # Get the surrounding lines
                                    context_lines = []
                                    if line_number > 0:  # Include line -1 if it exists
                                        context_lines.append(f"{line_number}: {lines[line_number - 1].rstrip()}")
                                    context_lines.append(f"{line_number + 1}: {line.rstrip()}")  # Current line
                                    if line_number < len(lines) - 1:  # Include line +1 if it exists
                                        context_lines.append(f"{line_number + 2}: {lines[line_number + 1].rstrip()}")

                                    # Print the context
                                    print(Fore.YELLOW + "📜 Context:")
                                    print("\n".join(context_lines))
                                    print(Fore.RED + user_info_or_message)
                                    print("-" * 50)
                            else:
                                continue
                            
                            # Rate limiting: Sleep after each API call to avoid hitting rate limits
                            time.sleep(5)
            
            except FileNotFoundError:
                print(Fore.RED + f"❌ Error: The file '{filepath}' was not found.")
            except IsADirectoryError:
                print(Fore.RED + f"❌ Error: '{filepath}' is a directory, not a file.")
            except PermissionError:
                print(Fore.RED + f"❌ Error: Permission denied for file '{filepath}'.")
            except OSError as e:
                print(Fore.YELLOW + f"❗️ Warning: Could not read file '{filepath}' due to OS error: {e}")
            except Exception as e:
                print(Fore.YELLOW + f"❗️ Could not read file '{filepath}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "📜 Usage: python detector.py <directory>")
        sys.exit(1)

    target_directory = sys.argv[1]
    detect_tokens(target_directory)
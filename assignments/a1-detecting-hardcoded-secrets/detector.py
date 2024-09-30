import os
import re
import sys

# Regular expression for the Calendly API token
# https://stackoverflow.com/questions/49517324/why-header-and-payload-in-the-jwt-token-always-starts-with-eyj
'''
JWTs consist of base64url encoded JSON, and a JSON structure just starts with {"..., which becomes ey... when encoded with a base64 encoder. The JWT header often (not always) starts with {"alg":..., which then becomes eyJ...
'''
TOKEN_REGEX = r'eyJ[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+'


def detect_tokens(directory):
    print("🚀 Scanning directory:", directory)
    print("=" * 50)

    if not os.path.isdir(directory):
        print(f"❌ Error: The directory '{directory}' does not exist or is not accessible.")
        return

    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, 'r', errors='ignore') as file:
                    lines = file.readlines()
                    if not lines:
                        print(f"❗️ Warning: The file '{filepath}' is empty.")
                        continue
                    
                    for line_number, line in enumerate(lines):
                        if re.search(TOKEN_REGEX, line):
                            token_match = re.search(TOKEN_REGEX, line)
                            found_token = token_match.group() if token_match else None

                            # Get the surrounding lines
                            context_lines = []
                            if line_number > 0:  # Include line -1 if it exists
                                context_lines.append(f"{line_number}: {lines[line_number - 1].rstrip()}")
                            context_lines.append(f"{line_number + 1}: {line.rstrip()}")  # Current line
                            if line_number < len(lines) - 1:  # Include line +1 if it exists
                                context_lines.append(f"{line_number + 2}: {lines[line_number + 1].rstrip()}")

                            # Print the results
                            print("🎉 Token found!")
                            print(f"📂 File: {filepath}")
                            print(f"🔍 Line: {line_number + 1}")
                            print(f"💡 Found Token: {found_token}")
                            print("📜 Context:")
                            print("\n".join(context_lines))
                            print("-" * 50)
            except FileNotFoundError:
                print(f"❌ Error: The file '{filepath}' was not found.")
            except IsADirectoryError:
                print(f"❌ Error: '{filepath}' is a directory, not a file.")
            except PermissionError:
                print(f"❌ Error: Permission denied for file '{filepath}'.")
            except OSError as e:
                print(f"❗️ Warning: Could not read file '{filepath}' due to OS error: {e}")
            except Exception as e:
                print(f"❗️ Could not read file '{filepath}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("📜 Usage: python detector.py <directory>")
        sys.exit(1)

    target_directory = sys.argv[1]
    detect_tokens(target_directory)
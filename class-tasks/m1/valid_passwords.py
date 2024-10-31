import re

def is_valid_password(password):
    if (len(password) >= 10 and                    # At least 10 characters long
        re.search(r'[A-Z]', password) and          # Contains at least 1 uppercase letter
        re.search(r'[a-z]', password) and          # Contains at least 1 lowercase letter
        re.search(r'\d', password) and             # Contains at least 1 digit
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):  # Contains at least 1 special character
        return True
    return False

def find_valid_passwords(password_list):
    valid_passwords = []
    for password in password_list:
        password = password.strip()  # clean up
        if is_valid_password(password):
            valid_passwords.append(password)
    return valid_passwords

def read_passwords_from_file(file_path):
    with open(file_path, 'r') as file:
        passwords = file.readlines()
    return passwords

def write_valid_passwords_to_file(valid_passwords, output_file):
    with open(output_file, 'w') as file:
        for pwd in valid_passwords:
            file.write(pwd + '\n')

input_file = 'class-tasks/m1/all_passwords.txt'
output_file = 'class-tasks/m1/op_valid_passwords.txt'

passwords = read_passwords_from_file(input_file)
valid_passwords = find_valid_passwords(passwords)
write_valid_passwords_to_file(valid_passwords, output_file)

print(f"Valid passwords have been written to {output_file}")
# Task 2: Password Security Check
# Author: Tanvir Hasan Shanto
# This program asks a user for a password and verifies it by asking for
# three letters from specific positions.

import sys
import random

# Function to read password from a file if provided
def read_password_from_file(filename):
    try:
        with open(filename, 'r') as file:
            password = file.readline().strip()
            return password
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

# Function to get password from user input
def get_password():
    password = input("Enter your password: ").strip()
    return password

# Function to check password length
def check_length(password):
    if len(password) < 9:
        print("\nPassword too short.")
        return False
    return True

# Function to perform security check
def security_check(password):
    length = len(password)
    # Select 3 random positions in the password (1-based)
    positions = random.sample(range(1, length + 1), 3)
    
    for pos in positions:
        letter = input(f"Enter letter at position {pos}: ").strip()
        # Check if input is correct
        if len(letter) != 1:
            print("Invalid input. Enter only one character.")
            return False
        if letter == password[pos - 1]:
            print("Correct")
        else:
            print("Security check failed.")
            return False
    return True

# Main program
def main():
    print("Password Security Check")
    print("=======================\n")

    # Check if password is provided via command-line file
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        password = read_password_from_file(filename)
        if not password:
            password = get_password()
    else:
        password = get_password()

    # Check password length
    if not check_length(password):
        return

    # Perform security check
    if security_check(password):
        print("\nSecurity check passed.")

# Entry point
if __name__ == "__main__":
    main()

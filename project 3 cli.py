# TASK 3 : PASSWORD GENERATOR USING PYTHON (CLI)

import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."

    # Characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Take user input
try:
    length = int(input("Enter the desired password length: "))
    generated_password = generate_password(length)
    print("Generated Password:", generated_password)
except ValueError:
    print("Please enter a valid number.")

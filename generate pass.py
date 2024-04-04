#To Generate Random Password
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password you want to generate: "))
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)

#To Allow User to Specify Length
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# To Get desired password length from user
while True:
    try:
        password_length = int(input("Enter desired password length: "))
        if password_length <= 0:
            raise ValueError("Password length must be a positive integer")
        break
    except ValueError as e:
        print("Invalid input. Please enter a positive integer.")
        
password = generate_random_password(password_length)
print("Generated Password:", password)
 #include options for symbols words,lowercase/uppercase
import random
import string

def generate_password(length, include_symbols=False, include_numbers=False, include_uppercase=False, include_lowercase=False):
    characters = ''
    if include_symbols:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase

    if not characters:
        print("Error: No character set selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
# Example usage:
length = 12  # Set the desired length of the password
include_symbols = True  # Set to True if you want to include symbols
include_numbers = True  # Set to True if you want to include numbers
include_uppercase = True  # Set to True if you want to include uppercase letters
include_lowercase = True  # Set to True if you want to include lowercase letters

password = generate_password(length, include_symbols, include_numbers, include_uppercase, include_lowercase)
print("Generated password:", password)

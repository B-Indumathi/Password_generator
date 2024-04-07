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
        
# To generate Password Given 

import getpass

password = getpass.getpass("Enter your password: ")
print("Your password is:", password)



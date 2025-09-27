
import random
import string
import datetime

def generate_password(length=8, use_symbols=True):
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Example run
length = int(input("Enter password length: "))
symbols = input("Include symbols? (y/n): ").lower() == 'y'

new_password = generate_password(length, symbols)
print("Generated Password:", new_password)

# Optional: save generated passwords with timestamp
with open("passwords.txt", "a") as f:
    f.write(f"{datetime.datetime.now()}: {new_password}\n")

import re

while True:
    name = input("Enter your name: ")
    if name.strip() and not name.isnumeric():
        break
    else:
        print("Invalid name, please enter a non-empty string with no numbers.")

while True:
    email = input("Enter your email address: ")
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        break
    else:
        print("Invalid email address, please enter a valid email address.")

print("Name:", name)
print("Email:", email)

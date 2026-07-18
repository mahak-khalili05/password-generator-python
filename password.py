import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

characters = letters + numbers + symbols

length = int(input("How many characters do you want? "))

while length < 8:
    print("Password must be at least 8 characters.")
    length = int(input("How many characters do you want? "))

password = ""

for i in range(length):
    password += random.choice(characters)

print("Your password is:", password)

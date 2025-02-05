#Password generator

import random


print("Welcome to the PyPassword generator!\n")

# Letters list (lowercase only)
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Symbols list (specific symbols for passwords)
symbols = [
    '!', '@', '#', '$', '%', '&', '*', '-', '_', '+', '=', '?', '~'
]

# Numbers list (0-9)
numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

letter_choice = int(input("How many letters would you like in your password?\n"))

symbol_choice = int(input("How many symbols would you like?\n"))

number_choice = int(input("How many numbers would you like?\n"))

password_list = []
for char in range(0, letter_choice):
    password_list.append(random.choice(letters))

for char in range(0, symbol_choice):
    password_list.append(random.choice(symbols))

for char in range(0, number_choice):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += str(char)

print(f"Your password is: {password}")




import random as rn
import os
os.system('cls')
print("Welcome to the PyPassword Generator!")

letters = [chr(i) for i in range(97, 123)] + [chr(j) for j in range(65, 91)]
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', 
    '?', '/', '~', '`'
]
numbers = [str(i) for i in range(0,10)]

letters_num = int(input("How many Letters would you like in your password?\n"))
symbols_num = int(input("How many Symbols would you like in your password?\n"))
numbers_num = int(input("How many numbers would you like in your password?\n"))

letters_char = [letters[rn.randint(0, len(letters)-1)] for i in range(0, letters_num)]
symbols_char = [symbols[rn.randint(0, len(symbols)-1)] for i in range(0, symbols_num)]
numbers_char = [numbers[rn.randint(0, len(numbers)-1)] for i in range(0, numbers_num)]

password_char = letters_char + symbols_char + numbers_char

length = letters_num + symbols_num + numbers_num
password_char = rn.sample(password_char, length)
password = ''
for i in password_char:
    password += i
print(f"The Generated Password is: {password}")



# List Comprehension

numbers = [1, 2, 3]

new_list = [n + 1 for n in numbers]

print(new_list)

name = "Angela"

letters = [letter for letter in name]

print(letters)

numbers = [i * 2 for i in range(1, 6)]

print(numbers)

# condition list comprehension

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

names_4 = [name.upper() for name in names if len(name) >= 5]

print(names_4)


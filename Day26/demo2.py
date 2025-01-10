# Dictionary Comprehension

# new_dict = {new_key : new_value for item in list}   

# this can be used if we want to create a dictionary with the help of list

# here we use { } brackets instead of [ ]

#  we can also use this kind of approach to create a new dictionary

# new_dict = {new_key : new_value for (key, value) in dict.items() if test}

#  we can add the condition also if we want

#  This can be used if we want to create a new dictionary with the help of exisiting dictionary

import random
from tkinter import scrolledtext
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = { name : random.randint(0, 100) for name in names }

print(students_scores)


passed_students = {name : score for (name, score) in students_scores.items() if score >=50}

print(passed_students)
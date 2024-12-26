def greet():
    print(f"Begining of Greet Function")
    print("This is Greet Function")
    print("End of Greet Function")

def greet_with_name(name):
    print(f"Hello {name}")
    print("This is Greet Function")
    print("End of Greet Function")

greet_with_name("Jayasurya")

# Functions with multiple parameters
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in that {location}")

# Positional Arguments
greet_with("Tom", "London")

# KeyWord Arguments

greet_with(location = "Delhi", name = "Shiyaji Shinde")
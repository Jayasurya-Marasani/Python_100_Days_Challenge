import os
os.system("cls")


logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \\ '.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ '.___.'\\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(a,b):
    print(f"{a} + {b} = {a+b}")
    return a+b

def subtract(a,b):
    print(f"{a} - {b} = {a-b}")
    return a-b

def multiply(a,b):
    print(f"{a} * {b} = {a*b}")
    return a*b

def divide(a,b):
    print(f"{a} / {b} = {a/b}")
    return a/b

def modulus(a,b):
    print(f"{a} % {b} = {a%b}")
    return a%b

run_n = 'n'
while run_n == 'n':
    os.system("cls")
    print(logo)
    res = 0
    run = 'y'
    num1 = float(input("What's the first number?:"))

    while run == 'y':
        op = input("+\n-\n*\n/\n%\nPick an operation: ")
        num2 = float(input("What's the next number?:"))

        if op == '+':
            res = add(num1, num2)
        elif op == '-':
            res = subtract(num1, num2)
        elif op == '*':
            res = multiply(num1, num2)
        elif op == '/':
            res = divide(num1, num2)
        elif op == '%':
            res = modulus(num1, num2)

        run = input(f"Type 'y' to continue with {res}, or type 'n' to continue with new calculation: ")
        num1 = res
        if run == 'n': 
            run_n = run


    



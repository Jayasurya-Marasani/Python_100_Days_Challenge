# Subscripting
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])
print("Hello"[-1])
print("Hello"[-2])
print("Hello"[-3])
print("Hello"[-4])
print("Hello"[-5])

# String
print("123" + "345")

# int 
print(123+345)

#To print Large Numbers we can underscores instead of commas for our understanding
print(123_456_789)

# Float = Floating point number
print(2.12342)

#Boolean has True or False
print(True)
print(False)

# Type Error, Type Checking and Type Conversion
# This code give object of type has no len()
# It has size() function
# print(len(12345))
num = 12345
print(type(num))

print(type("Hello"))
print(type(False))
print(type(1.234))
print(type(1234))
print(type([1,2,3]))
print(type((1,2,3)))

# Type Conversion or Type Casting
print(type(int('123')))
print(float('1234.66') + int('1234'))
print(bool(0))
print("Number of letters in your name: "+ str(len(input("Enter your name?"))))

print(type(6/3))
print(type(6//3))
print(5/3)
print(5//3)

print(2**3)

# Follows PEMDAS
# P - Paranthesis (), 
# E - Exponents     **
# M - Multiplication *
# D - Division /
# A - Addition + 
# S - Subtraction -

# Multiplication and Division are equally importart. The calculations that are most to the left are given first preference. i.e the calcualtions goes from left to right. Inorder to visualize the code use Thonny app.

print(3 * 3 + 3 / 3 - 3)  # prints 7 because 3*3 and 3/3 are executed first so then it will be 9 + 1 - 3 then it will 10 - 7 and the output will be 7

print(3 * (3 + 3)/ 3 - 3) # prints 3

# F Strings and Number Manipulation

bmi = 84/ 1.65**2

print(bmi)
print(int(bmi))
# for rounding
print(round(bmi))
print(round(bmi, 2))

# Short hand notaion
# a = a+1 can be writen as +=

# F strings makes easy to string variables and strings easily
score = 100
name = 'Mad'
print(f"your score is {score} and name is {name}")


height = float(input("Height:"))
weight = int(input("weight:"))

if height > 2:
    raise ValueError("Human Height should not be over 2 meters")

bmi = weight / height ** 2

print(bmi)
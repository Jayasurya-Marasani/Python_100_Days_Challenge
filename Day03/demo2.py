print("Welcome to Python Pizza Delieveries!")
size = input("Do you want pizza ? S, M or L:")
pepporoni = input("Do you want pepporni pizza? Y or N:")
extra_cheese = input("Do you want extra chesse? Y or N:")

bill = 0

if size == 'S' or size == 's':
    bill = 15
    # print("The cost for small size pizza is $15")
    if pepporoni == 'Y' or pepporoni == 'y':
        # print("Extra Amount is $2")
        bill += 2

elif size == 'M' or size == 'm':
    bill = 20
    # print("The cost for Medium size Pizza is $20")
    if pepporoni == 'Y' or pepporoni == 'y':
        # print("Extra Amount is $3")
        bill += 3

elif size == 'L' or size == 'l':
    bill = 25
    # print("The cost for Large Size Pizza is $25")
    if pepporoni == 'Y' or pepporoni == 'y':
        # print("Extra Amount is $2")
        bill += 3
else:
    print("You typed wrong inputs")
if extra_cheese == 'y' or extra_cheese == 'Y':
    bill += 1

print(f"Your final is: ${bill}")


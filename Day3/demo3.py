print("Welcome to the rollercoster")
height = float(input("Enter the Height in cm?\n"))

if height >= 120:
    print('You can ride rollercoster')
else:
    print("Sorry you have to grow taller before you can ride")



total_bill = 0

if height >= 120:
    print("You can ride the rollercoster")
    age = int(input("Enter your age?"))

    if age > 18:
        print("Adult tickets are $12")
        total_bill = 12
    elif age >=12 and age<=18:
        print("Youth tickets are $7")
        total_bill = 7
    elif age < 12:
        print("Child ticket are $5")
        total_bill = 5
    elif 45 >= age >=55:
        print("Everything is going to be ok. Have a free ride on us!")
    
    want_photos = input('Do you want photos (y/n)?\n')
    if want_photos == 'Y' or want_photos == 'y':
        total_bill += 3
    
    print(f"Your final bill is ${total_bill}")
else:
    print("Sorry you have to grow taller before you can ride")


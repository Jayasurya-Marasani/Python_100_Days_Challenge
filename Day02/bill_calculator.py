print('Welcome to the tip calculator!')
total_bill = float(input('What was the total bill?\n$'))
tip = float(input('How much tip would you like to give? 10, 12, or 15?\n'))
people = float(input('How many people to split the bill?\n'))

split_amount = round((((100+tip)/100)*total_bill)/people, 2)

print('Each person should pay : $'+ str(split_amount))
import random as rn
import my_module as mm
import os

# Clearing the Screen
os.system('cls')

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

choice = [mm.rock, mm.paper, mm.scissors]
choice_names = ['rock', 'paper', 'scissors']

print(f"User choose {choice_names[user_choice]}")
print(choice[user_choice])

computer_choice = rn.randint(0, 2)

print(f"Computer Choose {choice_names[computer_choice]}")
print(choice[computer_choice])

if user_choice > 2 or user_choice <0:
    print("You Enter Wrong Value. You Lose!")
elif user_choice == computer_choice:
    print("Draw")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose!") 
elif user_choice < computer_choice:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")


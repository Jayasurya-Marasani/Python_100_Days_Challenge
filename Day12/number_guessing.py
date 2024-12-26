import random
import os
os.system("cls")
def game(num, level):
    if level == 'easy':
        lives = 10
    else:
        lives = 5
    
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make Guess : "))
        diff = num - guess
        if diff > 0:
            print("Too Low")
        elif diff < 0:
            print("Too High")
        elif diff == 0:
            print(f"You got it! The answer was {num}")
            break
        if lives == 1:
            print("You've run out of guesses. Try Again!!!")
        else:
            print("Guess Again")
        lives -= 1

logo = """
 #####                                                        #     #                                    
#     # #    # ######  ####   ####     ##### #    # ######    ##    # #    # #    # #####  ###### #####  
#       #    # #      #      #           #   #    # #         # #   # #    # ##  ## #    # #      #    # 
#  #### #    # #####   ####   ####       #   ###### #####     #  #  # #    # # ## # #####  #####  #    # 
#     # #    # #           #      #      #   #    # #         #   # # #    # #    # #    # #      #####  
#     # #    # #      #    # #    #      #   #    # #         #    ## #    # #    # #    # #      #   #  
 #####   ####  ######  ####   ####       #   #    # ######    #     #  ####  #    # #####  ###### #    # """

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

num = random.randint(1, 100)

game(num, level)

import os
import time
os.system("cls")
Menu = {
    "espresso" : {
        "ingredients" : {
            "water" : 50,
            "milk" : 0,
            "coffee" : 18,
            
        },
        "cost" : 1.5,
        },
    "latte" : {
        "ingredients" : {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost" : 2.5,
    },
    "cappuccino" : {
        "ingredients" : {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,  
        },
        "cost" : 3.0,
    },
}

resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}
money = 0

def reduce_resources(resources, option):
    for i in option["ingredients"]:
        resources[i] = resources[i] - option["ingredients"][i]
    return resources

def calculate_money():
    quarters = int(input("Enter quarters : "))
    dimes = int(input("Enter dimes : "))
    nickles = int(input("Enter nickles : "))
    pennies = int(input("Enter pennies : "))
    return (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    

def report(resources, money):
    for i in resources:
        print(f"{i} : {resources[i]}")
    print(f"Money : ${money:.2f}")

def is_available(resources, option):
    flag = -1
    if resources["water"] < option["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        flag = 1
    if resources["milk"] < option["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        flag = 1
    if resources["coffee"] < option["ingredients"]["coffee"]:
        print("“Sorry there is not enough coffee.")
        flag = 1
    
    if flag == 1:
        return False
    else:
        return True
        
def process_order(choice, Menu, resources, money):
    if is_available(resources, Menu[choice]):
        given_money = calculate_money()
        if given_money < Menu[choice]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            resources = reduce_resources(resources, Menu[choice])
            change = given_money - Menu[choice]["cost"]
            money += change
            if change > 0.0:
                print(f"Here is ${change:.2f} dollars in change.")
            print(f"Here is your {choice}. Enjoy!")
    return resources, money
            

while True:
    
    choice = input("What would you like? (espresso/latte/cappuccino):" )
    if choice == "off":
        print(f"The Coffee Machine is Shutting Down......")
        break
    elif choice == "report" :
        report(resources, money)
    elif choice in Menu:
        resources, money = process_order(choice, Menu, resources, money)
    else:
        print("Invalid Option. Try Again.....")
        time.sleep(0.5)
        os.system("cls")
            


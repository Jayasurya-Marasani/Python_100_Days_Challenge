import os
os.system("cls")
auction_dict = {}

print('''
                         ___________
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-''.---------'' '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

run = 'yes'

while run == 'yes':
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $"))
    auction_dict[name] = bid
    print()
    run = input("Are there any other bidders? Typer 'yes' or 'no'\n")
    os.system("cls")
max_key = next(iter(auction_dict))

for i in auction_dict:
    if auction_dict[i] > auction_dict[max_key]:
        max_key = i
    
print(f"The winner is {max_key} with a bid of ${auction_dict[max_key]}")

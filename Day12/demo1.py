# Local Vs Global Space

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()

print(f"enemies outside function : {enemies}")

# Local Scope and  Global Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(potion_strength)
    print(player_health)

drink_potion()

# There is no Block Scope in Python!
# So here in if condition the variable called new_enemy doesn't have block scope. we can use it even outside the if condition. But if we put the same condition in function we can't use the new_enemy variable outside of that function.
enemies = ["Skeleton", "Zombie", "Alien"]

game_level = 3
if game_level < 5:
    new_enemy = enemies[0]

def create_enemy():
    
    if game_level < 5:
        new_enemy = enemies[0]


print(new_enemy)





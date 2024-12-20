import random as rn
states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]

states.append("Jayasurya")

print(states)

states.extend(["Hello", "Marasani"])
print(states)

# Who Pay the Bill

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(f"{friends[rn.randint(0, len(friends)-1)]} pays the bill")

print(f"{rn.choice(friends)} pays the bill")


fruits = ["Strawberries", "Nectarines", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][0])
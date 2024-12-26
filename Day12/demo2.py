# Modifying the Global Scope

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function : {enemies}")


increase_enemies()

print(f"enemies oustside function : {enemies}")

# Global Constants are very useful

pi = 3.14

def area_circle(r):
    global pi
    return pi * r * r

print(f"Area of circle of radius 10 : {area_circle(10)}")

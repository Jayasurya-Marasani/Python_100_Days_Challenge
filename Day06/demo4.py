# Reeborg's World 
# Hurdle 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() == False:
    if front_is_clear():
        move()
    elif wall_in_front():
        hurdle()
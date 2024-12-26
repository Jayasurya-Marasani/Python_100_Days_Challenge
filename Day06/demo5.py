# Reeborg's World 
# Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    

while at_goal() == False:
    if front_is_clear():
        move()
    elif wall_in_front():
        hurdle()
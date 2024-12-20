# Reeborg's World 
# Hurdle 2

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

while at_goal() == False:
    hurdle()
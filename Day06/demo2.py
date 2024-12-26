# Reeborg's World 
# Hurdle 1

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
    

hurdles = 6

while hurdles > 0:
    hurdle()
    hurdles -= 1
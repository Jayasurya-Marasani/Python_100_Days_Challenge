import pandas as pd
import turtle

df = pd.read_csv("50_states.csv")
states = df["state"].str.lower().to_list()
guessed_states = []

screen = turtle.Screen()
screen.title("US States Game")
img_path = "blank_states_img.gif"
screen.addshape(img_path)
turtle.shape(img_path)

guessed_correct = 0
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{guessed_correct}/50 State's Correct", prompt= "What's another state's name?").lower()
    
    if answer_state in states:
        t = turtle.Turtle()    
        t.hideturtle()
        t.penup()
        state_data = df[df['state'].str.lower() == answer_state]
        t.goto(state_data['x'].item(), state_data['y'].item())
        t.write(state_data["state"].item())
        guessed_correct += 1
        guessed_states.append(answer_state)
    elif answer_state == "exit":
        # missing_states = []
        # for state in states:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        missing_states = [state for state in states if state not in guessed_states]
        new_data_dict = {
            "Missing States" : missing_states
        }
        new_data = pd.DataFrame(new_data_dict)
        new_data = new_data.rename_axis("States")
        new_data.to_csv("states_to_learn.csv", index = True)

        break

# States_to_learn.csv



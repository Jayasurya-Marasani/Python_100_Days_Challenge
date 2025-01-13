from tkinter import *
import pandas as pd
import random
import os
from tkinter import messagebox
BACKGROUND_COLOR = "#B1DDC6"
words_dict = {} 
current_card = {}
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orignal_df = pd.read_csv("data/french_words.csv")
    words_dict = orignal_df.to_dict(orient="records")

else:
    words_dict = df.to_dict(orient="records")




def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(card_word, text = current_card['French'], fill = "black")
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(canvas_image, image = card_front_img)
    flip_timer = window.after(3000, func = flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(canvas_image, image = card_back_img)

def is_known():
    try:
        words_dict.remove(current_card)
    except:
        messagebox.showerror(title = "Error", message="You Have Learnt Every word")
        os.remove("data/words_to_learn.csv")
    else:
        data = pd.DataFrame(words_dict)
        data.to_csv("data/words_to_learn.csv", index = False)
        next_card()

window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, func = flip_card)
    

    
canvas = Canvas(width = 800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file = "images/card_front.png")
card_back_img = PhotoImage(file = "images/card_back.png")

canvas_image = canvas.create_image(400, 263, image = card_front_img)
canvas.grid(row = 0, column = 0, columnspan=2)

card_title = canvas.create_text(400, 150, text = "Title", font = ("Inter", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "Word", font = ("Inter", 60, "bold"))


cross_image = PhotoImage(file = "images/wrong.png")
unknown_button = Button(image = cross_image, highlightthickness=0, command = next_card)
unknown_button.grid(row = 1, column= 0)

check_image = PhotoImage(file = "images/right.png")
known_button = Button(image = check_image, highlightthickness=0, command=is_known)
known_button.grid(row = 1, column=1)

next_card()

window.mainloop()


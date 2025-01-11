from operator import is_
from re import L
from tkinter import *

FONT = ("Helvetica", 12, "normal")

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=600, height=600)
window.config(padx= 20, pady = 20)

# Entry

entry = Entry(width=10)
entry.focus()
entry.grid(row = 0, column = 1)

# miles label

miles_label = Label(text = "Miles", font = FONT)
miles_label.grid(row = 0, column=2)

# is equal to label

is_equal_to = Label(text = "is equal to", font = FONT)
is_equal_to.grid(row = 1, column=0)

# converted Label
km_label = Label(text = "0", font = FONT)
km_label.grid(row = 1, column=1)

# km text label

km = Label(text = "Km", font= FONT)
km.grid(row = 1, column= 2)

# button

def convert_to_km():
    mile = float(entry.get())
    km_label["text"] = int(mile * 1.609)

calculate = Button(text = "Calculate", command=convert_to_km)
calculate.grid(row = 2, column= 1)

window.mainloop()
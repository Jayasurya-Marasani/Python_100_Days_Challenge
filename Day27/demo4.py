from statistics import variance
from tkinter import *

from numpy import var

window = Tk()
window.minsize(width=600, height=600)
window.title("Widget Examples")

def button_clicked():
    my_label["text"] = entry.get()

my_label = Label(text = "I am a Label", font= ("JetBrainsMono Nerd Font", 24, "italic bold"))
my_label.pack()

button = Button(text = "Click Me", font = ("JetBrainsMono Nerd Font", 24, "bold"), command= button_clicked)
button.pack()

entry = Entry(width = 40)
entry.insert(END, string = "Enter the text")
print(entry.get())
entry.pack()

# Text Entry box
text = Text(height= 10, width=30)
text.focus()
text.insert(END, "Example of mulit-line text entry with a second line\nHello")
print(text.get("2.0", END))
text.pack()


# Spin box
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_ = 0, to = 10, width=5, command = spinbox_used)
spinbox.pack()


# Scale

def scale_used(value):
    print(value)

scale = Scale(from_ = 0, to = 100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text = "Is on?", variable=checked_state, command= checkbutton_used)
checked_state.get()
checkbutton.pack()
# Radiobutton


def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text = "Option 1", value = 1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text = "Option 2", value = 2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox

def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()














window.mainloop()
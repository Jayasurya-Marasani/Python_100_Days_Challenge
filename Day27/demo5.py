import tkinter

window = tkinter.Tk()

window.title("My First Gui Program")

window.minsize(width = 600, height = 600)

window.config(padx=200, pady=100)


# Label

my_label = tkinter.Label(text = "I am a Label", font = ("JetBrainsMono Nerd Font", 24, "italic bold"))
my_label.config(text = "New Label")
# my_label.pack(side = "left")
# my_label.place(x = 100, y = 200)
my_label.grid(column= 0, row = 0)
my_label.config(padx = 50, pady=50)
# Button
def button_clicked():
    new_text = entry.get()
    my_label["text"] = new_text


button = tkinter.Button(text = "Click Me", font = ("JetBrainsMono Nerd Font", 20, "bold"), command= button_clicked)
# button.pack(side = "left")
button.grid(row = 1, column = 1)


# Entry 
entry = tkinter.Entry(width= 40)
# entry.pack(side = "left")
entry.grid(column=3, row = 2)

# New Button
new_button = tkinter.Button(text = "Button 2", font = ("Aerial", 24, "bold"))
new_button.grid(column=2, row = 0)


window.mainloop()


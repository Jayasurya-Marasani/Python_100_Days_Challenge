import tkinter

window = tkinter.Tk()

window.title("My First Gui Program")

window.minsize(width = 600, height = 600)

# Entry class

input = tkinter.Entry(width= 40)

# Label

my_label = tkinter.Label(text = "I am a Label", font = ("JetBrainsMono Nerd Font", 24, "italic bold"))
# my_label["text"] = "new text"
# my_label.config(text = "config text")
my_label.pack()

# Button
def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text


button = tkinter.Button(text = "Click Me", font = ("JetBrainsMono Nerd Font", 20, "bold"), command= button_clicked)
button.pack()


# Entry 

input.pack()
print(input.get())


window.mainloop()


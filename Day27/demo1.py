import tkinter

window = tkinter.Tk()

window.title("My First Gui Program")

window.minsize(width=600, height=600)


def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

# Label

my_label = tkinter.Label(text = f"Sum = {add(1,2, 3, 4, 5, 6, 7, 8, 9, 10)}", font = ("JetBrainsMono Nerd Font", 24, "bold"))


# my_label = tkinter.Label(text = f" Sum = {add(1,2,3)}", font = ("JetBrainsMono Nerd Font", 24, "bold"))


# my_label = tkinter.Label(text = "I am a Label", font = ("Arial", 24, "bold"))

my_label.pack(expand = True)





window.mainloop()



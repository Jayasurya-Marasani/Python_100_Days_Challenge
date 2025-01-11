from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    reset_time = 0
    reps = 0
    canvas.itemconfig(timer_text, text = f"{reset_time:02}:{reset_time:02}")
    timer_label.config(text = "Timer", fg=GREEN)
    tick_label.config(text = "")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps%8==0:
        timer_label.config(text = "Break", fg = RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text = "Break", fg = PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text = "Work", fg = GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = count//60
    count_sec = count % 60
    canvas.itemconfig(timer_text, text = f"{count_min:02}:{count_sec:02}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = reps//2
        for _ in range(work_sessions):
            mark += "✔"
        tick_label.config(text = mark)      

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg = YELLOW, highlightthickness=0)


canvas = Canvas(width=200, height=224, bg = YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image = tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill = "white", font = (FONT_NAME, 35, "bold") )
canvas.grid(row = 1, column= 1)

timer_label = Label(text = "Timer", font = (FONT_NAME, "50", "normal"), fg = GREEN, bg = YELLOW)
timer_label.grid(column = 1, row = 0)

tick_label = Label(fg=GREEN, bg= YELLOW, font=(FONT_NAME, 20))
tick_label.grid(row = 3, column= 1)


# Buttons

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row = 2, column=0)

reset_button = Button(text = "Reset", highlightthickness=0,command=reset_timer)
reset_button.grid(row = 2, column= 2)

window.mainloop()
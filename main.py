from tkinter import *
from tkinter import ttk
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
timer = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK!", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"  # Dynamic Typing

    timer_string = f"{count_min}:{count_seconds}"
    canvas.itemconfig(timer_text, text=timer_string)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

# Canvas
canvas = Canvas(window, width=200, height=224, bg="red", highlightthickness=1)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# Timer_Label
timer_label = Label(window, text="TIMER", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

# start_button
start_button = ttk.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

# check_label
check_label = Label(text="", bg=YELLOW, fg=GREEN)
check_label.grid(row=2, column=1)

# reset_button
reset_button = ttk.Button(text="Reset", command=reset)
reset_button.grid(row=2, column=2)

window.mainloop()

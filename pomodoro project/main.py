import tkinter
import math
from tkinter import PhotoImage

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
HEAVY_GREEN = "#5fde7f"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    start_button.config(state="normal")
    canvas.itemconfig(timer_text, text = "00:00")
    happening.config(text = "")
    check.config(text = "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    start_button.config(state="disabled")
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1


    if reps % 8  == 0:
        countdown(long_break_sec)
        happening.config(text = "Long Break", fg = RED)
    elif reps % 2 != 0:
        countdown(work_sec)
        happening.config(text="Work", fg = GREEN)
    else:
        countdown(short_break_sec)
        happening.config(text="Short Break", fg = RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✅"
        check.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

text = tkinter.Label(text = "Timer", font = (FONT_NAME, 45), fg=HEAVY_GREEN, bg=YELLOW)
text.grid(column=1, row=0)

happening = tkinter.Label(text = "", font = (FONT_NAME, 40), fg = GREEN, bg = YELLOW)
happening.grid(column=1, row=1)

start_button = tkinter.Button(text="Start", highlightthickness=0, command = start_timer)
start_button.grid(column=0, row=3)

button1 = tkinter.Button(text="Reset", highlightthickness=0, command = reset_timer)
button1.grid(column=2, row=3)

check = tkinter.Label(bg = YELLOW, fg=GREEN)
check.grid(column=1, row=4)


window.mainloop()

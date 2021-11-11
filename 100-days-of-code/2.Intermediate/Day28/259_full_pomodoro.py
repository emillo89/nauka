from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 25
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    """reset title, timer and checkmarks"""
    window.after_cancel(timer)
    name.config(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text=None)
    global reps
    reps = 0

#start_timer to be responsible for calling function
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps in (1, 4, 6):
        count_down(work_sec)
        name.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        name.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        name.config(text="Break", fg=PINK)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += check
        checkmark.config(text=mark)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Create canvas with tomato image
img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(101, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#Create Label: timer, check mark
name = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
name.grid(column=1, row=0)

check = "✔"
checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

#Create button: start and reset
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()

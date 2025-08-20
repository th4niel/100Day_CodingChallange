from tkinter import *
import math

YELLOW = "#f7f5dd"
RED = "#e7305b"
GREEN = "#9bdeac"
PINK = "#e2979c"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Studying", fg=GREEN)


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)


window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

#label description
title_label = Label(text="Timer", fg=GREEN, font=("Courier", 50), bg=YELLOW)
title_label.grid(column=1, row=0)

#CANVA IMAGE
canvas = Canvas(width= 200, height= 224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./pomodoro/tomato.png")
canvas.create_image(100, 112, image =tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00",fill="White", font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)

#Button
start_label = Button(text="Start", command=start_timer)
start_label.grid(column=0, row=2)

reset_label = Button(text="Reset", command=reset_timer)
reset_label.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=("Courier",30))
check_mark.grid(column=1, row=3)

window.mainloop()

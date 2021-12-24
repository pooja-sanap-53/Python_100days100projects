# Day 26
# Date: 24 Dec 2021
# POMODORO

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER", fg=GREEN, font=(FONT_NAME, 28, "bold"), bg=YELLOW)
    checkbox.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep
    rep +=1 
    work_sec = WORK_MIN*60
    short_break_sec = 60*SHORT_BREAK_MIN
    long_break_sec = 60*LONG_BREAK_MIN

    if rep%8==0:
        countdown(long_break_sec)
        timer_label.config(text="LONG BREAK", fg=RED, font=(FONT_NAME, 28, "bold"), bg=YELLOW)

    elif rep %2==0:
        countdown(short_break_sec)
        timer_label.config(text="SHORT BREAK", fg=PINK, font=(FONT_NAME, 28, "bold"), bg=YELLOW)

    else:
        countdown(work_sec)
        timer_label.config(text="WORK", fg=GREEN, font=(FONT_NAME, 28, "bold"), bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(rep/2)
        for _ in range(work_sessions):
            mark +="✓"
        checkbox.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=30, bg=YELLOW)


canvas = Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Day_26/tomato.png")
canvas.create_image(103, 115, image=tomato_img)
timer_text = canvas.create_text(
    103, 133, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 28, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

end_btn = Button(text="Reset", highlightthickness=0, command = reset_timer)
end_btn.grid(column=2, row=2)

checkbox = Label(fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
checkbox.grid(column=1, row=3)


window.mainloop()

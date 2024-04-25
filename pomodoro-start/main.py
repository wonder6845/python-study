# TODO
# REP1: 25 MIN WORK
# 5 MIN Break
# REP2: 25 MIN WORK
# 5 MIN Break
# REP3: 25 MIN WORK
# 5 MIN Break
# REP4: 25 MIN WORK
# 20 MIN Break
# ✔

import winsound as sd
import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e12433"
GREEN = "#48767b"
YELLOW = "#ffe693"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20 
REPS = 0
second = 60
timer = None 

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    REPS = 0
    
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    title_label.configure(text="Title")
    check_label.config(text=check_mark, foreground=GREEN)
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    
    work_sec = WORK_MIN * second
    short_break_sec = SHORT_BREAK_MIN * second
    long_break_sec = LONG_BREAK_MIN * second
    
    REPS += 1
    # If it's 1st/3rd/5th/7th reps:
    if REPS % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", font=(FONT_NAME, 28, "bold"), foreground=PINK, background=YELLOW, highlightthickness=0)
        
    # if it's 8th reps:
    elif REPS % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", font=(FONT_NAME, 28, "bold"), foreground=RED, background=YELLOW, highlightthickness=0)
        
        
    # if it's 2nd/4th/6th reps:
    else:
        count_down(work_sec)
        title_label.config(text="Work", font=(FONT_NAME, 28, "bold"), foreground=GREEN, background=YELLOW, highlightthickness=0)
        
def beepsound():
    fr = 2000
    du = 1000
    sd.Beep(fr, du)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / second)
    count_sec = count % second
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks +=  check_mark
            check_label.config(text=check_mark, foreground=GREEN)
    

# ---------------------------- UI SETUP ------------------------------- # 

check_mark = "✔" 
fg = GREEN


window = tkinter.Tk()
window.title("Promodoro")
window.config(padx=100, pady=50,bg=YELLOW)


# Create Title
title_label = tkinter.Label(text="Timer", font=(FONT_NAME, 28, "bold"), foreground=fg, background=YELLOW, highlightthickness=0)
title_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=210, height=224, background=YELLOW, highlightthickness=0)

# Create Image
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(105, 110, image=tomato_img)

timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"),tags=str)
canvas.grid(column=1, row=1)


# Button
start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)

check_label = tkinter.Label(background=YELLOW, highlightthickness=0)
check_label.grid(column=1, row=4)

window.mainloop()
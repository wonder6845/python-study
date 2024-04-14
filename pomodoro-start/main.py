# TODO
# REP1: 25 MIN WORK
# 5 MIN Break
# REP2: 25 MIN WORK
# 5 MIN Break
# REP3: 25 MIN WORK
# 5 MIN Break
# REP4: 25 MIN WORK
# 20 MIN Break
 
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
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    count = 5
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(10)
    
def beepsound():
    fr = 2000
    du = 1000
    sd.Beep(fr, du)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_min < 10:
        count_min = f"0{count_min}"
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    if count == 0:
        beepsound() 
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
        
    

# ---------------------------- UI SETUP ------------------------------- # 

check_mark = "✅"
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

check_label = tkinter.Label(text=check_mark, font=(FONT_NAME, 13, "bold"), foreground=fg, background=YELLOW, highlightthickness=0)
check_label.grid(column=1, row=4)

window.mainloop()
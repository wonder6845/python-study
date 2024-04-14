import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#48767b"
YELLOW = "#ffe697"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    title_label.itemconfig(timer_text, text=count)
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
canvas.grid(column=1, row=2)



# Button
start_button = tkinter.Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=3)

reset_button = tkinter.Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=3)

check_label = tkinter.Label(text=check_mark, font=(FONT_NAME, 13, "bold"), foreground=fg, background=YELLOW, highlightthickness=0)
check_label.grid(column=1, row=4)

window.mainloop()
from tkinter import *

window = Tk()
#######이 사이에 코드 #####
window.title("🌏 My First GUI Program")
window.minsize(width=500, height=300)
window.config(background="Yellow")

# Label = 프린트
my_label = Label(text="I'm Lable", font=("Arial", 24, "bold"), background="Yellow")
# my_label.pack() # (중앙 위치)
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="Enter your name")

# Entry
input = Entry(width=10)
input.pack()

# Button

def button_cliked() -> None:
    my_label.config(text="Button were clicked")
    name = input.get()
    my_label.config(text=name)
    print("I got clicked")

button = Button(text="Enter", command=button_cliked)
button.pack()



#######이 사이에 코드 #####
# 계속 유지 시켜 주는 것
window.mainloop()



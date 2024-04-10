from tkinter import *

window = Tk()
#######이 사이에 코드 #####
window.title("My First GUI Program")
window.minsize(width=500, height=300)

sum = 0

# Label = 프린트
my_label = Label(text="I'm Lable", font=("Arial", 24, "bold"))
# my_label.pack() # (중앙 위치)
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="How many Times Did I clicked?")

# 숫자세기

count_label = Label(text=str(sum), font=("Arial", 10))
count_label.pack()

# Button

def button_cliked():
    global sum
    sum += 1
    print(f"I got clicked {sum}")
    count_label.config(text=str(sum))
    return sum
    
    
button = Button(text="Click me", command=button_cliked)
button.pack()


#######이 사이에 코드 #####
# 계속 유지 시켜 주는 것
window.mainloop()



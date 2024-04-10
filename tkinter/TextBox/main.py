from tkinter import *
class Window(Tk):
    def __init__(self) -> None:
        super().__init__()

        # Window 설정
        self.title("My First GUI Program")
        self.minsize(width=500, height=300)
        self.config(padx=300, pady=150)

        # 레이블 생성
        self.label = Label(text="This is a Label", font=("Arial", 15, "bold"))
        self.label.grid(column=0, row=0)
        
        # 버튼 생성
        self.button = Button(text="This is a button", command=self.button_clicked)
        self.button.grid(column=2, row=2)
        
        # Entry 생성
        self.input = Entry(width=10)
        self.input.grid(column=4, row=4)
    
    
    # 버튼 클릭시 실행되는 메소드
    def button_clicked(self):
        print("I got clicked")
        new_text = self.input.get()
        self.label.config(text=new_text)
        print(new_text)
    
    # Add New Button
    def add_new_button(self, text, column, row):
        new_button = Button(self, text=text, command=self.button_clicked)
        new_button.grid(column=column, row=row)
    
    
if __name__ == "__main__":
    window = Window()
    
    window.add_new_button("New Button", column=3, row=0)
    
    window.mainloop()


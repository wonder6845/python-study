POSITION = "center"
FONT = ("Arial", 18, "normal")
from turtle import Turtle

class Score_Board(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = data.read()

        
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update()

    def score_increase(self):    
        self.score += 1
        self.clear()
        self.update()


    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=POSITION, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()

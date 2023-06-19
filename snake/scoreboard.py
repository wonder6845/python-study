POSITION = "center"
FONT = ("Arial", 18, "normal")
from turtle import Turtle

class Score_Board(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
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
        self.write(f"Score: {self.score}", move=False, align=POSITION, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align=POSITION, font=FONT)

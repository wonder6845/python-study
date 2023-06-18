'''
STEP1: 몸통만들기
STEP2: 뱀 움직이기
STEP3: 뱀 먹이 만들기
STEP4: 뱀 먹이 합쳐지기
STEP5: 점수보드 만들기
STEP6: 벽에 부딪히면 끝
STEP7: 꼬리 부딛히면 끝

Class: snake food score board
'''

from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Detect Collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()


screen.exitonclick()
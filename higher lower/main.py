from data import data
from art import logo, vs
import random
import os

def clear():
    os.system('cls')

def choice(data):
    random_choice = random.choice(data)
    return random_choice

def return_data(value):
    name = value["name"]
    description = value["description"]
    country = value["country"]
    return f"{name}, {description}, {country}."

def judge(a, b):
    # 판단이 맞을 경우
    if a['follwer_count'] > b['follwer_count']:
        return a
    # 정답이 아닌 경우
    else:
        return b

def intro_game(a, b):
    print(f"Compare A: {return_data(a)}")
    print(vs)
    print(f"Against B: {return_data(b)}")
    select = input("Who has more follwers? Type 'A' or 'B': ").lower()
    return select

def game():
    obj_a = choice(data)
    obj_b = choice(data)
    score = 0
    end_of_game = False
    print(logo)
    select = intro_game(obj_a, obj_b)
    while not end_of_game:
        answer = judge(obj_a ,obj_b)
        if select == answer:
            clear()
            score += 1
            answer = obj_a
            obj_b = choice(data)
            print(logo)
            print(f"You're right! Current score: {score}.")
            select = intro_game(obj_a, obj_b)            
        else:
            end_of_game = True
            print(f"Sorry, that's wrong. Final score: {score}")
game()
import logo
import random
print(logo.logo)

def create_answer():
    answer = random.randint(1,100)
    return answer

def difficulty():
    select = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if select == 'easy':
        life = 10
    elif select == 'hard':
        life = 5
    return life

ANSWER = create_answer()

def nevigate_number(answer, life):
    end_of_game = False
    while not end_of_game:
        print(f"You have {life} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"You got it! The answer was {answer}")
            end_of_game = True
        else:
            if guess > answer:
                print("Too high.")
            else:
                print("Too low.")
            life -= 1
        if life > 0:
            print("Guess again.")
        else:
            print("You've run out of guesses, you lose.")
            end_of_game = True    


def guess_the_number():
    print("Welcom to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Psst, the correct answer is {ANSWER}")
    life = difficulty()
    nevigate_number(ANSWER, life)

guess_the_number()


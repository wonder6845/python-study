# Calculator
from art import logo
# Add
def add(n1, n2):
    return n1 + n2

# Substract
def substract(n1, n2):
    return n1 - n2

# Multiply
def mult(n1, n2):
    return n1 * n2

# Divide
def div(n1, n2):
    return n1 / n2


# 함수 호출을 위한 dictionary
operation = {
    "+": add,
    "-": substract,
    "*": mult,
    "/": div,
}


# 재귀함수
def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operation:
        print(symbol)
    operation_symbol = input("Pick an operation from the live above: ")

    num2 = float(input("What's the second number?: "))

    # 함수 호출을 위해 변수를 받음
    calculation_function = operation[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    stop = False

    while not stop:
        selection = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ").lower()
        if selection == 'n':
            stop == True
            calculator()
        else:
            for symbol in operation:
                print(symbol)    
        operation_symbol = input("Pick an operation from the live above: ")
        next_number = float(input("What's the next number?: "))
        calculation_function = operation[operation_symbol]
        after_answer = calculation_function(answer, next_number)
        print(f"{answer} {operation_symbol} {next_number} = {after_answer} ")
        after_answer = answer

calculator()
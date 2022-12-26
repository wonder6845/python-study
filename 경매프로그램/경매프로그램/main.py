from art import logo
import os
#HINT: You can call clear() to clear the output in the console.

def clear():
  os.system('cls')

print(logo)

print("Welcom to secret aution program.")

loop = True
auction = {}

winning_bid = 0
bidder = "nobody"

while loop == True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    select = input("Are there any other bidders? Type 'yes' or 'no': ")
    auction[name] = bid
    if bid > winning_bid:
        winning_bid = bid
        bidder = name

    if select == "yes":
        clear()
    else:
        loop = False
        print(auction)
        print(f"The winner is {bidder} with a bid of ${winning_bid}")



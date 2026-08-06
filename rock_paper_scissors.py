import random

choices = ["rock", "paper", "scissors"]
us = 0
cs = 0
round = 1

print("=== Welcome to ROCK, PAPER, SCISSORS Game ===")

while True:
    try:
        tr = int(input("How much round you like to play? "))
        if tr > 0:
            break
        else:
            print("please enter a number greater than 0")
    except ValueError:
        print("invalid input! please enter a valid input")
print(f"\n this is a {tr}- round game. type 'quit' anytime if you get tired ")

while round <= tr:
    print(f"\n --- Round{round} ---")
    ui = input("Enter rock, paper, scissors:").lower()

    if ui == "quit":
        print("you decided to leave early")
        break

    if ui not in choices:
        print("Invalid input! please type rock/paper/scissors")

    comp = random.choice(choices)
    print("computer choice:",comp)

    if ui == comp:
        print("it's a tie")
    elif ui == "rock":
        if comp == "scissors":
            print("player win")
            us += 1
        else:
            print("computer win")
            cs += 1
    elif ui == "paper":
        if comp == "rock":
            print("player win")
            us += 1    
        else:
            print("computer win")
            cs += 1
    elif ui == "scissors":
        if comp == "paper":
            print("player win")
            us += 1
        else:
            print("computer win")
            cs += 1

    print(f"Score -> You: {us} | Computer: {cs}")
    round +=1

print("\n---- FINAL RESULTS ----")
print(f"Player Total: {us}")
print(f"Computer Total: {cs}")

if us > cs:
    print("Congratulations, You won the game!")
elif cs > us:
    print("The computer wins the game.Better luck next time!")
else:
    print("It,s a tie buddy!")
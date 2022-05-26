import random
print("Let's play Rock, Paper, Scissors")
print("If you wanna play this game with me, enter yes, otherwise no")
userOpinion = input().lower()
while userOpinion == "yes":
    print("Enter a value to start the game")
    userInput = input().upper()
    items = ["ROCK", "PAPER", "SCISSORS"]
    randomInput = random.choice(items)
    print(randomInput)
    if userInput == randomInput:
        print("Ah it's a tie! Try again!")
    elif userInput == "ROCK" and randomInput == "PAPER":
        print("You lose! :(")
    elif userInput == "ROCK" and randomInput == "SCISSORS":
        print("You win!")
    elif userInput == "PAPER" and randomInput == "ROCK":
        print("You lose! :(")
    elif userInput == "PAPER" and randomInput == "SCISSORS":
        print("You lose! :(")
    elif userInput == "SCISSORS" and randomInput == "ROCK":
        print("You lose! :(")
    elif userInput == "SCISSORS" and randomInput == "PAPER":
        print("You win!")
    else:
        print("please enter a valid value")
    print("Do you wanna continue this game? (enter yes or no)")
    userOpinion = input().lower()
print("Well, thank you for playing with me! See you")
#import random module
import random

#the list of options
options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

#assign a random play to the computer
computer = random.choice(options)

#set player to False
player = False

while player == False: #set player to True
    player = input("Rock, Paper, Scissors, Lizard, Spock? ")
    if player == computer:
        print ("Draw")
    elif player == "Rock" or player =="rock":
        if computer == "Paper":
            print (computer, "covers", player, "you loose")
        elif computer == "Scissors":
            print (player, "crushes", computer, "you win")
        elif computer == "Spock":
            print (computer, "vaporizes", player, "you loose")
        else:
            print (player, "crushes", computer, "you win")
    elif player == "Paper" or player == "paper":
        if computer == "Scissors":
            print (computer, "cuts", player, "you loose")
        elif computer == "Spock":
            print (player, "disproves", computer, "you win")
        elif computer == "Lizard":
            print (computer, "eats", player, "you loose")
        else:
            print (player, "covers", computer, "you win")
    elif player == "Scissors" or player == "scissors":
        if computer == "Spock":
            print (computer, "smashes", player, "you loose")
        elif computer == "Lizard":
            print (player, "decapitates", computer, "you win")
        elif computer == "Rock":
            print (computer, "crushes", player, "you loose")
        else:
            print (player, "cuts", computer, "you win")
    elif player == "Lizard" or player == "lizard":
        if computer == "Rock":
            print (computer, "crushes", player, "you loose")
        elif computer == "Paper":
            print (player, "eats", computer, "you win")
        elif computer == "Scissors":
            print (computer, "decapitates", player, "you loose")
        else:
            print (player, "poisons", computer, "you win")
    elif player == "Spock" or player == "spock":
        if computer == "Lizard":
            print (computer, "poisons", player, "you loose")
        elif computer == "Rock":
            print (player, "vaporizes", computer, "you win")
        elif computer == "Paper":
            print (computer, "disproves", player, "you loose")
        else:
            print (player, "smashes", computer, "you win")
    elif player == "Q" or player == "q":
        break
    else:
        print ("Wrong input, start over")

#loop continues
    player = False
    computer = random.choice(options)

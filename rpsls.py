### Import random module
import random

### list of options
options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

def player_rock():
    if opponent == "Paper":
        print(opponent + " covers " + player + ", you loose!")
    elif opponent == "Scissors":
        print(player + " crushes " + opponent + ", you win!")
    elif opponent == "Lizard":
        print(player + " crushes " + opponent + ", you win!")
    elif opponent == "Spock":
        print(opponent + " vaporizes " + player + ", you loose!")

def player_paper():
    if opponent == "Rock":
        print(player + " covers " + opponent + ", you win!")
    elif opponent == "Scissors":
        print(opponent + " cuts " + player + ", you loose!")
    elif opponent == "Lizard":
        print(opponent + " eats " + player + ", you loose!")
    elif opponent == "Spock":
        print(player + " disproves " + opponent + ", you win!")

def player_scissors():
    if opponent == "Rock":
        print(opponent + " crushes " + player + ", you loose!")
    elif opponent == "Paper":
        print(player + " cuts " + opponent + ", you win!")
    elif opponent == "Lizard":
        print(player + " decapitates " + opponent + ", you win!")
    elif opponent == "Spock":
        print(opponent + " smashes " + player + ", you loose!")

def player_lizard():
    if opponent == "Rock":
        print(opponent + " crushes " + player + ", you loose!")
    elif opponent == "Paper":
        print(player + " eats " + opponent + ", you win!")
    elif opponent == "Scissors":
        print(opponent + " decapitates " + player + ", you loose!")
    elif opponent == "Spock":
        print(player + " poisons " + opponent + ", you win!")

def player_spock():
    if opponent == "Rock":
        print(player + " vaporizes " + opponent + ", you win!")
    elif opponent == "Paper":
        print(opponent + " disproves " + player + ", you loose!")
    elif opponent == "Scissors":
        print(player + " smashes " + opponent + ", you win!")
    elif opponent == "Lizard":
        print(opponent + " poisons " + player + ", you loose!")

### The main program
while True:
    print("[+] Game Time! [+]")
    for item in options:
            print(item, end=" ") 
    try:
        player = input("Your choice: "); ### players variable
        for i in options:
            if i != player:
                continue
            else:
                break
    except KeyboardInterrupt:
        print("Bye")
        quit()
    except:
        print("Something wrong")

    opponent = random.choice(options) ### computers variable

    if player == opponent:
        print("Draw!")
    if player == "Rock":
        player_rock()
    if player == "Paper":
        player_paper()
    if player == "Scissors":
        player_scissors()
    if player == "Lizard":
        player_lizard()
    if player == "Spock":
        player_spock()

    opponent = None

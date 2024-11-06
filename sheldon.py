import random

# list of options
options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

def player_rock(player, opponent):
    player_result = "BAZINGA!"
    if opponent == "Paper":
        player_result = opponent + " covers " + player + ", you loose!"
    if opponent == "Scissors":
        player_result = player + " crushes " + opponent + ", you win!"
    if opponent == "Lizard":
        player_result = player + " crushes " + opponent + ", you win!"
    if opponent == "Spock":
        player_result = opponent + " vaporizes " + player + ", you loose!"
    return player_result

def player_paper(player, opponent):
    player_result = "BAZINGA!"
    if opponent == "Rock":
        player_result = player + " covers " + opponent + ", you win!"
    if opponent == "Scissors":
        player_result = opponent + " cuts " + player + ", you loose!"
    if opponent == "Lizard":
        player_result = opponent + " eats " + player + ", you loose!"
    if opponent == "Spock":
        player_result = player + " disproves " + opponent + ", you win!"
    return player_result

def player_scissors(player, opponent):
    player_result = "BAZINGA!"
    if opponent == "Rock":
        player_result = opponent + " crushes " + player + ", you loose!"
    if opponent == "Paper":
        player_result = player + " cuts " + opponent + ", you win!"
    if opponent == "Lizard":
        player_result = player + " decapitates " + opponent + ", you win!"
    if opponent == "Spock":
        player_result = opponent + " smashes " + player + ", you loose!"
    return player_result

def player_lizard(player, opponent):
    player_result = "BAZINGA!"
    if opponent == "Rock":
        player_result = opponent + " crushes " + player + ", you loose!"
    if opponent == "Paper":
        player_result = player + " eats " + opponent + ", you win!"
    if opponent == "Scissors":
        player_result = opponent + " decapitates " + player + ", you loose!"
    if opponent == "Spock":
        player_result = player + " poisons " + opponent + ", you win!"
    return player_result    
        
def player_spock(player, opponent):
    player_result = "BAZINGA!"
    if opponent == "Rock":
        player_result = player + " vaporizes " + opponent + ", you win!"
    if opponent == "Paper":
        player_result = opponent + " disproves " + player + ", you loose!"
    if opponent == "Scissors":
        player_result = player + " smashes " + opponent + ", you win!"
    if opponent == "Lizard":
        player_result = opponent + " poisons " + player + ", you loose!"
    return player_result

# The main program
def main(player_choice):
    if player_choice != None:

        player = player_choice
        opponent = random.choice(options) # computers variable

        if player == opponent:
            result = "Draw!"
        if player == "Rock":
            result = player_rock(player, opponent)
        if player == "Paper":
            result = player_paper(player, opponent)
        if player == "Scissors":
            result = player_scissors(player, opponent)
        if player == "Lizard":
            result = player_lizard(player, opponent)
        if player == "Spock":
            result = player_spock(player, opponent)
        
        return result
     
    return result
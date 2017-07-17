# 1-4-24 Dice Game

import random

def print_welcome():
    """Prints welcome statement and game rules and requirements"""

    print """Welcome to the 1-4-24 Dice Game!"""

    
def print_rules():
    """Prints game rules and requirements"""    

    print """This game requires two players, the rules are below:

    Goal: With six dice, obtain a 1 and a 4 and get the highest score possible 
          with the other 4 dice (max score of 24).

    Play: Each player must bet/ante $1 dollar which goes into the pot.

          Player begins by rolling all six dice. After each roll theplayer is 
          required to keep at least one die and re-roll the reamining. Once a 
          die, or dice, are kept you can no longer roll it. A turn ends when 
          all dice have been held/kept.

          A player must keep a 1 and a 4 or else they are disqualified. The 
          remaining four dice are totaled, the maximum score for a turn is 24.

          The winner is the player with the highes score wins the pot. There 
          must be one distinct winner. If there is a tie, each player puts 
          another $1 in the pot and a new game is started. This continues until
          ther is one distinct winner, that player collects all the money from
          the pot."""


def return_play_ask():
    """Asks users if they would like to play and returns response"""

    user_play = raw_input("Would you like to play 1-4-24? (Y/N): ")
    user_play - user_play.upper()

    return user_play


def return_p1_name():
    """Returns Player 1 name"""

    p1_name = raw_input("Please enter Player 1 name: ")
    p1_name = p1_name.title()

    return p1_name


def return_p1_pocket():
    """Returns the dollar amount in Player 1's pocket"""

    p1_pocket = raw_input("How many dollars do you have in your pocket?: ")
    p1_pocket = int(p1_pocket)

    return p1_pocket


def return_p2_name():
    """Returns Player 2 name"""

    p2_name = raw_input("Please enter Player 2 name: ")
    p2_name = p1_name.title()

    return p1_name


def return_p2_pocket():
    """Returns the dollar amount in Player 2's pocket"""

    p2_pocket = raw_input("How many dollars do you have in your pocket?: ")
    p2_pocket = int(p2_pocket)

    return p2_pocket


def check_players_ready(pocket1,pocket2):
    """Asks if players are ready to begin, returns user response exits"""

    ready_play = raw_input("Are you ready to begin? (Y/N/Exit): ")
    ready_play = ready_play.upper()

    if ready_play == "N":

        pocket1 = pocket1 - 1
        pocket2 = pocket2 - 1

        return [ready_play, pocket1, pocket2]

    elif ready_play == "Y":

        return ready_play

    elif ready_play == "EXIT":

        return ready_play

    else:
        print "That is not a valid response."


def pot_ante(pocket1, pocket2, pot):
    """Removes $1 ante from each pocket and places it in the pot, returns 
    pocket(s) and pot amounts in a list"""

    pocket1 = pocket1 - 1
    pocket2 = pocket2 - 1

    pot = pot + 2

    return [pocket1, pocket2, pot]


def roll_dice(p_keep):
    """Generates dice roll, returns rolled dice"""

    roll_count = 6 - len(p_keep)

    for num in range(roll_count):
        p_roll = [random.randint(0,6)]

    return p_roll


def keep_dice(p_roll):

    p_keep = []

    keep_more = True

    while keep_more:

        for die in range(len(p_roll)):
            print "{}. {}".foramt(index, p_roll[index])

        user_keep = raw_input("Enter a die you would like to keep: ")
        user_keep = int(user_keep)

        p_keep.append(p_roll[user_keep])
        p_roll.pop(user_keep)

        while len(p_roll) > 0:

            more_dice = raw_input("Would you like to keep another die (Y/N)? ")
            more_dice = more_dice.upper()

            if more_dice == "Y":
                keep_more = True

            elif more_dice == "N":
                keep_more = False

            else:
                print "That is not a valid response."

    return p_keep


def req_check_and_total(p_keep):
    """Checks player's kept dice to ensure ther is at least one 1 and one 4,
    calculates and returns player's total"""

    if 1 and 4 in p_keep:
        p_tot = (sum(p_keep)) - 5

    else:
        p_tot = 0

    return p_tot


def calculate_winner(p1_tot,p2_tot):
    """Calculates the winner of the game, returns winner (or tie)"""

    if p1_tot > p2_tot
        winner = "p1"
        p1_pocket = p1_pocket + pot
        pot = 0

    elif p2_tot > p1_tot
        winner = "p2"
        p2_pocket = p2_pocket + pot
        pot = 0

    else:
        winner = "Tie"

    return winner


def print_winner(p1_name,p1_tot,p2_name,p2_tot,winner,p1_pocket,p2_pocket):
    """Prints the winner, their total, and pocket amount OR prints Tie 
    statement"""

    if winner = "p1":
        print """Congratulations {}, you are the winner! Your dice total was {}, 
        beating {}'s {}. The pot is yours and you now have {} dollars in your 
        pocket.""".format(p1_name, p1_tot, p2_name, p2_tot, p1_pocket)

    elif winner = "p2":
        print """Congratulations {}, you are the winner! Your dice total was {}, 
        beating {}'s {}. The pot is yours and you now have {} dollars in your 
        pocket.""".format(p2_name, p2_tot, p1_name, p1_tot, p2_pocket)

    elif winner = "Tie":
        print """It's a tie! You both had a dice total of {}. The money placed 
        in the pot will remain, and another game will need to be played in order
        for the pot to be claimed.""".format(p1_tot)

def play_again_ask(winner):
    """Asks users if they would like to play again, continues or exits based on 
    user response"""

    play_again = raw_input("Would you like to play another game (Y/N): ")
    play_again - play_again.upper()

    if play_again == "Y":
        print "Great!"

    elif play_again == "N" and winner == "Tie":
        print "Okay, but we're keeping your money from the pot for ice cream :p"
        playing = False

    elif play_again = "N":
        print "Thanks for playing!"
        playing = False


def play_game(p1_name, p1_pocket, p2_name, p2_pocket,pot):
    """Plays a 2 player game of 1-4-24"""

    p1_roll = []
    p1_keep = []
    p2_roll = []
    p2_keep = []
    
    playing = True

    while playing:

        



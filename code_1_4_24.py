# 1-4-24 Dice Game

import random

def print_welcome():
    """Prints welcome statement and game rules and requirements"""

    print
    print """Welcome to the 1-4-24 Dice Game!"""

    
def print_rules():
    """Prints game rules and requirements"""    

    print
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


def get_play_ask():
    """Asks users if they would like to play and returns response"""

    user_play = raw_input("Would you like to play 1-4-24? (Y/N): ")
    user_play = user_play.upper()

    return user_play


def get_p1_name():
    """Returns Player 1 name"""

    p1_name = raw_input("Please enter Player 1 name: ")

    if len(p1_name) < 1:
        
        p1_name = "No Name"

    p1_name = p1_name.title()

    return p1_name


def get_p1_pocket():
    """Returns the dollar amount in Player 1's pocket"""
    
    invalid = True

    while invalid:

        p1_pocket = raw_input("How many dollars do you have in your pocket?: ")

        if p1_pocket.isdigit() == True:

            p1_pocket = int(p1_pocket)

            invalid = False

        else:

            print
            print "That is not a valid response."
            print

    return p1_pocket


def get_p2_name(p1_name):
    """Returns Player 2 name"""

    p2_name = raw_input("Please enter Player 2 name: ")

    if len(p2_name) < 1:

        if p1_name == "No Name":

            p1_name = "No Name #1"

            p2_name = "No Name #2"

        else:

            p2_name = "No Name"

    p2_name = p2_name.title()

    return [p2_name, p1_name]


def get_p2_pocket():
    """Returns the dollar amount in Player 2's pocket"""

    invalid = True

    while invalid:

        p2_pocket = raw_input("How many dollars do you have in your pocket?: ")

        if p2_pocket.isdigit() == True:

            p2_pocket = int(p2_pocket)

            invalid = False

        else:

            print
            print "That is not a valid response."
            print

    return p2_pocket


def check_players_ready():
    """Asks if players are ready to begin, returns user response"""

    invalid = True

    while invalid:

        ready_play = raw_input("Are you ready to begin? (Y/N/Exit): ")
        ready_play = ready_play.upper()

        if ready_play == "N" or ready_play == "Y" or ready_play == "EXIT":
            invalid = False

        else:
            print "That is not a valid response."
            print

    return ready_play

def pot_ante(pocket1, pocket2, pot):
    """Removes $1 ante from each pocket and places it in the pot, returns 
    pocket(s) and pot amounts in a list"""

    pocket1 = pocket1 - 1
    pocket2 = pocket2 - 1

    pot = pot + 2

    ante = [pocket1, pocket2, pot]

    return ante


def roll_dice(p_keep, p_roll):
    """Generates dice roll, returns rolled dice"""

    p_roll = []

    roll_count = 6 - len(p_keep)

    for num in range(roll_count):
        p_roll.append(random.randint(1,6))

    return p_roll


def keep_dice(p_keep, p_roll):
    """Keeps dice from the roll per player's input, returns kept dice"""

    for num in range(len(p_roll)):
        print "{}. {}".format((num + 1), p_roll[(num)])

    print

    user_keep = raw_input("""Enter the number of the die/dice you would
like to keep, separated by a comma 
(remember that you must keep at least one): """)

    user_keep = user_keep.strip()
    user_keep = user_keep.split(",")
    user_keep = [int(x) for x in user_keep]

    for die in user_keep:

        p_keep.append(p_roll[(die - 1)])
    
    user_keep.sort(reverse=True)

    for die in user_keep:

        p_roll.pop((die - 1))

    if len(p_keep) < 6:

        print 
        print "Here are the dice that you have kept thus far: {}".format(p_keep)
        print

    return p_keep


def req_check_and_total(p_keep):
    """Checks player's kept dice to ensure ther is at least one 1 and one 4,
    calculates and returns player's total"""

    if 1 in p_keep and 4 in p_keep:
        p_tot = (sum(p_keep)) - 5

    else:
        p_tot = 0

    return p_tot


def calculate_winner(p1_tot,p2_tot):
    """Calculates the winner of the game, returns winner (or tie)"""

    if p1_tot > p2_tot and p2_tot != 0:
        winner = "p1"

    elif p1_tot != 0 and p2_tot == 0:
        winner = "p1-p2 bust"

    elif p2_tot > p1_tot and p1_tot != 0:
        winner = "p2"

    elif p2_tot != 0 and p1_tot == 0:
        winner = "p2-p1 bust"

    elif p1_tot == 0 and p2_tot == 0:
        winner = "both bust"

    else:
        winner = "Tie"

    return winner


def print_winner(p1_name,p1_tot,p1_keep,p2_name,p2_tot,p2_keep,winner,p1_pocket,p2_pocket):
    """Prints the winner, their total, and pocket amount OR prints Tie 
    statement"""

    print "{}'s dice: {}".format(p1_name, p1_keep)
    print
    print "{}'s dice: {}".format(p2_name, p2_keep)
    print

    if winner == "p1":
        print """Congratulations {}, you are the winner! Your dice total was {},
 beating {}'s {}. The pot is yours and you now have {} dollars in
 your pocket.""".format(p1_name, p1_tot, p2_name, p2_tot, p1_pocket)

    elif winner == "p1-p2 bust": 
        print """Congratulations {}, you are the winner! Your dice total was {},
and {} did not qualify (failed to keep a 1 and a 4). The pot
is yours and you now have {} dollars in your pocket.""".format(p1_name, p1_tot, p2_name, p1_pocket)

    elif winner == "p2":
        print """Congratulations {}, you are the winner! Your dice total was {},
eating {}'s {}. The pot is yours and you now have {} dollars in
your pocket.""".format(p2_name, p2_tot, p1_name, p1_tot, p2_pocket)

    elif winner == "p2-p1 bust":
        print """Congratulations {}, you are the winner! Your dice total was {},
and {} did not qualify (failed to keep a 1 and a 4). The pot
is yours and you now have {} dollars in your pocket.""".format(p2_name, p2_tot, p1_name, p2_pocket)

    elif winner == "both bust":
        print "Neither of you qualified, you both failed to keep a 1 and a 4! The "
        print "money placed in the pot will remain, and another game will need "
        print "to be played in order for the pot to be claimed."

    elif winner == "Tie":
        print """It's a tie! You both had a dice total of {}. The money placed in
the pot will remain, and another game will need to be played in
order for the pot to be claimed.""".format(p1_tot)

def play_again_ask(winner):
    """Asks users if they would like to play again, continues or exits based on 
    user response"""

    play_again = raw_input("Would you like to play another game (Y/N): ")
    play_again = play_again.upper()

    return play_again


def play_game(p1_name, p1_pocket, p2_name, p2_pocket, pot):
    """Plays a 2 player game of 1-4-24"""
  
    playing = True

    while playing:

        p1_roll = []
        p1_keep = []
        p2_roll = []
        p2_keep = []

        ante = pot_ante(p1_pocket, p2_pocket, pot)

        p1_pocket = ante[0]

        p2_pocket = ante[1]

        pot = ante[2]

        ready_response = check_players_ready()

        if ready_response == "EXIT":

            print
            print "Good Bye"

            playing = False

        elif ready_response == "N":

            print
            print """Okay, but we're keeping your money from the pot for ice cream :p

                     {} now has {} in thier pocket
                     {} now has {} in their pocket""".format(p1_name, p1_pocket, p2_name, p2_pocket)
        
            playing = False

        elif ready_response == "Y":

            print
            print "{}'s turn!".format(p1_name)

            while len(p1_keep) < 6:

                p1_roll = roll_dice(p1_keep, p1_roll)

                print
                print "Here are the numbers that you rolled:"
                print

                p1_keep = keep_dice(p1_keep, p1_roll)

            print
            print "Your turn is complete!"
            print
            print

            print "{}'s turn!".format(p2_name)

            while len(p2_keep) < 6:

                p2_roll = roll_dice(p2_keep, p2_roll)

                print "Here are the numbers that you rolled:"
                print

                p2_keep = keep_dice(p2_keep, p2_roll)

            print
            print "Your turn is complete!"
            print
            print

            p1_tot = req_check_and_total(p1_keep)

            p2_tot = req_check_and_total(p2_keep)

            winner = calculate_winner(p1_tot, p2_tot)

            if winner == "p1":
                p1_pocket = p1_pocket + pot
                pot = 0

            elif winner == "p1-p2 bust":
                p1_pocket = p1_pocket + pot
                pot = 0

            elif winner == "p2":
                p2_pocket = p2_pocket + pot
                pot = 0

            elif winner == "p2-p1 bust":
                p2_pocket = p2_pocket + pot
                pot = 0

            print

            print_winner(p1_name,p1_tot,p1_keep,p2_name,p2_tot,p2_keep,winner,p1_pocket,p2_pocket)

            print

            play_again = play_again_ask(winner)

            if play_again == "Y":
                print
                print "Great!"

            elif play_again == "N" and winner == "Tie":
                print
                print "Okay, but we're keeping your money from the pot for ice cream :p"
                playing = False

            elif play_again == "N":
                print
                print "Thanks for playing!"
                playing = False



print_welcome()

print_rules()

print

user_play = get_play_ask()

if user_play == "N":

    print "Okay, see you next time!"

elif user_play == "Y":

    print

    p1_name = get_p1_name()

    print

    p1_pocket = get_p1_pocket()

    print

    p2_name = get_p2_name(p1_name)

    if len(p2_name) > 1:

        p1_name = p2_name[1]

    p2_name = p2_name[0]

    print

    p2_pocket = get_p2_pocket()

    pot = 0

    print

    play_game(p1_name, p1_pocket, p2_name, p2_pocket, pot)





        



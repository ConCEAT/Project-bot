from random import randint
import os
import textwrap

def Machine(num_range, num_drawn):
    while True:
        input_players = raw_input("Type a number: ").strip()
        if input_players.lower() == "/giveup":
            print "Game > You, loser"
            break
        else:
            try:
                num_players = int(input_players)
                if num_players > num_range or num_players < 1:
                    print textwrap.fill ("You are out of chosen "
                    "range (1 to %d), get back!" % num_range, width = 57)
                else:
                    if num_players == num_drawn:
                        print textwrap.fill ("You got it! %d is "
                        "the one. Congratulations!" % num_players, width = 57)
                        break
                    elif num_players > num_drawn:
                        print "Less"
                    elif num_players < num_drawn:
                        print "More"
            except ValueError:
                print textwrap.fill ("%s is not a integer! "
                "Gimmi integers, blyat!" % input_players, width = 57)

def Draw(num_range):
    num_drawn = randint(1,num_range)
    print textwrap.fill("Your number has been drawn. "
    "You can give up by typing /giveup. Goodluck!!!", width=57)
    Machine(num_range, num_drawn)

def Startup():
    while True:
        try:
            num_range = int(raw_input("How many numbers you wanna" 
            " guess of? ").strip())
        except:
            print "There is an intiger needed!"
            continue
        if num_range < 1:
            print "Positive integer needed. Try once again."
            continue
        else:
            break
    return num_range
    
def Main():
    print "Welcome to the game, player!"
    num_range = Startup()
    Draw(num_range)
    while True:
        choose = raw_input(textwrap.fill("If you wanna play once more "
        "in the same range type /redraw or /d. If you wanna change range "
        "of numbers type /rerange or /r. If you wanna leave type /quit "
        "or /q.", width = 57)).strip().lower()
        if choose in ("/redraw", "/d"):
            Draw(num_range)
        elif choose in ("/rerange", "/r"):
            num_range = Startup()
            Draw(num_range)
        elif choose in ("/quit", "/q"):
            break
        else:
            print "There is no such a command as %s" % choose

if __name__ == "__main__":
    Main()
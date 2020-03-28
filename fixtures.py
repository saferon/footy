import random
import json
with open('scorekeeping.json', 'r') as scores:
    score_dict = json.load(scores)
with open('guesses.json', 'r') as guesses:
    guesses_dict = json.load(guesses)

gavin = 0
christie = 0
neil = 0
rambo = 0
keith = 0
hindu = 0

gavin = int(score_dict["gavin"])
gavin_guesses = guesses_dict["gavin"]

christie = int(score_dict["christie"])
christie_guesses = guesses_dict["christie"]

neil = int(score_dict["neil"])
neil_guesses = guesses_dict["neil"]

rambo = int(score_dict["rambo"])
rambo_guesses = guesses_dict["rambo"]

keith = int(score_dict["keith"])
keith_guesses = guesses_dict["keith"]

hindu = int(score_dict["hindu"])
hindu_guesses = guesses_dict["hindu"]

# christie, neil, rambo, keith, hindu, dad
# +2 points for result and score
# +1 point for score

def game1(team1, team2):
    """returns scores from a game"""
    roll1 = random.randrange(0,4)
    roll2 = random.randrange(0,4)
    print(team1 + " - " + str(roll1))
    print(team2 + " - " + str(roll2))
    if roll1 == roll2:
        if gavin_guesses[0] == gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] == christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] == neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] == rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] == keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] == hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print("It's a draw")
    elif roll1 > roll2:
        if gavin_guesses[0] > gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] > christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] > neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] > rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] > keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] > hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team1 + " is the winner")
    else:
        if gavin_guesses[0] < gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] < christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] < neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] < rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] < keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] < hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team2 + " is the winner")
    print("--------------------------------")

def game2(team1, team2):
    """returns scores from a game"""
    roll1 = random.randrange(0,4)
    roll2 = random.randrange(0,4)
    print(team1 + " - " + str(roll1))
    print(team2 + " - " + str(roll2))
    if roll1 == roll2:
        if gavin_guesses[0] == gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] == christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] == neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] == rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] == keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] == hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print("It's a draw")
    elif roll1 > roll2:
        if gavin_guesses[0] > gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] > christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] > neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] > rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] > keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] > hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team1 + " is the winner")
    else:
        if gavin_guesses[0] < gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] < christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] < neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] < rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] < keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] < hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team2 + " is the winner")
    print("--------------------------------")

def game3(team1, team2):
    """returns scores from a game"""
    roll1 = random.randrange(0,4)
    roll2 = random.randrange(0,4)
    print(team1 + " - " + str(roll1))
    print(team2 + " - " + str(roll2))
    if roll1 == roll2:
        if gavin_guesses[0] == gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] == christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] == neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] == rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] == keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] == hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print("It's a draw")
    elif roll1 > roll2:
        if gavin_guesses[0] > gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] > christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] > neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] > rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] > keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] > hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team1 + " is the winner")
    else:
        if gavin_guesses[0] < gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] < christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] < neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] < rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] < keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] < hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team2 + " is the winner")
    print("--------------------------------")

def game4(team1, team2):
    """returns scores from a game"""
    roll1 = random.randrange(0,4)
    roll2 = random.randrange(0,4)
    print(team1 + " - " + str(roll1))
    print(team2 + " - " + str(roll2))
    if roll1 == roll2:
        if gavin_guesses[0] == gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] == christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] == neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] == rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] == keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] == hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print("It's a draw")
    elif roll1 > roll2:
        if gavin_guesses[0] > gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] > christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] > neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] > rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] > keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] > hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team1 + " is the winner")
    else:
        if gavin_guesses[0] < gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] < christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] < neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] < rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] < keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] < hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team2 + " is the winner")
    print("--------------------------------")

def game5(team1, team2):
    """returns scores from a game"""
    roll1 = random.randrange(0,4)
    roll2 = random.randrange(0,4)
    print(team1 + " - " + str(roll1))
    print(team2 + " - " + str(roll2))
    if roll1 == roll2:
        if gavin_guesses[0] == gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] == christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] == neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] == rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] == keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] == hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print("It's a draw")
    elif roll1 > roll2:
        if gavin_guesses[0] > gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] > christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] > neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] > rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] > keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] > hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team1 + " is the winner")
    else:
        if gavin_guesses[0] < gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] < christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] < neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] < rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] < keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] < hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team2 + " is the winner")
    print("--------------------------------")

def game6(team1, team2):
    """returns scores from a game"""
    roll1 = random.randrange(0,4)
    roll2 = random.randrange(0,4)
    print(team1 + " - " + str(roll1))
    print(team2 + " - " + str(roll2))
    if roll1 == roll2:
        if gavin_guesses[0] == gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] == christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] == neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] == rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] == keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] == hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print("It's a draw")
    elif roll1 > roll2:
        if gavin_guesses[0] > gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] > christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] > neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] > rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] > keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] > hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team1 + " is the winner")
    else:
        if gavin_guesses[0] < gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] < christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] < neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] < rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] < keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] < hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team2 + " is the winner")
    print("--------------------------------")

def game7(team1, team2):
    """returns scores from a game"""
    roll1 = random.randrange(0,4)
    roll2 = random.randrange(0,4)
    print(team1 + " - " + str(roll1))
    print(team2 + " - " + str(roll2))
    if roll1 == roll2:
        if gavin_guesses[0] == gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] == christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] == neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] == rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] == keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] == hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print("It's a draw")
    elif roll1 > roll2:
        if gavin_guesses[0] > gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] > christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] > neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] > rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] > keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] > hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team1 + " is the winner")
    else:
        if gavin_guesses[0] < gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] < christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] < neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] < rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] < keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] < hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team2 + " is the winner")
    print("--------------------------------")

def game8(team1, team2):
    """returns scores from a game"""
    roll1 = random.randrange(0,4)
    roll2 = random.randrange(0,4)
    print(team1 + " - " + str(roll1))
    print(team2 + " - " + str(roll2))
    if roll1 == roll2:
        if gavin_guesses[0] == gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] == christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] == neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] == rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] == keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] == hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print("It's a draw")
    elif roll1 > roll2:
        if gavin_guesses[0] > gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] > christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] > neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] > rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] > keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] > hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team1 + " is the winner")
    else:
        if gavin_guesses[0] < gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] < christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] < neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] < rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] < keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] < hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team2 + " is the winner")
    print("--------------------------------")

def game9(team1, team2):
    """returns scores from a game"""
    roll1 = random.randrange(0,4)
    roll2 = random.randrange(0,4)
    print(team1 + " - " + str(roll1))
    print(team2 + " - " + str(roll2))
    if roll1 == roll2:
        if gavin_guesses[0] == gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] == christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] == neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] == rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] == keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] == hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print("It's a draw")
    elif roll1 > roll2:
        if gavin_guesses[0] > gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] > christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] > neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] > rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] > keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] > hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team1 + " is the winner")
    else:
        if gavin_guesses[0] < gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] < christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] < neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] < rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] < keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] < hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team2 + " is the winner")
    print("--------------------------------")

def game10(team1, team2):
    """returns scores from a game"""
    roll1 = random.randrange(0,4)
    roll2 = random.randrange(0,4)
    print(team1 + " - " + str(roll1))
    print(team2 + " - " + str(roll2))
    if roll1 == roll2:
        if gavin_guesses[0] == gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] == christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] == neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] == rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] == keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] == hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print("It's a draw")
    elif roll1 > roll2:
        if gavin_guesses[0] > gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] > christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] > neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] > rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] > keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] > hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team1 + " is the winner")
    else:
        if gavin_guesses[0] < gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] < christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] < neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] < rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] < keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] < hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team2 + " is the winner")
    print("--------------------------------")

def game11(team1, team2):
    """returns scores from a game"""
    roll1 = random.randrange(0,4)
    roll2 = random.randrange(0,4)
    print(team1 + " - " + str(roll1))
    print(team2 + " - " + str(roll2))
    if roll1 == roll2:
        if gavin_guesses[0] == gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] == christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] == neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] == rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] == keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] == hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print("It's a draw")
    elif roll1 > roll2:
        if gavin_guesses[0] > gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] > christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] > neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] > rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] > keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] > hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team1 + " is the winner")
    else:
        if gavin_guesses[0] < gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] < christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] < neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] < rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] < keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] < hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team2 + " is the winner")
    print("--------------------------------")

def game12(team1, team2):
    """returns scores from a game"""
    roll1 = random.randrange(0,4)
    roll2 = random.randrange(0,4)
    print(team1 + " - " + str(roll1))
    print(team2 + " - " + str(roll2))
    if roll1 == roll2:
        if gavin_guesses[0] == gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] == christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] == neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] == rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] == keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] == hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print("It's a draw")
    elif roll1 > roll2:
        if gavin_guesses[0] > gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] > christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] > neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] > rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] > keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] > hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team1 + " is the winner")
    else:
        if gavin_guesses[0] < gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] < christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] < neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] < rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] < keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] < hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team2 + " is the winner")
    print("--------------------------------")

def game13(team1, team2):
    """returns scores from a game"""
    roll1 = random.randrange(0,4)
    roll2 = random.randrange(0,4)
    print(team1 + " - " + str(roll1))
    print(team2 + " - " + str(roll2))
    if roll1 == roll2:
        if gavin_guesses[0] == gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] == christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] == neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] == rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] == keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] == hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print("It's a draw")
    elif roll1 > roll2:
        if gavin_guesses[0] > gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] > christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] > neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] > rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] > keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] > hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team1 + " is the winner")
    else:
        if gavin_guesses[0] < gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] < christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] < neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] < rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] < keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] < hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team2 + " is the winner")
    print("--------------------------------")

def game14(team1, team2):
    """returns scores from a game"""
    roll1 = random.randrange(0,4)
    roll2 = random.randrange(0,4)
    print(team1 + " - " + str(roll1))
    print(team2 + " - " + str(roll2))
    if roll1 == roll2:
        if gavin_guesses[0] == gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] == christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] == neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] == rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] == keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] == hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print("It's a draw")
    elif roll1 > roll2:
        if gavin_guesses[0] > gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] > christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] > neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] > rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] > keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] > hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team1 + " is the winner")
    else:
        if gavin_guesses[0] < gavin_guesses[1]:
            gavin += 1
            if gavin_guesses[0] == roll1 and gavin_guesses[1] == roll2:
                gavin += 2
        if christie_guesses[0] < christie_guesses[1]:
            christie += 1
            if christie_guesses[0] == roll1 and christie_guesses[1] == roll2:
                christie += 2
        if neil_guesses[0] < neil_guesses[1]:
            neil += 1
            if neil_guesses[0] == roll1 and neil_guesses[1] == roll2:
                neil += 2
        if rambo_guesses[0] < rambo_guesses[1]:
            rambo += 1
            if rambo_guesses[0] == roll1 and rambo_guesses[1] == roll2:
                rambo += 2
        if keith_guesses[0] < keith_guesses[1]:
            keith += 1
            if keith_guesses[0] == roll1 and keith_guesses[1] == roll2:
                keith += 2
        if hindu_guesses[0] < hindu_guesses[1]:
            hindu += 1
            if hindu_guesses[0] == roll1 and hindu_guesses[1] == roll2:
                hindu += 2
        print(team2 + " is the winner")
    print("--------------------------------")



##########  format, HOME TEAM, AWAY TEAM ##########
game("Rangers", "Celtic")  # 1
game("Real Madrid", "Barcelona")  # 2
game("Man United", "Man City")  # 3
game("Aberdeen", "Cove")  # 4
game("Peterhead", "Alloa")  # 5
game("Montrose", "Arbroath")  # 6
game("Liverpool", "Everton")  # 7
game("Hearts", "Hibbs")  # 8
game("Accrington Stanley", "Forrest Green")  # 9
game("Leeds", "Notts")  # 10
game("Motherwell", "Airdrie")  # 11
game("Keith", "Devronvale")  # 12
game("West Ham", "Crystal Palace")  # 13
game("West Brom", "Aston Villa")  # 14
###################################################

# Week 1

# Rangers - 1
# Celtic - 0
# Rangers is the winner
# --------------------------------
# Real Madrid - 0
# Barcelona - 1
# Barcelona is the winner
# --------------------------------
# Man United - 1
# Man City - 0
# Man United is the winner
# --------------------------------
# Aberdeen - 0
# Cove - 1
# Cove is the winner
# --------------------------------
# Peterhead - 0
# Alloa - 2
# Alloa is the winner
# --------------------------------
# Montrose - 0
# Arbroath - 0
# It's a draw
# --------------------------------
# Liverpool - 2
# Everton - 1
# Liverpool is the winner
# --------------------------------
# Hearts - 1
# Hibbs - 0
# Hearts is the winner
# --------------------------------
# Accrington Stanley - 0
# Forrest Green - 0
# It's a draw
# --------------------------------
# Leeds - 1
# Notts - 2
# Notts is the winner
# --------------------------------
# Motherwell - 1
# Airdrie - 1
# It's a draw
# --------------------------------
# Keith - 0
# Devronvale - 1
# Devronvale is the winner
# --------------------------------
# West Ham - 2
# Crystal Palace - 0
# West Ham is the winner
# --------------------------------
# West Brom - 0
# Aston Villa - 0
# It's a draw
# --------------------------------

#######################################
# one point for everything correct
# 1. D - 0
# 2. A - 1
# 3. H - 1
# 4. D - 0
# 5. A - 
# 6. D
# 7. H 
# 8. D 
# 9. H 
# 10.D 
# 11.A 
# 12. D 
# 13. A 
# 14. D 
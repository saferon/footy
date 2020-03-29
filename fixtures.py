import random
import json
with open('scorekeeping.json', 'r') as scores:
    score_dict = json.load(scores)
with open('guesses.json', 'r') as guesses:
    guesses_dict = json.load(guesses)

# christie, neil, rambo, keith, hindu, dad
# +2 points for result and score
# +1 point for score

teams = [
    "Rangers", "Celtic", "Real Madrid", "Barcelona", "Man United", "Man City",
    "Aberdeen", "Cove", "Peterhead", "Alloa", "Montrose", "Arbroath", "Liverpool", "Everton",
    "Hearts", "Hibbs", "Accrington Stanley", "Forrest Green", "Leeds", "Notts", "Motherwell", "Airdrie", 
    "Keith", "Devronvale", "West Ham", "Crystal Palace","West Brom", "Aston Villa"
        ]

def play_game(team1, team2, game):
    players = ["christie", "mupps", "rambo", "keith", "hindu", "gav"]
    roll1 = random.randint(0,4)
    roll2 = random.randint(0,4)
    if roll1 == roll2:
        for people in players:
            guess = guesses_dict[people][game]
            if guess[0] == guess[1]:
                score_dict[people] += 1
                if guess[0] == roll1 and guess[1] == roll2:
                    score_dict[people] += 2
            with open('scorekeeping.json', 'w') as dumping:
                json.dump(score_dict, dumping)
        print("It's a draw")
    elif roll1 > roll2:
        for people in players:
            guess = guesses_dict[people][game]
            if guess[0] > guess[1]:
                score_dict[people] += 1
                if guess[0] == roll1 and guess[1] == roll2:
                    score_dict[people] += 2
            with open('scorekeeping.json', 'w') as dumping:
                json.dump(score_dict, dumping)
        print(team1 + " is the winner")
    else:
        for people in players:
            guess = guesses_dict[people][game]
            if guess[0] < guess[1]:
                score_dict[people] += 1
                if guess[0] == roll1 and guess[1] == roll2:
                    score_dict[people] += 2
            with open('scorekeeping.json', 'w') as dumping:
                json.dump(score_dict, dumping)
        print(team2 + " is the winner")
    print(str(team1) + " " + str(roll1) + " - " + str(roll2)+ " " + str(team2))


def leaderboard():
    players = ["christie", "mupps", "rambo", "keith", "hindu", "gav"]
    for player in players:
        print(player + " - " + str(score_dict[player]))


##########  format, HOME TEAM, AWAY TEAM ##########
play_game("Rangers", "Celtic", 0)  # 1
play_game("Real Madrid", "Barcelona", 1)  # 2
play_game("Man United", "Man City", 2)  # 3
play_game("Aberdeen", "Cove", 3)  # 4
play_game("Peterhead", "Alloa", 4)  # 5
play_game("Montrose", "Arbroath", 5)  # 6
play_game("Liverpool", "Everton", 6)  # 7
play_game("Hearts", "Hibbs", 7)  # 8
play_game("Accrington Stanley", "Forrest Green", 8)  # 9
play_game("Leeds", "Notts", 9)  # 10
play_game("Motherwell", "Airdrie", 10)  # 11
play_game("Keith", "Devronvale", 11)  # 12
play_game("West Ham", "Crystal Palace", 12)  # 13
play_game("West Brom", "Aston Villa", 13)  # 14
###################################################
leaderboard()
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
# {"gav": 5, "keith": 4, "christie": 3, "hindu": 7, "rambo": 2, "neil": 4}

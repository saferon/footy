import random
import json
import operator
with open('scorekeeping.json', 'r') as scores:
    score_dict = json.load(scores)
with open('guesses.json', 'r') as guesses:
    guesses_dict = json.load(guesses)
with open('weekly.json', 'r') as weekly:
    weekly_dict = json.load(weekly)
# christie, neil, rambo, keith, hindu, dad
# +2 points for result and score
# +1 point for score


def play_game(team1, team2, game):
    """runs game"""
    players = ["keith", "hindu", "rambo", "mupps", "christie", "gav"]
    roll1 = random.randint(0,3)
    roll2 = random.randint(0,3)
    print("--------GAME" + " " +str(game + 1) + "--------")
    if roll1 == roll2:
        for people in players:
            guess = guesses_dict[people][game]
            if guess[0] == guess[1]:
                score_dict[people] += 1
                weekly_dict[people] += 1
                if guess[0] == roll1 and guess[1] == roll2:
                    score_dict[people] += 2
                    weekly_dict[people] += 2
            with open('scorekeeping.json', 'w') as dumping:
                json.dump(score_dict, dumping)
            with open('weekly.json', 'w') as weeklydump:
                json.dump(weekly_dict, weeklydump)
            
        # print("It's a draw")
    elif roll1 > roll2:
        for people in players:
            guess = guesses_dict[people][game]
            if guess[0] > guess[1]:
                score_dict[people] += 1
                weekly_dict[people] += 1
                if guess[0] == roll1 and guess[1] == roll2:
                    score_dict[people] += 2
                    weekly_dict[people] += 2
            with open('scorekeeping.json', 'w') as dumping:
                json.dump(score_dict, dumping)
            with open('weekly.json', 'w') as weeklydump:
                json.dump(weekly_dict, weeklydump)
        # print(team1 + " is the winner")
    else:
        for people in players:
            guess = guesses_dict[people][game]
            if guess[0] < guess[1]:
                score_dict[people] += 1
                weekly_dict[people] += 1
                if guess[0] == roll1 and guess[1] == roll2:
                    score_dict[people] += 2
                    weekly_dict[people] += 1
            with open('scorekeeping.json', 'w') as dumping:
                json.dump(score_dict, dumping)
            with open('weekly.json', 'w') as weeklydump:
                json.dump(weekly_dict, weeklydump)
        # print(team2 + " is the winner")
    print(str(team1) + " - " + str(roll1))
    print(str(team2) + " - " + str(roll2))
    print("-----------------------")


def weeklyboard():
    """prints out leaderboard for this week"""
    week = sorted(weekly_dict.items(), key=operator.itemgetter(1), reverse=True)
    print(" ")
    print("---THIS WEEKS SCORES---")
    # print(leaders)
    for player in week:
        print(str(player[0]).title() + " - " +str(player[1]))
    print("-----------------------")


def reset_weekly():
    players = ["keith", "hindu", "rambo", "mupps", "christie", "gav"]
    for people in players:
        weekly_dict[people] = 0
        with open('weekly.json', 'w') as weeklydump:
                json.dump(weekly_dict, weeklydump)


def leaderboard():
    leaders = sorted(score_dict.items(), key=operator.itemgetter(1), reverse=True)
    print(" ")
    print("------LEADERBOARD------")
    # print(leaders)
    for player in leaders:
        print(str(player[0]).title() + " - " +str(player[1]))
    print("-----------------------")


##########  format, HOME TEAM, AWAY TEAM ##########
print("-----------------------")
play_game("Aberdeen", "Hearts", 0)  # 1 
play_game("Kilmarnock", "Livingston", 1)  # 2
play_game("Rangers", "Motherwell", 2)  # 3
play_game("Ross County", "St Mirren", 3)  # 4 
play_game("St John", "Hamilton", 4)  # 5
play_game("Hibs", "Celtic", 5)  # 6
play_game("Villa", "Wolves", 6)  # 7 
play_game("Arsenal", "Norwich", 7)  # 8
play_game("Bourmouth", "Newcastle", 8)  # 9
play_game("Brighton", "Man United", 9)  # 10 
play_game("Palace", "Burnley", 10)  # 11
play_game("Watford", "Southham", 11)  # 12
play_game("Sheffield Utd", "Spurs", 12)  # 13 
play_game("West Ham", "Chelsea", 13)  # 14
play_game("Man City", "Liverpool", 14)  # 15
play_game("Everton", "Leicester", 15)  # 16 
###################################################
weeklyboard()
leaderboard()
reset_weekly()

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




# midweek scores
# christie - 0 #     (OVERALL = 3)
# rambo - 0 #        (OVERALL = 2)
# gav - 1 #          (OVERALL = 6)
# keith - 5 #        (OVERALL = 9)
# mupps - 4 #        (OVERALL = 8)
# hindu - 0 #        (OVERALL = 7)
# christie - 0 #     (OVERALL = 3)






#
#It's a draw
#Ajax 0 - 0 Real Madrid
#Celtic is the winner
#Celtic 4 - 2 Athletico Madrid
#It's a draw
#Rangers 0 - 0 Hamburg
#christie - 3
##############################3
# rambo
#It's a draw
#Aberdeen 4 - 4 Liverpool
#Chelsea is the winner
#Barcelona 1 - 3 Chelsea
#Seville is the winner
#Man City 0 - 3 Seville
#rambo - 2
#
# hindu
#Dortmund is the winner
#Dortmund 3 - 1 Leverkusen
#Juventeus is the winner
#Juventeus 4 - 0 Lazio
#It's a draw
#Wolves 0 - 0 Galatasary
#hindu - 7
#
# gav
#It's a draw
#Fingeroula 3 - 3 Espanolia
#It's a draw
#Brussia Munch 3 - 3 Elrick
#It's a draw
#Arsenal 3 - 3 Tottenham
#gav - 6
#
# mupps
#Leicester is the winner
#Leicester 3 - 1 Porto
#Marseille is the winner
#Marseille 4 - 1 Watford
#Newcastle is the winner
#Newcastle 3 - 2 Nantes
#mupps - 8
#
# keith
#
#Roma is the winner
#Roma 3 - 1 Wolfsburg
#Inter is the winner
#Getaffe 1 - 2 Inter
#Shakatier is the winner
#Shakatier 3 - 1 Olyimpiacos
#keith - 9


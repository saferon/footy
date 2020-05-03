import random
import json
import operator
with open('scorekeeping.json', 'r') as scores:
    score_dict = json.load(scores)
with open('guesses.json', 'r') as guesses:
    guesses_dict = json.load(guesses)
with open('weekly.json', 'r') as weekly:
    weekly_dict = json.load(weekly)
with open('tally.json', 'r') as tally:
    tally_dict = json.load(tally)


def play_game(team1, team2, game):
    """runs game"""
    players = ["keith", "hindu", "rambo", "mupps", "christie", "gav"]
    roll1 = random.randint(0, 3)
    roll2 = random.randint(0, 3)
    print("--------GAME" + " " +str(game + 1) + "--------")
    if roll1 == roll2:
        for people in players:
            guess = guesses_dict[people][game]
            if guess[0] == guess[1]:
                score_dict[people] += 1
                weekly_dict[people] += 1
                tally_dict[people][0] += 1
                if guess[0] == roll1 and guess[1] == roll2:
                    score_dict[people] += 3
                    weekly_dict[people] += 3
                    tally_dict[people][1] += 1
            with open('scorekeeping.json', 'w') as dumping:
                json.dump(score_dict, dumping)
            with open('weekly.json', 'w') as weeklydump:
                json.dump(weekly_dict, weeklydump)
            with open('tally.json', 'w') as tallydump:
                json.dump(tally_dict, tallydump)
        # print("It's a draw")
    elif roll1 > roll2:
        for people in players:
            guess = guesses_dict[people][game]
            if guess[0] > guess[1]:
                score_dict[people] += 1
                weekly_dict[people] += 1
                tally_dict[people][0] += 1
                if guess[0] == roll1 and guess[1] == roll2:
                    score_dict[people] += 3
                    weekly_dict[people] += 3
                    tally_dict[people][1] += 1
            with open('scorekeeping.json', 'w') as dumping:
                json.dump(score_dict, dumping)
            with open('weekly.json', 'w') as weeklydump:
                json.dump(weekly_dict, weeklydump)
            with open('tally.json', 'w') as tallydump:
                json.dump(tally_dict, tallydump)
        # print(team1 + " is the winner")
    else:
        for people in players:
            guess = guesses_dict[people][game]
            if guess[0] < guess[1]:
                score_dict[people] += 1
                weekly_dict[people] += 1
                tally_dict[people][0] += 1
                if guess[0] == roll1 and guess[1] == roll2:
                    score_dict[people] += 3
                    weekly_dict[people] += 3
                    tally_dict[people][1] += 1
            with open('scorekeeping.json', 'w') as dumping:
                json.dump(score_dict, dumping)
            with open('weekly.json', 'w') as weeklydump:
                json.dump(weekly_dict, weeklydump)
            with open('tally.json', 'w') as tallydump:
                json.dump(tally_dict, tallydump)
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
        print(str(player[0]).title() + " - " + str(player[1]) + ", from predictions: " + str(tally_dict[player[0]][0]) + ", from correct scores: " + str(tally_dict[player[0]][1]))
    print("-----------------------")


def reset_weekly():
    players = ["keith", "hindu", "rambo", "mupps", "christie", "gav"]
    for people in players:
        weekly_dict[people] = 0
        tally_dict[people][0] = 0
        tally_dict[people][1] = 0
        with open('weekly.json', 'w') as weeklydump:
            json.dump(weekly_dict, weeklydump)
        with open('tally.json', 'w') as tallydump:
            json.dump(tally_dict, tallydump)


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
play_game("Aberdeen", "St Johnstone", 0)  # 1
play_game("Killy", "Hibs", 1)  # 2
play_game("Celtic", "Hearts", 2)  # 3
play_game("Hamilton", "Huns", 3)  # 4
play_game("St Mirren", "Motherwell", 4)  # 5
play_game("Partick", "Livingston", 5)  # 6
play_game("Liverpool", "Man Utd", 6)  # 7
play_game("Arsenal", "Wolves", 7)  # 8
play_game("Chelsea", "Brighton", 8)  # 9
play_game("Leicester", "Watford", 9)  # 10
play_game("Southampton", "Norwich", 10)  # 11
play_game("Newcastle", "Southampton", 11)  # 12
play_game("Aston Villa", "Burnley", 12)  # 13
play_game("Bournemouth", "West Ham", 13)  # 14
play_game("Sheffield Utd", "Everton", 14)  # 15
play_game("Burnley", "Man City", 15)  # 16
play_game("Aughnagaatt", "Mintlaw", 16)  # 17
play_game("Ellon", "Maud", 17)  # 18
play_game("Turrrrra", "Fyvie", 18)  # 19
play_game("Peternapper", "Brochure", 19)  # 20
play_game("New Pitslago", "New Deer", 20)  # 21
play_game("Fishy", "New Leeds", 21)  # 22
play_game("Whitehills", "Bummmff", 22)  # 23
play_game("Buckie", "Elgin", 23)  # 24
play_game("Forres", "Clachnacudden", 24)  # 25
play_game("Keith", "Wick", 25)  # 26
#play_game("Malmo", "Hammerby", 26)  # 27
#play_game("Fenerbahce", "Galatasaray", 27)  # 28
#play_game("LA Galaxy", "New York Red Bulls", 28)  # 29
###################################################
weeklyboard()
leaderboard()
reset_weekly()

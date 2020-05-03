import random
import json
import operator
with open('weekly.json', 'r') as weekly:
    weekly_dict = json.load(weekly)
with open('tally.json', 'r') as tally:
    tally_dict = json.load(tally)
# christie, neil, rambo, keith, hindu, gav
# +2 points for result and score
# +1 point for score

def weeklyboard():
    """prints out leaderboard for this week"""
    week = sorted(weekly_dict.items(), key=operator.itemgetter(1), reverse=True)
    print(" ")
    print("---THIS WEEKS SCORES---")
    # print(leaders)
    for player in week:
        print(str(player[0]).title() + " - " + str(player[1]) + ", from predictions: " + str(tally_dict[player[0]][0]) + ", from correct scores: " + str(tally_dict[player[0]][1]))
    print("-----------------------")

weeklyboard()
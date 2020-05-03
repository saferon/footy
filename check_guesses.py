import json
with open('guesses.json', 'r') as guesses:
    guesses_dict = json.load(guesses)

def check_guesses():
    """checks the length of the guesses"""
    players = ["christie", "gav", "hindu", "keith", "mupps", "rambo"]
    for people in players:
        dictionary = guesses_dict[people]
        print(people + ": " + str(len(dictionary)))

check_guesses()
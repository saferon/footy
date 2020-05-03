import json
with open('guesses.json', 'r') as guesses:
    guesses_dict = json.load(guesses)

christie = input("input christies guesses: ")
gav = input("input gavs guesses: ")
hindu = input("input hindus guesses: ")
keith = input("input keiths guesses: ")
mupps = input("input mupps guesses: ")
rambo = input("input rambos guesses: ")
christie_guesses = []
gav_guesses = []
hindu_guesses = []
keith_guesses = []
mupps_guesses = []
rambo_guesses = []
valid_inputs = ["0","1","2","3"]
for letters in christie:
    if letters in valid_inputs:
        christie_guesses.append(int(letters))
for letters in gav:
    if letters in valid_inputs:
        gav_guesses.append(int(letters))
for letters in hindu:
    if letters in valid_inputs:
        hindu_guesses.append(int(letters))
for letters in keith:
    if letters in valid_inputs:
        keith_guesses.append(int(letters))
for letters in mupps:
    if letters in valid_inputs:
        mupps_guesses.append(int(letters))
for letters in rambo:
    if letters in valid_inputs:
        rambo_guesses.append(int(letters))


def sort_lists_into_lists(fixme, person):
    guesses_dict[person] = []
    small_list = []
    while len(fixme) > 0:
        small_list.append(fixme[0])
        fixme.pop(0)
        small_list.append(fixme[0])
        # print(small_list)
        fixme.pop(0)
        guesses_dict[person].append(small_list)
        small_list = []
    with open('guesses.json', 'w') as dumping:
        json.dump(guesses_dict, dumping)


def print_out_guesses():
    players = ["christie", "gav", "hindu", "keith", "mupps", "rambo"]
    for people in players:
        dictionary = guesses_dict[people]
        print(people + ": " + str(dictionary) + str(len(dictionary)))


#######################
sort_lists_into_lists(christie_guesses, "christie")
sort_lists_into_lists(gav_guesses, "gav")
sort_lists_into_lists(hindu_guesses, "hindu")
sort_lists_into_lists(keith_guesses, "keith")
sort_lists_into_lists(mupps_guesses, "mupps")
sort_lists_into_lists(rambo_guesses, "rambo")
print("Guesses taken and sorted.")
print_out_guesses()
#######################


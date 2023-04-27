#!/usr/bin/env python
from __future__ import print_function
import traceback

def main():

    #
    #  DICT
    #
    empty = {}
    print(empty)

    seahawks = {"QB": "Russell Wilson",
                "RB": "Chris Carson",
                "WR": ["Tyler Lockett", "Doug Baldwin"],
                "TE": "Will Dissly"}
    print(seahawks)

    # Make a change
    seahawks['RB'] = 'Rashaad Penny'
    print(seahawks)

    # Get a specific key
    print(seahawks["QB"])

    #
    # KEY Constraints. The Key MUST be an immutable data type
    #
    try:
        print({[1, 2, 3]: "This doesn't work"})
    except TypeError:
        print(traceback.format_exc().splitlines()[-1])

    print({(1, 2, 3): "tuples rock"})

    #
    # Multilayer dicts
    #
    OL = {"C": "Justin Britt", "G": ["Jordan Simmons", "J.R. Sweezy"], "T": ["Duane Brown", "Germain Ifedi"]}
    skill_pos = {"QB": "Russell Wilson", "RB": "Chris Carson",
                      "WR": ["Doug Baldwin", "Tyler Lockett"], "TE": ["Will Dissly", "George Fant"]}
    DL = {"DE": ["Dion Jordan", "Frank Clark"], "DT": ["Poona Ford", "Jarran Reed"]}
    LB = {"MLB": "Bobby Wagner", "OLB": ["Barkevious Mingo", "K.J. Wright"]}
    DB = {"CB": ["Tre Flowers", "Shaquill Griffin"], "FS": "Tedric Thompson", "SS": "Bradley MacDougald"}
    ST = {"P": "Michael Dickson", "K": "Sebastian Janikowski", "LS": "Tyler Ott"}
    hawks = {"offense": [OL, skill_pos], "defense": [DL, LB, DB], "specialteams": ST}
    print(hawks["offense"])


    #
    # Preventing KeyErrors
    #
    celtics = {'C': 'Kendrick Perkins', 'F': ['Kevin Garnett', 'Paul Pierce'], 'G': ['Rajon Rondo', 'Ray Allen']}

    try:
        print(celtics['SG'])
    except KeyError:
        print(traceback.format_exc().splitlines()[-1])

    """ That's not going to work, clearly, because we generalized the positions in the dict. 
        The better way is to check first """
    if 'SG' not in celtics and 'G' in celtics:
        print(celtics['G'])

    #
    #  GET()  (Another way to avoid KeyErrors) 
    #
    """ another way to do this is to use get() """
    print(celtics.get("PG"))    # This outputs None, but it doesn't generate an error.


    #
    # Copying Dicts.
    #
    all_gone = celtics.copy()
    print(all_gone)

    #
    # Clearing Dicts.
    #
    celtics.clear()
    print(celtics)  # Like I said.... All Gone!

    #
    # Merging Dictionaries.
    #
    guy = {"Harry": "Billy Crystal"}
    girl = {"Sally": "Meg Ryan"}

    when_harry_met_sally = {}
    when_harry_met_sally.update(guy)
    when_harry_met_sally.update(girl)
    print(guy)
    print(girl)
    print(when_harry_met_sally)

    #
    # Iterating over dicts
    #
    print()
    for role, actor in when_harry_met_sally.items():
        print("{} was played by {}".format(role, actor))

    for k in when_harry_met_sally.keys():
        print(k)
    for stuff in when_harry_met_sally:  # (The default is to iterate over the keys)
        print(stuff)

    for v in when_harry_met_sally.values():
        print(v)

    #
    # GETTING LENGTH OF DICT
    #
    print(len(when_harry_met_sally))

    #
    # DELETING AN ENTRY BY KILLING THE KEY
    #
    del when_harry_met_sally['Sally']
    print(when_harry_met_sally)     # Sad :(

    #
    # POP (works similar to a list, but you must provide the key, and it returns the value)
    #
    states_and_cities = {"Massachusetts": "Boston", "Vermont": "Montpelier", "New Hampshire": "Concord"}
    print(states_and_cities)
    print(states_and_cities.pop("New Hampshire"))
    print(states_and_cities.pop("Vermont", "Oh SHIT!")) # The 2nd argument is a default value, if the key doesn't exist
    print(states_and_cities.pop("Vermont", "Oh SHIT!")) # Now it prints out, because Vermont was popped.

    #
    # POP ITEM (doesn't take a parameter, it just returns an arbitrary value from the dict and returns it as
    #           a tuple)
    #
    states_and_cities = {"Massachusetts": "Boston", "Vermont": "Montpelier", "New Hampshire": "Concord"}
    for i in range(0, len(states_and_cities)):
        print(states_and_cities.popitem())






if __name__ == '__main__':
    main()
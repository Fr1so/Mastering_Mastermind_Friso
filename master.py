import random

colours = ["Red", "Blue", "Green", "Yellow", "White", "Black"]

def computerColours():
    fourColoursList = []
    for i in range(4):
        fourColoursList.append(random.choice(colours))
    return fourColoursList

def playerColours():
    fourColoursList = []
    for i in range(4):
        fourColoursList.append(input("Input colour: "))
    print(fourColoursList)

def Guess():
    fourGuessList = []
    for i in range(4):
        fourGuessList.append(input("Input colour: "))


    return [0, 1, 1, 2]

mappingDict = {"0" : "pos. + kleur = goed",
               "1" : "kleur. = goed",
               "2" : "fout"}

Wincondition =

def Game(player):

while correctVar == false:
    if Guess(input, compare) == [0, 0, 0, 0 ]:
        correctVar = true
    else:
        if player == "human":
            input = waitforinput
        """else:
            input = >> algorithm here"""

computerColours()
Guess()


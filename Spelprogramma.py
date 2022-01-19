# Importeert de random functie

import random

# Lijst met alle spellen

spelList = ["Monopoly", "Yathzee", "Bridge", "Poker", "Pesten", "Mens erger je niet", "Cluedo"]

# Random alle spellen

def spelProgramma(spelList):
    resultaten= []
    for a in range(len(spelList)):
        resultaten.append(random.choice(spelList))
    return resultaten
print("Alle random verkrijgbare spellen:")
print(spelProgramma(spelList))

# Random 3 spellen

def spelProgramma2(spelList):
    resultaten= []
    for b in range(3):
        resultaten.append(random.choice(spelList))
    return resultaten
print("3 Random spellen:")
print (spelProgramma2(spelList))

# Random 10 spellen

def spelProgramma3(spelList):
    resultaten= []
    for c in range(10):
        resultaten.append(random.choice(spelList))
    return resultaten
print("10 Random spellen:")
print(spelProgramma3(spelList))


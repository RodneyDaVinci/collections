listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listTwo = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Plus

def addAndDisplayLists (listOne, listTwo):
    resultaten= []
    for a in range (len(listOne)):
        resultaten.append(listOne[a] + listTwo[a])
    return resultaten

for a in range(len(listOne)):
    print(listOne[a], "+", listTwo[a], "=", addAndDisplayLists(listOne, listTwo)[a])

# Min

def substractAndDisplayLists (listOne, listTwo):
    resultaten= []
    for b in range (len(listOne)):
        resultaten.append(listOne[b] - listTwo[b])
    return resultaten

for b in range(len(listOne)):
    print(listOne[b], "-", listTwo[b], "=", substractAndDisplayLists(listOne, listTwo)[b])

# Keer

def multiplyAndDisplayLists(listOne, listTwo):
    resultaten= []
    for c in range (len(listOne)):
        resultaten.append(listOne[c] * listTwo[c])
    return resultaten

for c in range(len(listOne)):
    print(listOne[c], "*", listTwo[c], "=", multiplyAndDisplayLists(listOne, listTwo)[c])

# Gedeeld door

def divideAndDisplayLists(listOne, listTwo):
    resultaten= []
    for d in range (len(listOne)):
        resultaten.append(listOne[d] / listTwo[d])
    return resultaten

for d in range(len(listOne)):
    print(listOne[d], "/", listTwo[d], "=", divideAndDisplayLists(listOne, listTwo)[b])
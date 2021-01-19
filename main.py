import random

def getMatch(col):
    if len(col) < 3: return []

    listt = col[len(col)-3:len(col)] + col[0:3]

    if sum(listt[3:6]) % 10 == 0:
        result = listt[3:6]
        del col[0]
        del col[0]
        del col[0]
    elif sum(listt[2:5]) % 10 == 0:
        result = listt[2:5]
        del col[len(col)-1]
        del col[0]
        del col[0]
    elif sum(listt[1:4]) % 10 == 0:
        result = listt[1:4]
        del col[len(col)-1]
        del col[len(col)-1]
        del col[0]
    elif sum(listt[0:3]) % 10 == 0:
        result = listt[0:3]
        del col[len(col)-1]
        del col[len(col)-1]
        del col[len(col)-1]
    else:
        result = []
    return result

def layCard(col, num):
    col.append(num)
    result = []
    while True:
        new = getMatch(col)
        result += new
        if len(new) == 0:
            return result
    return result

def printCols(cols):
    print("============================")
    if len(cols) == 0:
        print()
        return
    longestColIndex = 0
    for i in range(1, len(cols)):
        if len(cols[i]) > len(cols[longestColIndex]):
            longestColIndex = i
    for rowNr in range(len(cols[longestColIndex])):
        for colNr in range(len(cols)):
            print("    " if rowNr > len(cols[colNr]) - 1 else " {0:2} ".format(cols[colNr][rowNr]), end="")
        print()
    print("============================")


def game(printing=True):
    deck = [min((i % 13) + 1, 10) for i in range(52)]
    random.shuffle(deck)
    cols = [[] for i in range(7)]
    nrOfRounds = 0
    nrOfLaidCards = 0

    while True:
        if len(cols) == 0:
            if printing: print("nrOfLaidCards:", nrOfLaidCards, "SUCCESS")
            return True
        colsCopy = cols[:]
        for i in range(len(colsCopy)):
            if printing:
                printCols(cols)
                print("Number of cards in deck:", len(deck))
                print("Number of coloumns left:", len(cols))
                print("Deck:", deck)
                input()
            if len(deck) == 0:
                if printing: print("nrOfLaidCards:", nrOfLaidCards, "fail")
                return False
            num = deck[0]
            del deck[0]
            deck += layCard(colsCopy[i], num)
            if len(colsCopy[i]) == 0:
                del cols[i - len(colsCopy) + len(cols)]
            nrOfLaidCards += 1
        nrOfRounds += 1
        if nrOfRounds > 1000:
            if printing: print("nrOfRounds: 1000+")
            # raise Exception("nrOfRounds exceeded 1000")
            return False


#
# Det er ca 2.073% win rate.
# Dette ble beregna med 6 mill forsøk 26/12 2020
#

def doStats():
    nrOfGames = 0
    nrOfSuccesses = 0
    while True:
        result = game(printing=False)
        nrOfGames += 1
        if result:
            nrOfSuccesses += 1
            # print("Success after", nrOfGames, "attempts")
            # return
        else:
            # print(nrOfGames, "attempts")
            pass
        print("{:14d}".format(nrOfSuccesses), "successes", "{:14d}".format(nrOfGames), "attempts", "{0:14.6f}%".format(100*nrOfSuccesses/nrOfGames), "win rate")

# print(game())
# doStats()

class ListIterator():
    def __init__(self, listt):
        self.listt = listt
        self.index = 0
    
    def removeByIndex(self, i):
        self.listt.pop(i)
        if i < self.index:
            self.index -= 1
    
    def __next__(self):
        self.index += 1
        if self.index >= len(self.listt):
            raise StopIteration
        return self.index, self.listt[self.index], self

class IterableList():
    def __init__(self, listt):
        self.listt = listt
    
    def __iter__(self):
        return ListIterator(self.listt)

listt = [1, 2, 1, 3, 1, 4, 1]
print(listt)
for i, val, it in IterableList(listt):
    if val == 3:
        it.removeByIndex(i)
    print(i, val, it)

print(listt)

class A():
    def __init__(self, ting):
        self.a = 0
    
    def __str__(self):
        return "yo"

a = A(34)
print(a)

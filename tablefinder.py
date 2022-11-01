from EIAMath import *


def find(cas,mor):
    row=0
    col=0
    if cas == 1:
        col = 1
        if mor == 1:
            row = 1
        elif mor == 2:
            row = 9
        elif mor == 3:
            row = 17
        elif mor == 4:
            row = 25
        elif mor == 5:
            row = 33

    elif cas == 2:
        col = 3
        if mor == 1:
            row = 1
        elif mor == 2:
            row = 9
        elif mor == 3:
            row = 17
        elif mor == 4:
            row = 25
        elif mor == 5:
            row = 33

    elif cas == 3:
        col = 5
        if mor == 1:
            row = 1
        elif mor == 2:
            row = 9
        elif mor == 3:
            row = 17
        elif mor == 4:
            row = 25
        elif mor == 5:
            row = 33

    elif cas == 4:
        col = 7
        if mor == 1:
            row = 1
        elif mor == 2:
            row = 9
        elif mor == 3:
            row = 17
        elif mor == 4:
            row = 25
        elif mor == 5:
            row = 33

    elif cas == 5:
        col = 9
        if mor == 1:
            row = 1
        elif mor == 2:
            row = 9
        elif mor == 3:
            row = 17
        elif mor == 4:
            row = 25
        elif mor == 5:
            row = 33
    tup = (row-1,col-1)
    return tup


def clause(letter, cTab, mTab):
    if letter == "r":
        print(outChitArr)
        return


def chitFinder(attack, defend, river):
    if attack == "Outflank":
        if defend == "Outflank":
            return
        elif defend == "Counter Attack":
            return
        elif defend == "Escalated Counter Attack":
            return
        elif defend == "Cordon":
            return
        elif defend == "Withdraw":
            return
        elif defend == "Defend":
            return
    elif attack == "Assault":
        if defend == "Outflank":
            return
        elif defend == "Counter Attack":
            chitTab = [2,6]
            return chitTab
        elif defend == "Escalated Counter Attack":
            chitTab = [4,6]
            return chitTab
        elif defend == "Cordon":
            if river == 1:
                clause("r",6,6)
                return
            else:
                chitTab = [6, 6]
                return chitTab
        elif defend == "Withdraw":
            chitTab = [8,6]
            return chitTab
        elif defend == "Defend":
            chitTab = [10, 6]
            return chitTab
    elif attack == "Escalated Assault":
        if defend == "Outflank":
            return
        elif defend == "Counter Attack":
            chitTab = [2, 12]
            return chitTab
        elif defend == "Escalated Counter Attack":
            chitTab = [4, 12]
            return chitTab
        elif defend == "Cordon":
            chitTab = [6, 12]
            return chitTab
        elif defend == "Withdraw":
            chitTab = [8, 12]
            return chitTab
        elif defend == "Defend":
            chitTab = [10, 12]
            return chitTab
    elif attack == "Echelon":
        if defend == "Outflank":
            return
        elif defend == "Counter attack":
            chitTab = [2, 18]
            return chitTab
        elif defend == "Escalated Counter Attack":
            chitTab = [4, 18]
            return chitTab
        elif defend == "Cordon":
            chitTab = [6, 18]
            return chitTab
        elif defend == "Withdraw":
            chitTab = [8, 18]
            return chitTab
        elif defend == "Defend":
            chitTab = [10, 18]
            return chitTab
    elif attack == "Probe":
        if defend == "Outflank":
            return
        elif defend == "Counter Attack":
            chitTab = [2, 24]
            return chitTab
        elif defend == "Escalated Counter Attack":
            chitTab = [4, 24]
            return chitTab
        elif defend == "Cordon":
            chitTab = [6, 24]
            return chitTab
        elif defend == "Withdraw":
            chitTab = [8, 24]
            return chitTab
        elif defend == "Defend":
            chitTab = [10, 24]
            return chitTab


def dieCalc(roll, arr, tableNum):
    tempArr = arr
    casRoll = tempArr[tableNum[0]+roll][tableNum[1]]
    morRoll = tempArr[tableNum[0]+roll][tableNum[1]+1]
    return(casRoll,morRoll)


def tabCalc(tup, chitArr,combArr,x,aroll,droll):
    if x == 1:
        combTup = int(chitArr[tup[0]][tup[1]]),int(chitArr[tup[0]][tup[1]+1])
        print("table:", combTup,"\nresult:",dieCalc(aroll,combArr,find(combTup[0],combTup[1])))
        combTup = int(chitArr[tup[0]+1][tup[1]]), int(chitArr[tup[0]+1][tup[1] + 1])
        print("table:", combTup, "\nresult:", dieCalc(droll, combArr, find(combTup[0], combTup[1])))
    elif x == 2:
        combTup = int(chitArr[tup[0]][tup[1]+2]), int(chitArr[tup[0]][tup[1]+3])
        print("table:", combTup, "\nresult:", dieCalc(aroll, combArr, find(combTup[0], combTup[1])))
        combTup = int(chitArr[tup[0]+1][tup[1]+2]), int(chitArr[tup[0]+1][tup[1]+3])
        print("table:", combTup, "\nresult:", dieCalc(droll, combArr, find(combTup[0], combTup[1])))
    elif x == 3:
        combTup = int(chitArr[tup[0]][tup[1]+4]), int(chitArr[tup[0]][tup[1]+5])
        print("table:", combTup, "\nresult:", dieCalc(aroll, combArr, find(combTup[0], combTup[1])))
        combTup = int(chitArr[tup[0]+1][tup[1]+4]), int(chitArr[tup[0]+1][tup[1]+5])
        print("table:", combTup, "\nresult:", dieCalc(droll, combArr, find(combTup[0], combTup[1])))


text = open("combat.csv", "r")
Arr = MakeArray(text)
chit = open("BaseChit.csv","r")
ChitArr = MakeArray(chit)
outChit = open("OutflankChit.csv", "r")
outChitArr = MakeArray(outChit)
#print("Is there a river?:")
#river = input()
#print("What is the Attacker chit?:")
#aChit = input()
#print("What is the Defender chit?:")
#dChit = input()
#tabCalc(chitFinder(aChit,dChit,river),ChitArr,Arr)
outChit.close()
chit.close()
text.close()

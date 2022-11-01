from tkinter import *
from tkinter import ttk
from EIAMath import *
from tablefinder import *

root = Tk()
root.title("EIA Calc")
root.resizable(0, 0)
root.geometry('650x350')

def printAnswer():
    #newWindow= Toplevel(root)
    #newWindow.title("EIA Calc")
    #newWindow.geometry('250x250')
    #print("Attacker Chit:", clicked.get())
    #print("Defender Chit:", clicked2.get())
    #print(clicked.get(),clicked2.get())
    #print(chitFinder(clicked.get(),clicked2.get(),river))
    arolloptions = ["Select One", 0, 1, 2, 3, 4, 5, 6, 7]
    arollclick = IntVar()
    arollclick.set("Select One")
    attackRollMenu = ttk.OptionMenu(root, arollclick, *arolloptions).place(x=300, y=24)
    attackRollLabel = ttk.Label(root, text="Attacker roll").place(x=220, y=25)
    drolloptions = ["Select One",0,1,2,3,4,5,6,7]
    drollclick = IntVar()
    drollclick.set("Select One")
    defendRollMenu = ttk.OptionMenu(root, drollclick, *drolloptions).place(x=300, y=49)
    DefendRollLabel = ttk.Label(root,text = "Defender roll").place(x=220, y=50)
    return

attackLabel = ttk.Label(root, text="Attacker Chit").place(x=20, y=25)
options = [
    "Select One",
    "Outflank",
    "Assault",
    "Escalated Assault",
    "Echelon",
    "Probe"
]
clicked = StringVar()
clicked.set("Select One")
ttk.OptionMenu(root, clicked, *options).place(x=20, y=50)

defendLabel = ttk.Label(root, text="Defender Chit").place(x=20, y=75)
optionsD = [
    "Select One",
    "Outflank",
    "Counter Attack",
    "Escalated Counter Attack",
    "Cordon",
    "Withdraw",
    "Defend"
]
clicked2 = StringVar()
clicked2.set("Select One")
ttk.OptionMenu(root, clicked2, *optionsD).place(x=20, y=100)
quitButton = ttk.Button(root, text="Quit", command=root.destroy).place(x=570, y=320)
riv =0
river = ttk.Checkbutton(root,text = "Is there a river?",variable = riv,onvalue = 1, offvalue = 0).place(x=100, y= 25)
submit = ttk.Button(root, text='Submit', command=printAnswer).place(x=20, y=200)

text = open("combat.csv", "r")
Arr = MakeArray(text)
chit = open("BaseChit.csv","r")
ChitArr = MakeArray(chit)
outChit = open("OutflankChit.csv", "r")
outChitArr = MakeArray(outChit)

outChit.close()
chit.close()
text.close()

root.mainloop()

import tkinter as t
import random as r

def computerChoice():
    number = r.choice(selection)
    return number

cc = computerChoice()
selection = ["Rock", "Scissor", "Paper"]


def conclusionMaker (pc, user):
    if pc == selection[0] and user == selection[0]:
        print("tie")
    elif pc == selection[0] and user == selection[1]:
        print("you lose")
    elif pc == selection[0] and user == selection[2]:
        print("you win")
    elif pc == selection[1] and user == selection[1]:
        print("tie")
    elif pc == selection[1] and user == selection[0]:
        print("you win")
    elif pc == selection[1] and user == selection[2]:
        print("you lose")
    elif pc == selection[2] and user == selection[2]:
        print("tie")
    elif pc == selection[2] and user == selection[0]:
        print("you lose")
    elif pc == selection[2] and user == selection[1]:
        print("you win")
    else:
        print("error")

cm = conclusionMaker(cc, user)


frame = t.Tk()
frame.title("Rock Scissor Paper")

welcomeMSG = t.Label(frame, text="Welcome to Rock Scissor Papers!")
welcomeMSG.pack(pady=10)

Rockbtn = t.Button(frame, text="Rock")
Rockbtn.pack(pady=7)

Scissorbtn = t.Button(frame, text="Scissor")
Scissorbtn.pack(pady=7)

Paperbtn = t.Button(frame, text="Paper")
Paperbtn.pack(pady=7)

computerOutput = t.Label(frame, text=cc)
computerOutput.pack(pady=8)

conclusion = t.Label(frame, text=cm)
conclusion.pack(pady=5)
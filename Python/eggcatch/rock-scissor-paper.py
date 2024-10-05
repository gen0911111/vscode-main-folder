import tkinter as t
import random as r

selection = ["Rock", "Scissor", "Paper"]

def computerChoice():
    number = r.choice(selection)
    return number


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


frame = t.Tk()
frame.title("Rock Scissor Paper")

welcomeMSG = t.Label(frame, text="Welcome to Rock Scissor Papers!")
welcomeMSG.pack(pady=10)

def btnPressed(user):
    computerOutput.config(text=f"Computer Chose:{computerChoice()}")

    cm = conclusionMaker(computerChoice(), user)
    conclusion.config(text=f"result is:{cm}")

Rockbtn = t.Button(frame, text="Rock", command=lambda:btnPressed("Rock"))
Rockbtn.pack(pady=7)

Scissorbtn = t.Button(frame, text="Scissor", command=lambda:btnPressed("Scissor"))
Scissorbtn.pack(pady=7)

Paperbtn = t.Button(frame, text="Paper", command=lambda:btnPressed("Paper"))
Paperbtn.pack(pady=7)

computerOutput = t.Label(frame, text="")
computerOutput.pack(pady=8)

conclusion = t.Label(frame, text="")
conclusion.pack(pady=5)

frame.mainloop()
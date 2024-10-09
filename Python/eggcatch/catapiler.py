import random as r
import turtle as t

t.bgcolor("lightblue")

catapiler = t.Turtle()
catapiler.shape("square")
catapiler.color("purple")
catapiler.speed(0)
catapiler.penup()
catapiler.hideturtle()

leaf = t.Turtle()
leaf.color("lightgreen")
leaf.speed()
leaf.penup()
leaf.hideturtle()
leaf.shape("triangle")

gameIsStarted = False
textTurtle = t.Turtle()
textTurtle.write("Press w to start", align="center", font=("Arial", "Bold", 12))
textTurtle.hideturtle()

scoreTurtle = t.Turtle()
scoreTurtle.hideturtle()
scoreTurtle.speed(0)

def scoreDisplay(score):
    scoreTurtle.clear()
    scoreTurtle.penup()
    x = (t.window_width()/2)-50
    y = (t.window_height()/2)-50
    scoreTurtle.setpos(x, y)
    scoreTurtle.write(str(score), align="right", font=("Arial", 12))

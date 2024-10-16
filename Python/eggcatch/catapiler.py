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

def spawnLeaf():
    leaf.hideturtle()
    leaf.setx(r.randint(-200, 200))
    leaf.sety(r.randint(-200, 200))
    leaf.showturtle()

def hitWall():
    rightWall = t.window_width()/2
    leftWall = -t.window_width()/2
    upWall = t.window_height()/2
    downWall = -t.window_height()/2
    (x,y) = catapiler.pos()
    outOfBoundary = x > rightWall or x < leftWall or y > upWall or y < downWall
    return outOfBoundary

def gameover():
    catapiler.color('red')
    leaf.color('black')
    t.penup()
    t.hideturtle()
    t.write("Game Over", align="center", font=("Arial", 20))

def gameLogic():
    global gameIsStarted
    if gameIsStarted:
        return
    gameIsStarted = True

def up():
    if catapiler.heading() == 0 or catapiler.heading() == 180:
        catapiler.setheading(90)

def down():
    if catapiler.heading() == 0 or catapiler.heading() == 180:
        catapiler.setheading(270)

def left():
    if catapiler.heading() == 90 or catapiler.heading() == 270:
        catapiler.setheading(180)

def right():
    if catapiler.heading() == 90 or catapiler.heading() == 270:
        catapiler.setheading(0)
import random as r
import turtle as t

t.bgcolor("lightblue")

catapiler = t.Turtle()
catapiler.shape("arrow")
catapiler.color("purple")
catapiler.speed(0)
catapiler.penup()
catapiler.hideturtle()

leaf = t.Turtle()
leaf.color("green")
leaf.speed()
leaf.penup()
leaf.hideturtle()
leaf.shape("turtle")

gameIsStarted = False
textTurtle = t.Turtle()
textTurtle.write("Press q to start", align="center", font=("Arial", 12, "bold"))
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
    scoreTurtle.write(str(score), align="right", font=("Arial", 30))

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

    SCORE = 0
    textTurtle.clear()

    catapiler.speed = 3
    catapiler.showturtle()
    catapiler.length =3
    catapiler.shapesize(1, catapiler.length,1)
    scoreDisplay(SCORE)
    spawnLeaf()

    while True:
        catapiler.forward(catapiler.speed)
        if catapiler.distance(leaf) < 20:
            spawnLeaf()
            SCORE += 10
            scoreDisplay(SCORE)
            catapiler.length +=1
            catapiler.speed +=1
            catapiler.shapesize(1, catapiler.length,1)
        if hitWall():
            gameover()
            break

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

t.onkey(gameLogic, "q")
t.onkey(up, "w")
t.onkey(down, "s")
t.onkey(left, "a")
t.onkey(right, "d")
t.listen()
t.mainloop()
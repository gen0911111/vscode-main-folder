from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font



# canvas
canw = 900
canh = 500

root = Tk()
root.title("Egg Catcher")
c = Canvas(root, width=canw, height=canh, background="sky blue")

c.create_rectangle(-5,
                   canh - 100,
                   canw + 5,
                   canh + 5,
                   fill="sea green",
                   width=0)
c.create_oval(-80, -80, 120, 120, fill="orange", width=0)
c.pack()

# color cycle
paint = cycle(
    ["blue", "white", "yellow", "light green", "light pink"])

# Egg size
ew = 45
eh = 55

eggscore = 1
eggspeed = 500
interval = 4000
difficulty = 0.95

# Catcher
catcolor = "brown"
catw = 200
cath = 200

catstartx = canw / 2 - catw / 2
catstartx2 = catstartx + catw

catstarty = canh / 2 - cath / 2
catstarty2 = catstarty + cath

catcher = c.create_arc(catstartx,
                       catstarty,
                       catstartx2,
                       catstarty2,
                       start=200,
                       extent=140,
                       style="arc",
                       outline=catcolor,
                       width=3)

# font for score & lives
gamefont = font.nametofont("TkFixedFont")
gamefont.config(size=18)

score = 0
scoretext = c.create_text(10, 10, anchor= "nw", font= gamefont, fill= "purple", text= "Score : " + str(score))

liveremains = 3
livestext = c.create_text(canw - 10, 10, anchor= "ne", font= gamefont, fill= "red", text= "Lives : " + str(liveremains))

eggs = [] # storing/collecting egg

def makeEgg():
  x = randrange(10, 790)
  y = 40
  newegg = c.create_oval(x, y, x+ew, y+eh, fill=next(paint), width=0)
  eggs.append(newegg)
  root.after(interval, makeEgg)

def moveEgg():
  for egg in eggs:
    (eggx, eggy, eggx2, eggy2) = c.coords(egg)
    c.move(egg, 0, 10)
    if eggy2 > canh:
      eggdrop(egg)
  root.after(eggspeed, moveEgg)

def eggdrop(egg):
  eggs.remove(egg)
  c.delete(egg)
  loselive()
  if liveremains == 0:
    messagebox.showinfo("Game Over, Final score" + str(score))
    root.destroy()

def loselive():
  global liveremains
  liveremains -= 1
  c.itemconfigure(livestext, text="Lives : " + str(liveremains))

def checkcatch():
  (ccx, ccy, ccx2, ccy2) = c.coords(catcher)
  for egg in eggs:
    (eggx, eggy, eggx2, eggy2) = c.coords(egg)
    if ccx < eggx and eggx2 < ccx2 and ccy2 - eggy2 < 40:
      eggs.remove(egg)
      c.delete(egg)
      increasescore(eggscore)
  root.after(100, checkcatch)

def increasescore(point):
  global score, eggspeed, interval
  score += point
  eggspeed = int(eggspeed*difficulty)
  interval = int(interval*difficulty)
  c.itemconfigure(scoretext, text= "Score : " + str(score))

def left(event):
  (x1, y1, x2, y2) = c.coords(catcher)
  if x1 > 10:
    c.move(catcher, -20, 0)

def right(event):
  (x1, y1, x2, y2) = c.coords(catcher)
  if x2 < canw:
    c.move(catcher, 20, 0)

c.bind("<Left>", left)
c.bind("<Right>", right)
c.focus_set()

root.after(1000, makeEgg)
root.after(1000, moveEgg)
root.after(1000, checkcatch)

root.mainloop()
from tkinter import Tk, Canvas, HIDDEN, NORMAL


def eyes():
    currentColor = ds.itemcget(eyeRightOpen, "fill")
    newColor = ds.itemcget(eyeRightClose, "fill")
    currentState = ds.itemcget(eyeRightOpen, 'state')
    newState = NORMAL if currentState == HIDDEN else HIDDEN
    ds.itemconfigure(eyeLeftOpen, fill=newColor, state=newState)
    ds.itemconfigure(eyeRightOpen, fill=newColor, state=newState)


def blink():
    eyes()
    root.after(3000, eyes)
    root.after(3000, blink)

def animate(event):
    if (70 <= event.x and event.x <= 240) and (100 <= event.y and event.y <= 130):
        #ds.itemconfigure(eyes, state=NORMAL)
        blink()

root = Tk()
root.title("Virtual Pet Blob")
ds = Canvas(root, width=400, height=400)
ds.configure(bg="orange", highlightthickness=0)
ds.bodycolor="blue"

body = ds.create_oval(20, 20, 300, 250, outline="black", fill=ds.bodycolor)
eyeLeftOpen = ds.create_oval(70, 100, 100, 130, outline="black", fill="white", state=NORMAL)
eyeRightOpen = ds.create_oval(210, 100, 240, 130, outline="black", fill="white", state=NORMAL)

eyeLeftClose = ds.create_rectangle(70, 114, 100, 116, fill="black", state=HIDDEN)
eyeRightClose = ds.create_rectangle(210, 114, 240, 116, fill="black", state=HIDDEN)

mouthNormal = ds.create_rectangle(140, 180, 170, 185, fill="black", state=NORMAL)
mouthSmile = ds.create_arc(100, 60, 220, 60, fill="pink", state=HIDDEN)



ds.pack()

ds.bind('<Motion>', animate)

#root.after(1000, blink)

root.mainloop()
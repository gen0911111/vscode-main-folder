from tkinter import Tk, Canvas, HIDDEN, NORMAL

root = Tk()
root.title("Virtual Pet Blob")
ds = Canvas(root, width=400, height=400)
ds.configure(bg="orange", highlightthickness=0)
ds.bodycolor="lightblue"

body = ds.create_oval(20, 20, 300, 250, outline="black", fill=ds.bodycolor)
eyeLeft = ds.create_oval(30, 200, 60, 230, outline="black", fill="black")
eyeRight = ds.create_oval(260, 200, 290, 230, outline="black", fill="black")
mouth = ds.create_line(100, 60, 220, 60, outline="black", fill="black")
ds.pack()



root.mainloop()
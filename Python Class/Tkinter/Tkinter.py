from tkinter import *

screen = Tk()

var_count = IntVar()
count = 0

def counter(msg):
    global count
    if msg=="add":
        count+=1
    else:
        count-=1
    var_count.set(count)
    
screen.title("WELCOME TO COUNTER APP")
screen.geometry("350x350")

btn = Button(screen, text="+",command=lambda :counter("add"),font=("Arial",20,"bold"))
btn.place(x=10,y=20)

lbl = Label(screen, textvariable=var_count,font=("Arial",20,"bold"))
lbl.place(x=80,y=30)

btn = Button(screen, text="-",command=lambda :counter("minus"),font=("Arial",20,"bold"))
btn.place(x=120,y=20)

screen.mainloop()
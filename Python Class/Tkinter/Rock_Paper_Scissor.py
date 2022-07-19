from tkinter import *
import random 

screen = Tk()

var_count = IntVar()
random = 0

screen.title("BACCHO WALA GAME")
screen.geometry("300x300")

computer_value = {"""
                  0 = Rock
                  1 = Paper
                  2 = Scissor
                  """
}

btn = Button(screen, text="Rock",font=("Arial",20,"bold"))
btn.place(x=10,y=30)

btn = Button(screen, text="Paper",font=("Arial",20,"bold"))
btn.place(x=50,y=30)

btn = Button(screen, text="Scissor",font=("Arial",20,"bold"))
btn.place(x=100,y=30)

def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text = "Player              ")
    l3.config(text = "Computer")
    l4.config(text = "")
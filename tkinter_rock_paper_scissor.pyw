from tkinter import *
import random


root = Tk()

root.geometry('750x450')


# root.resizable(0,0)
root.title("Rock Paper Scissor.....")

options = {"0":"Rock","1":"Paper","2":"Scissor"}

def button_state():
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")

def isrock():
    value = options[str(random.randint(0,2))]
    if value == "Rock":
        match_result = "Match Draw"
    elif value=="Scissor":
        match_result = "Wohoo! You Won"
    else:
        match_result = "Computer Win"
    l4.config(text=match_result)
    l1.config(text="Rock")
    l3.config(text=value)
    button_state()

def ispaper():
   value = options[str(random.randint(0, 2))]
   if value == "Paper":
      match_result = "Match Draw"
   elif value=="Scissor":
      match_result = "Computer Win"
   else:
      match_result = "Amazingg..You won"
   l4.config(text = match_result)
   l1.config(text = "Paper")
   l3.config(text = value)
   button_state()

def isscissor():
   value = options[str(random.randint(0,2))]
   if value == "Rock":
      match_result = "Computer Win"
   elif value == "Scissor":
      match_result = "Match Draw"
   else:
      match_result = "You Win... :D"
   l4.config(text = match_result)
   l1.config(text = "Scissor")
   l3.config(text = value)
   button_state()

def reset():
    b1.config(state="active")
    b2.config(state="active")
    b3.config(state="active")
    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text="")


frame = LabelFrame(root,text="Rock Paper Scissor",font=("Bell MT",20,"bold"),labelanchor="n",bd=5,bg="#bf7326",width=600,height=450,cursor="target")
frame.pack(expand=True,fill=BOTH)

l1 = Label(frame,text="Player",font=("Fira code",18,"italic"))
l1.place(relx=.18,rely = .1)

l2 = Label(frame,text="VS",font=("Fira code",18,"italic"),bg="#bf7326")
l2.place(relx=.45,rely =.1)

l3 = Label(frame,text="Computer",font=("Fira code",18,"italic"))
l3.place(relx=.65,rely = .1)

l4 = Label(frame,text="",font= ("Fira code",18,"italic"),bg = "#bf7326")
l4.place(x = 275,y = 150)


b1 = Button(frame,text = "Rock",font = ("Fira code",18,),bg = "white",width=7,command=isrock)
b1.place(x=100,y = 300)

b2 = Button(frame,text = "Paper",font = ("Fira code",18,),bg = "white",width=7,command=ispaper)
b2.place(x=225,y = 300)

b3 = Button(frame,text = "Scissor",font = ("Fira code",18,),bg = "white",width=7,command=isscissor)
b3.place(x=350,y = 300)

b4 = Button(frame,text = "RESET",font = ("Fira code",18,),bg = "red",width=7,command=reset)
b4.place(x=475,y = 300)

root.mainloop()
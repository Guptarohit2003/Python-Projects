'''from tkinter import *
import random


root = Tk()
root.geometry("600x400")
root['bg'] = "skyblue"
root.resizable(width=False,height=False)
root.title("Number Guessing Game")

TARGET = random.randint(0,100)
RETRIES = 0

def update_result(text):
    result.configure(text=text)

def new_game():
    gbut.config(state="normal")

    global TARGET, RETRIES

    TARGET = random.randint(0,100)
    RETRIES = 0
    update_result(text="Guess a number between\n 1 and 100")


def play_game():
    global RETRIES

    choice = int(numform.get())

    if choice != TARGET:

        RETRIES +=1

        result = "Wrong answer!! try again"
        if choice+10<TARGET:
            hint = "\nYour Guess is too low!!!\n"
        elif choice<TARGET:
            hint = "\nYou're so close...\n guess a little greater number\n"
        elif choice-10>TARGET:
            hint = "\nYour Guess is too high!!!\n"
        elif choice>TARGET:
            hint = "\nYou're so close...\n guess a little smaller number\n"
        result += "\n HINT:\n" + hint
    else:
        result = "You guessed the correct number aftter {} retries".format(RETRIES)
        gbut.config(state="disabled")
        result += "\n" + "Click on PLay to start a new game"
    update_result(result)



ebut = Button(root,text = "Exit",font=("Arial",14),fg = "White",bg="REd",command=exit)
ebut.place(x=280,y=320)

title = Label(root,text="WELCOME TO THE NUMBER GUESSING GAME",font=("Arial",16,"bold"),fg= "Black",bg="skyblue")

result = Label(root,text = "Click Play to start new game",font=("Arial",12,"italic"),fg = "#fffcbd",bg = "skyblue",justify=LEFT)

title.place(x = 70,y = 50)
result.place(x = 180,y = 190)

pbut = Button(root,text="Play",font=("Arial",14,"bold"),fg = "Black",bg= "#05f028",command=new_game)

gbut = Button(root,text="Guess",font = ("Arial",14),fg="#13d675",bg="Black",state="disabled",command=play_game)

pbut.place(x = 210,y = 320)
gbut.place(x=350,y = 145)

gnum = StringVar()

numform = Entry(root,font=("Arial",11),textvariable=gnum)
numform.place(x=180,y=150)

root.mainloop()'''


import tkinter as tk
import random
 
window = tk.Tk()

window.geometry("600x400")
 
window.config(bg="#065569")
 
window.resizable(width=False,height=False)
 
window.title('Number Guessing Game')
 
 
TARGET = random.randint(0, 1000)
RETRIES = 0
 
 
def update_result(text):
    result.configure(text=text)
 
def new_game():
    guess_button.config(state='normal')
    global TARGET, RETRIES
    TARGET = random.randint(0, 1000)
    RETRIES = 0
    update_result(text="Guess a number between\n 1 and 1000")

def play_game():
    global RETRIES
 
    choice = int(number_form.get())
     
    if choice != TARGET:
        RETRIES += 1
     
        result = "Wrong Guess!! Try Again"
        if TARGET < choice:
            hint = "The required number lies between 0 and {}".format(choice)
        else:
            hint = "The required number lies between {} and 1000".format(choice)
        result += "\n\nHINT :\n" + hint
     
    else:
        result = "You guessed the correct number after {} retries".format(RETRIES)
        guess_button.configure(state='disabled')
        result += "\n" + "Click on Play to start a new game"
     
    update_result(result)
 

title = tk.Label(window,text="Guessing Game",font=("Arial",24),fg="#fffcbd",bg="#065569")
 
result = tk.Label(window, text="Click on Play to start a new game", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569", justify=tk.LEFT)
 
play_button = tk.Button(window, text="Play Game", font=("Arial", 14, "bold"), fg = "Black", bg="#29c70a", command=new_game)
 
guess_button = tk.Button(window,text="Guess",font=("Arial",13), state='disabled', fg="#13d675",bg="Black", command=play_game)
 
exit_button = tk.Button(window,text="Exit Game",font=("Arial",14), fg="White", bg="#b82741", command=exit)
 
 
guessed_number = tk.StringVar()
number_form = tk.Entry(window,font=("Arial",11),textvariable=guessed_number)
 
 
 
title.place(x=170, y=50)
result.place(x=180, y=210)
 
exit_button.place(x=300,y=320)
guess_button.place(x=350, y=147) 
play_button.place(x=170, y=320)

number_form.place(x=180, y=150)
 
window.mainloop()
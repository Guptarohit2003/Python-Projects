from tkinter import *

#creating a main window

root = Tk()
root.resizable(False,False)
root.title("Tic Tac Toe")

Label(root,text="Tic Tac Toe",font=("Fira code",25)).pack()
current_chr = "X"

status_label = Label(root,text = "X's Turn",font=("Fira code",25),bg="green",fg= "snow")
status_label.pack(fill=X)

#making play Area with labels and buttons
paly_area = Frame(root,width=300,height=300,bg="white")

X_points = []
O_points = []
XO_points = []

class XOpoint:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.value = None
        self.botton = Button(paly_area,text="",width=10,height=5,command=self.set)
        self.botton.grid(row=x,column=y,padx=5,pady=5)
    
    #displaying the turn
    def set(self):
        global current_chr
        if not self.value:
            self.botton.configure(text=current_chr,bg = "snow",fg = "green")
            self.value = current_chr
            if current_chr == "X":
                X_points.append(self)
                current_chr = "O"
                status_label.configure(text = "O's Turn")
            elif current_chr == "O":
                O_points.append(self)
                current_chr = "X"
                status_label.configure(text = "X's Turn")
        check_win()

    def reset(self):
        self.botton.configure(text="",bg="white")
        if self.value == 'X':
            X_points.remove(self)
        elif self.value == 'O':
            O_points.remove(self)
        self.value = None
    
for x in range(1,4):
    for y in range(1,4):
        XOpoint(x,y)

#detecting win and draw
class WinningPossibility:
    def __init__(self,x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
    def check(self, for_chr):
        p1 = False
        p2 = False
        p3 = False
        if for_chr == "X":
            for i in X_points:
                if i.x == self.x1 and i.y == self.y1:
                    p1 = True
                elif i.x == self.x2 and i.y == self.y2:
                    p2 = True
                if i.x == self.x3 and i.y == self.y3:
                    p3 = True
        elif for_chr == "O":
            for i in O_points:
                if i.x == self.x1 and i.y == self.y1:
                    p1 = True
                elif i.x == self.x2 and i.y == self.y2:
                    p2 = True
                if i.x == self.x3 and i.y == self.y3:
                    p3 = True
        return all([p1,p2,p3])
wonning_possib = [
    WinningPossibility(1,1,1,2,1,3),
    WinningPossibility(2,1,2,2,2,3),
    WinningPossibility(3,1,3,2,3,3),
    WinningPossibility(1,1,2,1,3,1),
    WinningPossibility(1,2,2,2,3,2),
    WinningPossibility(1,3,2,3,3,3),
    WinningPossibility(1,1,2,2,3,3),
    WinningPossibility(1,3,2,2,3,1)
]
for x in range(1,4):
    for y in range(1,4):
        XO_points.append(XOpoint(x,y))

#checking who won the game and displaying
def check_win():
    for possiblity in wonning_possib:
        if possiblity.check('X'):
            status_label.configure(text = "X won!")
            disable_game()
            return
        elif possiblity.check("O"):
            status_label.configure(text="O won!")
            disable_game()
            return

    if len(X_points) + len(O_points) == 9:
        status_label.configure(text="Draw!")
        disable_game()

#disabling game
def disable_game():
    for point in XO_points:
        point.botton.configure(state = DISABLED)
    play_again_button.pack()
#play again button
def play_again():
    global current_chr
    current_chr = 'X'
    for point in XO_points:
        point.botton.configure(state = NORMAL)
        point.reset()
    status_label.configure(text = "X's turn")
    play_again_button.pack_forget()

play_again_button = Button(root,text = "Play Again",font = ("Fira code",15),command=play_again)


paly_area.pack(padx=10,pady=10)

root.mainloop()
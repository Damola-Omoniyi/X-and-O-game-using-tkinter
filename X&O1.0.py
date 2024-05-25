#This is a tic tac toe game
#This code is made using tkinter

#first the main window is created
from tkinter import *
global win
win=Tk()
win.title("X&O: FINAL VERSION")

#WIN windows
def win_x():
    '''This closes the main window and creates a new one when x wins'''
    win.destroy()
    X_win=Tk()
    frm=Frame(bg="black", width=80, height=80)
    Xwin=Label(text="X WINS!!", master=frm, height=5, width=20, fg="red",bg="black", font=("times new roman","38"))
    frm.grid()
    Xwin.grid(row=0, column=0,)
    X_win.mainloop()

def win_o():
    '''This closes the main window and creates a new one when  wins'''
    win.destroy()
    O_win=Tk()
    frm=Frame(bg="black", width=80, height=80)
    Owin=Label(text="0 WINS!!", master=frm, height=5, width=20, fg="blue",bg="black", font=("times new roman","38"))
    frm.grid()
    Owin.grid(row=0, column=0,)
    O_win.mainloop()


#turn is the value that ensures X&O are alternating:
# when a button is clicked the value of turn alternates
#this determines whose turn it is to play
global turn
turn=True

def alt():
    '''this function switches the value of turn
     and switches whose turn it is to play'''
    global turn
    if turn==True:
        turn=False
    else:
        turn=True


#chances is used for the draw system
# when all the boxes are filled we have no more chances
# leading to a draw
global chances
chances=9

def Chances():
    global chances
    chances=chances-1
    if chances==0:
        win.destroy()
        draw=Tk()
        frm=Frame(bg="black", width=80, height=80)
        lbl_draw=Label(text="DRAW!!",master=frm, height=5, width=20, fg="white",bg="black", font=("times new roman","38"))
        frm.grid()
        lbl_draw.grid(row=0, column=0,)
        draw.mainloop()


#THE WIN AND LOSS SYSTEM: there are 16 ways to win
# (8 each for x and o)
# anytime a space is filled this increases a value
# until the value reaches an amount(3)
#once 3 is reached either x or o wins
# depending on the value
global xwins_row1
xwins_row1 = 0
def XWins_row1():
    global xwins_row1
    xwins_row1 = xwins_row1 + 1

global owins_row1
owins_row1 = 0
def OWins_row1():
    global owins_row1
    owins_row1= owins_row1 + 1

global xwins_row2
xwins_row2=0
def XWins_row2():
    global xwins_row2
    xwins_row2= xwins_row2 + 1

global owins_row2
owins_row2=0
def OWins_row2():
    global owins_row2
    owins_row2= owins_row2 + 1

global xwins_row3
xwins_row3=0
def XWins_row3():
    global xwins_row3
    xwins_row3= xwins_row3 + 1

global owins_row3
owins_row3=0
def OWins_row3():
    global owins_row3
    owins_row3= owins_row3 + 1

global xwins_columnA
xwins_columnA=0
def XWins_columnA():
    global xwins_columnA
    xwins_columnA= xwins_columnA + 1

global owins_columnA
owins_columnA=0
def OWins_columnA():
    global owins_columnA
    owins_columnA = owins_columnA + 1


global xwins_columnB
xwins_columnB=0
def XWins_columnB():
    global xwins_columnB
    xwins_columnB= xwins_columnB + 1


global owins_columnB
owins_columnB=0
def OWins_columnB():
    global owins_columnB
    owins_columnB= owins_columnB + 1

global xwins_columnC
xwins_columnC=0
def XWins_columnC():
    global xwins_columnC
    xwins_columnC= xwins_columnC + 1


global owins_columnC
owins_columnC=0
def OWins_columnC():
    global owins_columnC
    owins_columnC= owins_columnC + 1

global xwins_diagonalright
xwins_diagonalright=0
def XWins_diagonalright():
    global xwins_diagonalright
    xwins_diagonalright= xwins_diagonalright + 1


global owins_diagonalright
owins_diagonalright=0
def OWins_diagonalright():
    global owins_diagonalright
    owins_diagonalright= owins_diagonalright + 1

global xwins_diagonalleft
xwins_diagonalleft=0
def XWins_diagonalleft():
    global xwins_diagonalleft
    xwins_diagonalleft= xwins_diagonalleft + 1

global owins_diagonalleft
owins_diagonalleft=0
def OWins_diagonalleft():
    global owins_diagonalleft
    owins_diagonalleft= owins_diagonalleft + 1





#FUNCTIONS: Whenever a button is clicked
# a label comes up showing the sign x or o
#and performing the necessry functions

def click1a():
    global turn
    if turn==True:
        alt()
        lbl1A = Label(text="X", bd=54, bg="black", fg="red", font=("Serif", "15", "bold"), relief=SUNKEN)
        lbl1A.grid(row=0, column=0)
        XWins_row1()
        if xwins_row1==3:
            win_x()
        XWins_columnA()
        if xwins_columnA==3:
            win_x()
        XWins_diagonalright()
        if xwins_diagonalright==3:
         win_x()
    elif turn==False:
        alt()
        lbl1A = Label(text="O", bg="black", fg="blue", bd=54, font=("Serif", "15", "bold"), relief=SUNKEN)
        lbl1A.grid(row=0, column=0)
        OWins_row1()
        if owins_row1==3:
            win_o()
        OWins_columnA()
        if owins_columnA==3:
            win_o()
        OWins_diagonalright()
        if owins_diagonalright==3:
         win_o()
    Chances()

def click1b():
    global turn
    if turn==True:
        alt()
        lbl1B = Label(text="X", bg="black", fg="red", bd=54, font=("Serif", "15", "bold"), relief=SUNKEN)
        lbl1B.grid(row=0, column=1)
        XWins_row1()
        if xwins_row1==3:
            win_x()
        XWins_columnB()
        if xwins_columnB==3:
            win_x()
    elif turn==False:
        alt()
        lbl1B = Label(text="O", bd=54, bg="black", fg="blue", font=("Serif", "15", "bold"), relief=SUNKEN)
        lbl1B.grid(row=0, column=1)
        OWins_row1()
        if owins_row1==3:
            win_o()
        OWins_columnB()
        if owins_columnB==3:
            win_o()
    Chances()


def click1c():
    global turn
    if turn==True:
        alt()
        lbl1C = Label(text="X", bd=54, bg="black", fg="red", font=("Serif", "15", "bold"), relief=SUNKEN)
        lbl1C.grid(row=0, column=2)
        XWins_row1()
        if xwins_row1==3:
            win_x()
        XWins_columnC()
        if xwins_columnC==3:
            win_x()
        XWins_diagonalleft()
        if xwins_diagonalleft==3:
            win_x()
    elif turn==False:
         alt()
         lbl1C = Label(text="O", bd=54, bg="black", fg="blue", font=("Serif", "15", "bold"), relief=SUNKEN)
         lbl1C.grid(row=0, column=2)
         OWins_row1()
         if owins_row1==3:
             win_o()
         OWins_columnC()
         if owins_columnC==3:
             win_o()
         OWins_diagonalleft()
         if owins_diagonalleft==3:
             win_o()
    Chances()

def click2a():
    global turn
    if turn==True:
        alt()
        lbl2A = Label(text="X", bd=54, bg="black", fg="red", font=("Serif", "15", "bold"), relief=SUNKEN)
        lbl2A.grid(row=1, column=0)
        XWins_row2()
        if xwins_row2==3:
            win_x()
        XWins_columnA()
        if xwins_columnA==3:
            win_x()
    elif turn==False:
         alt()
         lbl2A = Label(text="O", bd=54, bg="black", fg="blue", font=("Serif", "15", "bold"), relief=SUNKEN)
         lbl2A.grid(row=1, column=0)
         OWins_row2()
         if owins_row2==3:
             win_o()
         OWins_columnA()
         if owins_columnA==3:
            win_o()
         a=True
    Chances()


def click2b():
    global turn
    if turn==True:
        alt()
        lbl2B = Label(text="X", bd=54, bg="black", fg="red", font=("Serif", "15", "bold"), relief=SUNKEN)
        lbl2B.grid(row=1, column=1)
        XWins_row2()
        if xwins_row2==3:
            win_x()
        XWins_columnB()
        if xwins_columnB==3:
            win_x()
        XWins_diagonalright()
        if xwins_diagonalright==3:
            win_x()
        XWins_diagonalleft()
        if xwins_diagonalleft==3:
            win_x()
    elif turn==False:
         alt()
         lbl2B = Label(text="O", bd=54, bg="black", fg="blue", font=("Serif", "15", "bold"), relief=SUNKEN)
         lbl2B.grid(row=1, column=1)
         OWins_row2()
         if owins_row2==3:
             win_o()
         OWins_columnB()
         if owins_columnB==3:
             win_o()
         OWins_diagonalright()
         if owins_diagonalright==3:
             win_o()
         OWins_diagonalleft()
         if owins_diagonalleft==3:
             win_o()
    Chances()

def click2c():
    global turn
    if turn==True:
        alt()
        lbl2C = Label(text="X", bd=54, bg="black", fg="red", font=("Serif", "15", "bold"), relief=SUNKEN)
        lbl2C.grid(row=1, column=2)
        XWins_row2()
        if xwins_row2==3:
            win_x()
        XWins_columnC()
        if xwins_columnC==3:
            win_x()
    elif turn==False:
         alt()
         lbl2C = Label(text="O", bd=54, bg="black", fg="blue", font=("Serif", "15", "bold"), relief=SUNKEN)
         lbl2C.grid(row=1, column=2)
         OWins_row2()
         if owins_row2==3:
             win_o()
         OWins_columnC()
         if owins_columnC==3:
             win_o()
    Chances()

def click3a():
    global turn
    if turn==True:
        alt()
        lbl3A = Label(text="X", bd=54, bg="black", fg="red", font=("Serif", "15", "bold"), relief=SUNKEN)
        lbl3A.grid(row=2, column=0)
        XWins_row3()
        if xwins_row3==3:
            win_x()
        XWins_columnA()
        if xwins_columnA==3:
            win_x()
        XWins_diagonalleft()
        if xwins_diagonalleft==3:
            win_x()
    elif turn==False:
         alt()
         lbl3A = Label(text="O", bd=54, bg="black", fg="blue", font=("Serif", "15", "bold"), relief=SUNKEN)
         lbl3A.grid(row=2, column=0)
         OWins_row3()
         if owins_row3==3:
             win_o()
         OWins_columnA()
         if owins_columnA==3:
            win_o()
         OWins_diagonalleft()
         if owins_diagonalleft==3:
             win_o()
    Chances()

def click3b():
    global turn
    if turn==True:
        alt()
        lbl3B = Label(text="X", bd=54, bg="black", fg="red", font=("Serif", "15", "bold"), relief=SUNKEN)
        lbl3B.grid(row=2, column=1)
        XWins_row3()
        if xwins_row3==3:
            win_x()
        XWins_columnB()
        if xwins_columnB==3:
            win_x()
    elif turn==False:
         alt()
         lbl3B = Label(text="O", bd=54, bg="black", fg="blue", font=("Serif", "15", "bold"), relief=SUNKEN)
         lbl3B.grid(row=2, column=1)
         OWins_row3()
         if owins_row3==3:
            win_o()
         OWins_columnB()
         if owins_columnB==3:
             win_o()
    Chances()

def click3c():
    global turn
    if turn==True:
        alt()
        lbl3C = Label(text="X", bd=54, bg="black", fg="red", font=("Serif", "15", "bold"), relief=SUNKEN)
        lbl3C.grid(row=2, column=2)
        XWins_row3()
        if xwins_row3==3:
            win_x()
        XWins_columnC()
        if xwins_columnC==3:
            win_x()
        XWins_diagonalright()
        if xwins_diagonalright==3:
            win_x()
    elif turn==False:
         alt()
         lbl3C = Label(text="O", bd=54, bg="black", fg="blue", font=("Serif", "15", "bold"), relief=SUNKEN)
         lbl3C.grid(row=2, column=2)
         OWins_row3()
         if owins_row3==3:
             win_o()
         OWins_columnC()
         if owins_columnC==3:
             win_o()
         OWins_diagonalright()
         if owins_diagonalright==3:
             win_o()
    Chances()

#BUTTONS
btn1A=Button(text="", width=16, height=8, bg="black", command=click1a)
btn1B=Button(text="", width=16, height=8, bg="black", command=click1b)
btn1C=Button(text="", width=16, height=8, bg="black", command=click1c)
btn2A=Button(text="", width=16, height=8, bg="black", command=click2a)
btn2B=Button(text="", width=16, height=8, bg="black", command=click2b)
btn2C=Button(text="", width=16, height=8, bg="black", command=click2c)
btn3A=Button(text="", width=16, height=8, bg="black", command=click3a)
btn3B=Button(text="", width=16, height=8, bg="black", command=click3b)
btn3C=Button(text="", width=16, height=8, bg="black", command=click3c)

#GRID
btn1A.grid(row=0, column=0, padx=2, pady=2)
btn1B.grid(row=0, column=1, padx=2, pady=2)
btn1C.grid(row=0, column=2, padx=2, pady=2)
btn2A.grid(row=1, column=0, padx=2, pady=2)
btn2B.grid(row=1, column=1, padx=2, pady=2)
btn2C.grid(row=1, column=2, padx=2, pady=2)
btn3A.grid(row=2, column=0, padx=2, pady=2)
btn3B.grid(row=2, column=1, padx=2, pady=2)
btn3C.grid(row=2, column=2, padx=2, pady=2)

win.mainloop()

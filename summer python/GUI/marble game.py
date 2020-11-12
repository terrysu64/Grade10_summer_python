#Name: Terry Su
#Date: August 11, 2020
#Purpose: GUI FINAL PROJECT - Marble Game

#INITIALIZE

from tkinter import*
from tkinter import messagebox
import random

#root interface

root = Tk()
root.title('Marble Game')

#variables

LabelMessage = StringVar()
LabelMessage.set(value = 'Marble Game')

MarbleCount = 31

PlayerCount = 0

Computer = 0

MarbleList = []

MarblePic = PhotoImage(file = 'marble.gif')

MarbleNumber = DoubleVar()
MarbleNumber.set(value = 0)

#SUB PROGRAM

#menu

def how():
    print()
    print('Hello, welcome to the marble game. This is a two player game')
    print('In front of you we got 31 marbles. Each player takes turns')
    print('in taking 1-4 marbles at a time. The player to take the last marble loses!')
    print('There is an entry below the canvas where you may enter how many marbles to take.')
    print('The label will also tell you which player is going. Sorry bout the cube marbles')
    print('they were too big to fit on the screen.')
    print()
    print('Sincerely,')
    print('Terry Su')
    print()
    print()
    print('Enjoy!')

def Credits():
    print()
    print('ALL RIGHTS RESERVED')
    print('TERRY SU 2020')

#take button

def take():

    global MarbleCount
    global PlayerCount
    global Computer

    if int(MarbleNumber.get()) < 1 or int(MarbleNumber.get()) > 4:
        messagebox.showerror('Error', 'YOU MAY ONLY TAKE 1-4 MARBLES')

    if int(MarbleNumber.get()) == 1:
        c.delete(MarbleList[0])
        MarbleList.pop(0)
        MarbleCount -= 1
        PlayerCount += 1
        LabelMessage.set(str(MarbleCount) + ' marbles left!')
        print(PlayerCount)

    elif int(MarbleNumber.get()) == 2:
        for x in range(0,2):
            if MarbleList != []:
                c.delete(MarbleList[0])
                MarbleList.pop(0)
        MarbleCount -= 2
        PlayerCount += 1
        LabelMessage.set(str(MarbleCount) + ' marbles left!')

    elif int(MarbleNumber.get()) == 3:
        for x in range(0,3):
            if MarbleList != []:
                c.delete(MarbleList[0])
                MarbleList.pop(0)
        MarbleCount -= 3
        PlayerCount += 1
        LabelMessage.set(str(MarbleCount) + ' marbles left!')

    elif int(MarbleNumber.get()) == 4:
        for x in range(0,4):
            if MarbleList != []:
                c.delete(MarbleList[0])
                MarbleList.pop(0)
        MarbleCount -= 4
        PlayerCount += 1
        LabelMessage.set(str(MarbleCount) + ' marbles left!')

    if MarbleCount <= 0:
        if PlayerCount % 2 == 0:
            LabelMessage.set('PLAYER 1 WINS!')
        elif PlayerCount % 2 != 0:
            LabelMessage.set('PLAYER 2 WINS!')

#reset button
            
def reset():

    global MarbleList
    global MarbleCount
    global PlayerCount

    LabelMessage.set('Marble Game')

    c.delete(ALL)

    MarbleList = []
    
    for x in range(0,31):
        pic = c.create_image(random.randint(0,400),random.randint(0,400), anchor = CENTER, image = MarblePic)
        MarbleList.append(pic)
        
    MarbleCount = 31

    PlayerCount = 0
            

#INTERFACE PROGRAM

#menu

menubar = Menu(root) 

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = 'How To Play', command = lambda:how())
helpmenu.add_command(label = 'Credits', command = lambda:Credits())
menubar.add_cascade(label = 'Help', menu = helpmenu)
root.config(menu = menubar)

#main message label

Label(root, textvariable = LabelMessage , font = ('Arial',25,'bold', 'underline')).pack()

#canvas with marbles on it

c = Canvas(root,width = 400, height = 400)
c.config(background = 'peach puff')
c.pack()

for x in range(0,31):
    pic = c.create_image(random.randint(0,400),random.randint(0,400), anchor = CENTER, image = MarblePic)
    MarbleList.append(pic)

#take 1-4 marbles label

Label(root, text = 'Enter A Number Between 1-4', font = ('Arial', 10, 'bold')).pack()

#entry of 1-4

Entry(root, width = 8, textvariable = MarbleNumber).pack()

#take marbles button

Button(root, command = lambda:take(), text = 'Take Marbles', font = ('Arial', 10, 'bold')).pack()

#empty space

Label(root).pack()

#reset button

Button(root, command = lambda:reset(), text = 'Reset', font = ('Arial', 10, 'bold')).pack(fill = X)

#exit button

Button(root, command = lambda:root.destroy(), text = 'Exit', font = ('Arial', 10, 'bold')).pack(fill = X)


mainloop()











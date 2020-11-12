#Name: Terry Su
#Date: July 24, 2020
#Purpose: Jitterclick project for morgan su

#Import modules

from tkinter import*
import time

#Initialization

test = Tk()
test.title('Jitterclick Challenge')

count = 1
seconds = 10
timemessage = StringVar('')
scoremessage = StringVar('')

#Subprogram

def click():
    global count
    scoremessage.set('click: ' + str(count))
    count += 1

def reset():
    global count
    global seconds
    count = 1
    scoremessage.set('Clicks has been reset')
    seconds = 10
    

#Main program

labeltitle = Label(test, text = 'Lets test your skills!', font = ('Arial', 16, 'bold'))
labeltitle.pack()

labeltime = Label(test, textvariable = timemessage, font = ('Arial', 16))
labeltime.pack()

clickbutton = Button(test, text = 'CLICK ME!', command = lambda:click(), width = 30 , height = 8)
clickbutton.pack(fill = X)

resetbutton = Button(test, text = 'Reset', command = lambda:reset(), width = 30, height = 2)
resetbutton.pack(fill = X)

labelscore = Label(test, textvariable = scoremessage, font = ('Arial', 16))
labelscore.pack()

mainloop()





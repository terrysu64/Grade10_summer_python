#Name: Terry Su
#Date: July 23, 2020
#Purpose: GUI button(command button from VB) and label from ICS3U course notes

#Description: This widget displays a command button attached to a command.

#INITIALIZATION

from tkinter import*
#Imports the GUI model

master = Tk()
master.title('button and label')
#initializes the interface and gives it a title

labelString = StringVar("")
#sets labelString as a string variable

#SUBPROGRAM

def clicked(num):
    labelString.set('Clicked button' + str(num))
#sets up a function for everytime button 1 or 2 in clicked the label will display which butoon was clicked

#MAIN INTERFACE
    
button1 = Button(master,
                 text = 'clicked 1',
                 width = 9, height = 3,
                 command = lambda:clicked(1))
                #A lambda or an anonymous function is used to defer the execution of the function
                #the function will be called when the button is clicked not when created
                #Lambda expressions are usually one line functions stored in a variable that returns a value
                #they may have mutiple arguments but cannot have multiple lines
                

button2 = Button(master,
                 text = 'clicked 2',
                 width = 9, height = 3,
                 command = lambda:clicked(2))
#sets up 2 buttons with their propreties

button1.pack(side = LEFT)
button2.pack(side = RIGHT)
Label(master,
      textvariable = labelString,
      width = 20).pack()
#The pack() geometry manager organizes widgets in blocks before placing them in the interface
#it also has propreties(fill, side, and expand)

mainloop() #THIS CALL activated Python to monitor all of the widjets on the screen

    

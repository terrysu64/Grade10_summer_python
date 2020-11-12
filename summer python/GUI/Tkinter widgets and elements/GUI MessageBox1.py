#Name: Terry Su
#Date: August 11, 2020
#Purpose: GUI MessageBox1 from ICS3U course notes

#Description: This widget is used to display message boxes.

#Import

from tkinter import*
from tkinter import messagebox #The message box is a seperate module that needs to be imported

#Initialize

root = Tk()
root.title('GUI Message Box')

#Sub Program

def dialog():
    var = messagebox.showinfo('my pop up message', 'this is a baisic message pop up')

#Interface Program
    
button1 = Button(root, text = '   exit   ', width = 30, command = lambda: exit())
button2 = Button(root, text = 'Message box plz', width = 30, command = lambda: dialog())

button1.grid(column = 1, row = 2)
button2.grid(column = 1, row = 1)


root.mainloop()


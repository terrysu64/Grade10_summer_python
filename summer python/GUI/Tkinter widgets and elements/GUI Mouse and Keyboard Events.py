#Name: Terry Su
#Date: August 11, 2020
#Purpose: GUI Mouse and Keyboard Events from ICS3U course notes

#Description: It is possibleto mouse and keyboard events happening on a canvas or other widgets.

#Import

from tkinter import*

#Initialize

root = Tk()
root.title('GUI Mouse and Keyboard Events')

c = Canvas(root)
c.config(background = 'green')

#Sub Program

def mouseClick(event):
    c.create_oval(event.x,event.y,event.x,event.y,width = 1, outline = 'black', fill = 'blue')
    c.create_oval(event.x-5,event.y-5,event.x+5,event.y+5,width = 1, outline = 'red', fill = '')
    c.update()

def keyPressed(event):
    print('pressed', event.char)
    c.create_rectangle(event.x-5,event.y-5,event.x+5,event.y+5,width = 1, outline = 'red', fill = '')
    c.update()

def up(event):
    c.create_line(event.x,event.y,event.x,event.y-100)
    c.update()

c.bind("<Key>", keyPressed) #this binds every key on the keyboard to the keyPressed() function. The argument is the specific key and location pressed
c.bind("<Button-1>", mouseClick) #this binds the left click button on the mouse to the mouseClick() function
c.bind("<Up>", up) #this binds the up button to a seperate command
c.pack(fill = BOTH)
c.focus_set()

#Other special keys that you can bind include:
#Return, Escape, Down, Left, Right, Delete...
#Button-1 = left mouse button
#Button-2 = middle button
#Button-3 = right mouse button

mainloop()

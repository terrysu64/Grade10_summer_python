#Name: Terry Su
#Date: August 1, 2020
#Purpose: GUI Menu from ICS3U course notes

#Description: This widget is used to display all kinds of menus used by an application

#Import

from tkinter import*

#Initialize

root = Tk()
root.title('GUI menu')

#Subprogram

def hello():
    print('hello this is a test')
def Help():
    print('this interface is used to experiment with the menu widget')

#Interface program
menubar = Menu(root) #creates the horizontal menu bar

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = 'Open', command = lambda: hello())
filemenu.add_command(label = 'Save', command = lambda: hello())
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = lambda:root.destroy())
#creates the commands of the specific menus

menubar.add_cascade(label = 'File', menu = filemenu)
#adds the specific menu to the menubar

editmenu = Menu(menubar, tearoff = 0)
editmenu.add_command(label = 'Cut', command = lambda:hello())
editmenu.add_command(label = 'Copy', command = lambda:hello())
editmenu.add_command(label = 'Paste', command = lambda:hello())

menubar.add_cascade(label = 'Edit', menu = editmenu)
#adds a second menu to the menubar

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = 'About', command = lambda: Help())

menubar.add_cascade(label = 'Help', menu = helpmenu)
#adds a third menu to the menubar

root.config(menu = menubar)
#Adds the entire menubar with the specific menus on the interface

Label(text = 'GUI menu', font = ('Arial',13,'bold')).pack()
root.mainloop()

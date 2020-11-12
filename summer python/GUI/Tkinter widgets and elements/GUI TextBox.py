#Name: Terry Su
#Date: August 10, 2020
#Purpose: GUI TextBox from ICS3U course notes

#Description: This widget displays multiple lines of text. The text widget is used to display text documents, containing either plain
#             text or formatted text(using various fonts, embedded images...). The text widget can also be used as a text editor.
#             As such it is a complex widget. Line indexes start at 1, column indexes start at 0.

#Import

from tkinter import*

root = Tk()
root.title('GUI TextBox')

textbox = Text(root,height = 10, width = 30)
textbox.grid(row = 0, column = 0, columnspan = 3)

#Sub Program

def dump():
    print(textbox.get(1.0,END))

def clear():
    textbox.delete(1.0,END)

#Interface Program
    
textbox.insert(INSERT, 'hi\n') #\n within a string creates a new line
textbox.insert(INSERT, 'wassup\n')
textbox.insert(INSERT, 'whats goody')

dumpButton = Button(root, text = 'Print', width = 10, height = 2, command = lambda:dump())
dumpButton.grid(row = 1, column = 0)

clearButton = Button(root, text = 'Clear', width = 10, height = 2, command = lambda:clear())
clearButton.grid(row = 1, column = 1)

exitButton = Button(root, text = 'Exit', width = 10, height = 2, command = lambda:root.destroy())
exitButton.grid(row = 1, column = 2)

mainloop()



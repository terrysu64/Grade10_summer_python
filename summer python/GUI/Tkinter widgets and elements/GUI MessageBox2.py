#Name: Terry Su
#Date: August 11, 2020
#Purpose: GUI MessageBox2 from ICS3U course notes

#Description: These are the various types of message boxes that this widget may display.

#Import

from tkinter import*
from tkinter import messagebox

#Initialize

top = Tk()
top.title('GUI Message Box')

labelmessage = StringVar()
labelmessage.set(value = 'different types of message boxes')

#Sub Program

def showinfo():
    messagebox.showinfo('say hello', 'hello wrld')

def showwarning():
    messagebox.showwarning('Warning', 'you gotta virus boy')

def showerror():
    messagebox.showerror('Error', 'you got a virus for sure!')

def showquestion():
    x = messagebox.askquestion('Question', 'do you think you have a virus?')
    print(x)

def showokcancel():
    x = messagebox.askokcancel('ok cancel', 'ok to delete?')
    print(x)

def showyesno():
    x = messagebox.askyesno('Y or N', 'do u want a virus?')
    print(x)

def showretrycancel():
    x = messagebox.askretrycancel('Retry Cancel', 'virus not deleted')
    print(x)

Label(top,textvariable = labelmessage, font = ('Arial', 14, 'bold')).pack()

#Interface Program

Button(top,text = 'Info Message Box', command = lambda: showinfo()).pack(fill = X)
Button(top,text = 'Warning Message Box', command = lambda: showwarning()).pack(fill = X)
Button(top,text = 'Error Message Box', command = lambda: showerror()).pack(fill = X)
Button(top,text = 'Question Message Box', command = lambda: showquestion()).pack(fill = X)
Button(top,text = 'Ok/Cancel Message Box', command = lambda: showokcancel()).pack(fill = X)
Button(top,text = 'Y/N Message Box', command = lambda: showyesno()).pack(fill = X)
Button(top,text = 'Retry/Cancel Message Box', command = lambda: showretrycancel()).pack(fill = X)

top.mainloop()

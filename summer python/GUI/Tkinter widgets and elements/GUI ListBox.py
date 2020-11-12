#Name: Terry Su
#Date: August 2, 2020
#Purpose: GUI ListBox from ICS3U course notes

#Description: This widget is used to provide a list of options for the user.

#Import

from tkinter import *

#Initialize
master = Tk()
master.title('GUI ListBox')

info = StringVar()
info.set(value = 'add this item')

#SubProgram

def delete():
    listbox.delete(listbox.index(ACTIVE))  #the delete method is used to clear an item from a listbox
    #like lists, all elements of an array have specific indexes starting from 0
    #ACTIVE, means the index of the selected element

def delete_all():
    listbox.delete(0,END)
    #END, is the last index of the list + 1

def add():
    listbox.insert(listbox.index(ACTIVE) + 1, info.get()) # the insert method is used to add an item to a listbox

#Interface Program
    
listbox = Listbox(master)
listbox.pack()

Button(master, text = 'delete selected', command = lambda: delete()) \
.pack()
Button(master, text = 'delete all', command = lambda: delete_all()) \
.pack()
Button(master, text = 'add text', command = lambda: add()) \
.pack()
Label(master,text = '').pack()
Entry(master, width = 20, textvariable = info) \
.pack()

listbox.insert(END, 'a list entry')
for item in [1,2,3,4]:
    listbox.insert(END, item)
    
mainloop()

#Name: Terry Su
#Date: August 2, 2020
#Purpose: GUI Scroll Bar from ICS3U course notes

#Description: This widget adds the scrolling capabillity to many other widgets, such as list boxes.

#Import

from tkinter import*

#Initialize

master = Tk()
master.title('GUI Scroll Bar')

#Interface Program

scrollbar = Scrollbar(master)
scrollbar.pack(side = RIGHT, fill = Y)

listbox = Listbox(master, yscrollcommand = scrollbar.set) #yscrollcommand makes the scroll bar stay in place once its been scrolled

for i in range(100):
    listbox.insert(END, str(i))

listbox.pack(side = LEFT, fill = BOTH)

scrollbar.config(command = listbox.yview) #connects the listbox to the scroll bar

mainloop()




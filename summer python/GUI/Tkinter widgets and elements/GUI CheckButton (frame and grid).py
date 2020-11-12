#Name: Terry Su
#Date: July 24, 2020
#Purpose: GUI CheckButton(frame and grid) from ICS3U course notes

#Description: This widget is used to display the options as checkboxes. The user may select and check multiple options at once.

#INITIALIZATION

from tkinter import*
root = Tk()
root.title('CheckButton (frame and grid)')

#SUBPROGRAM

days = StringVar('')

def select():
    days.set('work days: ' + v1.get() + ' ' + v2.get() + ' ' + v3.get())

v1 = StringVar()
v1.set(value = ' ')
v2 = StringVar()
v2.set(value = ' ')
v3 = StringVar()
v3.set(value = ' ')

#MAIN INTERFACE

#label 1
lbl1 = Label(root, text = 'which days can you work?')
lbl1.grid(row = 0, sticky = W, padx = 10, pady = 5)
#Griding is a way other than pack()/packing to arrange widgets in specific positions on the interface 

#frame containing checkbuttons
frame =  Frame(root, relief = GROOVE, borderwidth = 3)
frame.grid(row = 1, sticky = W, padx = 10, pady = 5)

#checkbuttons
check1 = Checkbutton(frame,text = 'monday',variable = v1, onvalue = 'monday', offvalue = '')
check2 = Checkbutton(frame,text = 'tuesday',variable = v2, onvalue = 'tuesday', offvalue = '')
check3 = Checkbutton(frame,text = 'wednsday',variable = v3, onvalue = 'wednsday', offvalue = '')
check1.grid(row = 0, sticky = W, padx = 5)
check2.grid(row = 1, sticky = W, padx = 5)
check3.grid(row = 2, sticky = W, padx = 5)

#command button
process = Button(root,text = 'Select', width = 20, height = 2, command = lambda:select())
process.grid(row = 2, sticky = W, padx = 10,pady = 5)

#label 2
lbl2 = Label(root,textvariable = days, width = 30, anchor = W, font = ('Arial', 12, 'bold'))
lbl2.grid(row = 3, sticky = W, padx = 10, pady = 5)

#end 
mainloop()




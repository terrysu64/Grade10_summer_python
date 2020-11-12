#Name: Terry Su
#Date: July 27, 2020
#Purpose: GUI Scale from ICS3U course notes

#Description: The Scale widget allows the user to select a numerical value by moving a slider knob along the scale.
#             You can control the max/min values of the scale as well as the resolution/accuracy of the values.
#             The scale may be used as an input widget, when you want to input a numerical value.

#Importing

from tkinter import*

#Initialization

root = Tk()
root.title('GUI scale')

#Subprogram

def output():
    print(numscale.get())
    #a GUI program can create output in the main shell too

numscale = Scale(root, from_ = 10, to = 100, resolution = 0.1, orient = HORIZONTAL)
#the resolution determines the accuracy of the scale's values
#orient determines the orientation of the scale
numscale.pack()
numscale.set(50)
#the .set() method initializes a value for the scale

button = Button(root, text = 'Print', command = lambda: output())
button.pack()

mainloop()

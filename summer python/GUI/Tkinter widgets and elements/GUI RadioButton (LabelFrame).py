#Name: Terry Su
#Date: July 27, 2020
#Purpose: GUI RadioButton/option buttons (LabelFrame) from ICS3U course notes

#Description: This widget displays options as radio buttons/option buttons. The user can select only one from a group at a time.
#             Each radio button has a value and a variable.

#Import

from tkinter import*

#Initialize

root = Tk()
root.title('GUI RadioButton')

fnt = IntVar(0)
attr = IntVar(0)
m = StringVar()
m.set(value = "This is the message")

#SubProgram

def display():
    if attr.get() == 0:
        m = 'normal' #check if variable is a or m after
    elif attr.get() == 1:
        m = 'bold'
    else:
        m = 'italic'
    if fnt.get() == 0:
        message.config(font = ('Times New Roman', 15, m))
    elif fnt.get() == 1:
        message.config(font = ('Arial', 15, m))
    else:
        message.config(font = ('Vivaldi', 15, m))

#Interface program

message = Label(root, textvariable = m,
                font = ('Times New Roman', 15, 'normal'))
message.grid(row = 0, column = 0, columnspan = 2)

fontGroup = LabelFrame(root, text = 'Font', padx = 5, pady = 5)
fontGroup.grid(row = 1, column = 0)
attrGroup = LabelFrame(root, text = 'Attribute', padx = 5, pady = 5)
attrGroup.grid(row = 1, column = 1)

Radiobutton(fontGroup, text = 'Times New Roman', command = lambda: display(), variable = fnt, value = 0).grid(row = 0, sticky = W)
Radiobutton(fontGroup, text = 'Arial', command = lambda: display(), variable = fnt, value = 1).grid(row = 1, sticky = W)
Radiobutton(fontGroup, text = 'Viviladi', command = lambda: display(), variable = fnt, value = 2).grid(row = 2, sticky = W)
#The widgets are centered in their cells. You can use the sticky option to change this;
#You can align the borders along NSEW (north, south, east, west)


Radiobutton(attrGroup, text = 'Plain', command = lambda: display(), variable = attr, value = 0) \
.grid(row = 0, sticky = W)
Radiobutton(attrGroup, text = 'Bold', command = lambda: display(), variable = attr, value = 1) \
.grid(row = 1, sticky = W)
Radiobutton(attrGroup, text = 'Italic', command = lambda: display(), variable = attr, value = 2) \
.grid(row = 2, sticky = W)
#a backslash continues a line on the next


        

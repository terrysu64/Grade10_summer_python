#Date: August 30, 2021
#Name: Terry SU
#A GUI program to generate various filled or hollow geometric shapes

from tkinter import *
from tkinter import messagebox

myWindow = Tk()
myWindow.resizable(0,0)
myWindow.title("Star Patterns")
myWindow.configure(background = "#00FFFF")

colour = StringVar()
shapeVar = IntVar()
fill = IntVar()
shapeWidth = IntVar()

def clear_ButtonClicked():
    display.delete(1.0, END)
    shapeWidth.set(0)
   
def display_Square():
    display.insert(INSERT, "\n")
    if fill.get() == 2:
        for rows in range(shapeWidth.get()):
            for columns in range(shapeWidth.get()):
                display.insert(END, "* ")
            display.insert(INSERT, "\n")
    else:
        for rows in range(shapeWidth.get()):
            for columns in range(shapeWidth.get()):
                if (rows == 0 or rows == shapeWidth.get() - 1 or columns == 0 or columns == shapeWidth.get() - 1):
                    display.insert(END, "* ")
                else:
                    display.insert(END, "  ")
            display.insert(INSERT, "\n")

def display_Triangle():
    display.insert(INSERT, "\n")
    if fill.get() == 2:
        for rows in range(shapeWidth.get()):
            for columns in range(rows + 1):
                display.insert(END, "* ")
            display.insert(INSERT, "\n")
    else:
        for rows in range(shapeWidth.get()):
            for columns in range(rows + 1):
                if (rows == shapeWidth.get() - 1 or columns == 0 or columns == rows):
                    display.insert(END, "* ")
                else:
                    display.insert(END, "  ")
            display.insert(INSERT, "\n")
           
def display_Diamond():
    display.insert(INSERT, "\n")
    if shapeWidth.get() % 2 == 0:
        display.insert (INSERT, "Please choose an odd number as size!")
        display.insert(INSERT, "\n")
    else:
        if fill.get() == 1:
            for rows in range(shapeWidth.get()):
                for columns in range(shapeWidth.get()):
                    border = shapeWidth.get() // 2
                    if (rows + columns == border or columns - rows == border or rows - columns == border or rows + columns == border*3):
                        display.insert(END, "* ")
                    else :
                        display.insert(END, "  ")
                display.insert(INSERT, "\n")
        else:
            spaces = shapeWidth.get() // 2 + 1
            counter = -1
            for i in range(shapeWidth.get() // 2 + 1):
                spaces -= 1
                counter += 2
                for j in range(spaces,0,-1):
                    display.insert (END, "  ")
                for h in range(counter):
                    display.insert(END, "* ")
                display.insert (INSERT, "\n")
            spaces = 0
            counter = shapeWidth.get()
            for i in range(shapeWidth.get() // 2):
                spaces += 1
                counter -= 2
                for j in range(spaces):
                    display.insert(END, "  ")
                for h in range(counter):
                    display.insert(END, "* ") 
                display.insert (INSERT, "\n")
                
def display_X():
    display.insert(INSERT, "\n")
    if fill.get() == 2:
       sizeX = shapeWidth.get() * 4
       distance = 0
       distanceRight = sizeX

       while distance * 4 <= sizeX + shapeWidth.get() * 2:
           for count in range(sizeX):
               if distance <= count <= distance + shapeWidth.get() - 1 or distanceRight > count >= distanceRight - shapeWidth.get():
                   display.insert(END, "*  ")
               else:
                  display.insert(END, "   ")

           display.insert(INSERT, "\n")
           display.insert(INSERT, "\n")
           distance += 1
           distanceRight -= 1

       distance -= 1
       distanceRight += 1

       while distance > 0:
           distance -= 1
           distanceRight += 1
           for count in range(sizeX):
               if distance <= count <= distance + shapeWidth.get() - 1 or distanceRight > count >= distanceRight - shapeWidth.get():
                   display.insert(END, "*  ")
               else:
                   display.insert(END, "   ")

           display.insert(INSERT, "\n")
           display.insert(INSERT, "\n")

    else:
       sizeX = shapeWidth.get() * 4
       distance = 0
       distanceRight = sizeX
       for count in range(sizeX + 1):
           if distance <= count <= distance + shapeWidth.get() - 1 or distanceRight >= count > distanceRight - shapeWidth.get():
               display.insert(END, "*  ")
           else:
               display.insert(END, "   ")

       display.insert(INSERT, "\n")
       display.insert(INSERT, "\n")
       distance = 1

       while distance * 4 <= sizeX + shapeWidth.get() * 3:
           for count in range(sizeX):
               if (distance == count) or (distance + shapeWidth.get() - 1 == count and distance < sizeX // 4 + 2) or \
                       (distanceRight - 1 == count) or (
                       distanceRight - shapeWidth.get() == count and distance < sizeX // 4 + 2):
                   display.insert(END, "*  ")
               else:
                   display.insert(END, "   ")

           display.insert(INSERT, "\n")
           display.insert(INSERT, "\n")
           distance += 1
           distanceRight -= 1

       distance -= 1
       distanceRight += 1

       while distance > 1:
           distance -= 1
           distanceRight += 1
           for count in range(sizeX):
               if (distance == count) or (distance + shapeWidth.get() - 1 == count and distance < sizeX // 4 + 2) or \
                       (distanceRight - 1 == count) or (
                       distanceRight - shapeWidth.get() == count and distance < sizeX // 4 + 2):
                   display.insert(END, "*  ")
               else:
                   display.insert(END, "   ")

           display.insert(INSERT, "\n")
           display.insert(INSERT, "\n")

       distance = 0

       for count in range(sizeX + 1):
           if distance <= count <= distance + shapeWidth.get() - 1 or distanceRight >= count > distanceRight - shapeWidth.get():
               display.insert(END, "*  ")
           else:
               display.insert(END, "   ")

       display.insert(INSERT, "\n")
    display.insert(INSERT, "\n")
    
def print_ButtonClicked():
    display.delete(1.0, END)
    shape = shapeVar.get()
    if shape != 1 and shape != 2 and shape != 3 and shape != 4 or fill.get() != 2 and fill.get() != 1:
        display.insert(INSERT, "\n")
        display.insert (INSERT, "Please select a shape and a pattern!")
        display.insert(INSERT, "\n")
    else:
        if shape == 1:
            display_Triangle()
        elif shape == 2:
            display_Square()
        elif shape == 3:
            display_Diamond()
        else:
            display_X()

myWindowTitle = Label(myWindow, text = "Star Patterns", font = ("Times New Roman", "30", "bold", "italic"), fg = "#4169E1", bg = "#00FFFF")

myWindowSizeLabel = Label(myWindow, text = "Select A Size Value:", font = ("Times New Roman", "15", "normal"), fg = "#4169E1", bg = "#00FFFF")
shapeWidth = Scale(myWindow, from_=1, to=20, orient = HORIZONTAL, length = 290, font = ("Times New Roman", "12", "normal"), fg = "#4169E1", bg = "#00FFFF")

myWindowShapeFrame = LabelFrame(myWindow, text = "Shape", font = ("Times New Roman", "15", "normal"), fg = "#4169E1", bg = "#00FFFF")
myWindowTypeFrame = LabelFrame(myWindow, text = "Type", font = ("Times New Roman", "15", "normal"), fg = "#4169E1", bg = "#00FFFF")

myWindowTriangle = Radiobutton(myWindowShapeFrame, text = "Triangle", variable = shapeVar, value = 1, font = ("Times New Roman", "15", "normal"), fg = "#4169E1", bg = "#00FFFF")
myWindowSquare = Radiobutton(myWindowShapeFrame, text = "Square", variable = shapeVar, value = 2, font = ("Times New Roman", "15", "normal"), fg = "#4169E1", bg = "#00FFFF")
myWindowDiamond = Radiobutton(myWindowShapeFrame, text = "Diamond", variable = shapeVar, value = 3, font = ("Times New Roman", "15", "normal"), fg = "#4169E1", bg = "#00FFFF")
myWindowX = Radiobutton(myWindowShapeFrame, text = "X", variable = shapeVar, value = 4, font = ("Times New Roman", "15", "normal"), fg = "#4169E1", bg = "#00FFFF")

myWindowHollow = Radiobutton(myWindowTypeFrame, text = "Hollow", variable = fill, value = 1, font = ("Times New Roman", "15", "normal"), fg = "#4169E1", bg = "#00FFFF")
myWindowFilled = Radiobutton(myWindowTypeFrame, text = "Filled", variable = fill, value = 2, font = ("Times New Roman", "15", "normal"), fg = "#4169E1", bg = "#00FFFF")

myWindowGenerateShapeButton = Button(myWindow, text = "Generate Shape", command = lambda: print_ButtonClicked(), pady = 5, padx = 5, font = ("Times New Roman", "15", "normal"), width = 25, fg = "#4169E1")
myWindowClearButton = Button(myWindow, text = "Clear", command = lambda: clear_ButtonClicked(), pady = 5, padx = 5, font = ("Times New Roman", "15", "normal"), width = 25, fg = "#4169E1")

frame = Frame(myWindow)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=E+W)
yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=N+S)

display = Text(frame, wrap=NONE, bd=1, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, height = 20, width = 57)
display.grid(row=0, column=0, sticky=N+S+E+W)
xscrollbar.config(command=display.xview)
yscrollbar.config(command=display.yview)

myWindowTitle.grid(row=1, column=1, columnspan = 2)
myWindowShapeFrame.grid(row = 3, column = 2)
myWindowTriangle.grid(row = 2, column = 1)
myWindowSquare.grid(row = 2, column = 2)
myWindowDiamond.grid(row = 2, column = 3)
myWindowX.grid(row = 2, column = 4)
myWindowTypeFrame.grid(row = 3, column = 1)
myWindowHollow.grid(row = 2, column = 1)
myWindowFilled.grid(row = 2, column = 2)
myWindowSizeLabel.grid(row = 4, column = 1)
shapeWidth.grid(row = 4, column = 2)
myWindowGenerateShapeButton.grid(row = 5, column = 1, columnspan = 2)
frame.grid(row = 6, column = 1, columnspan = 2)
myWindowClearButton.grid(row = 7, column = 1, columnspan = 2)

mainloop()

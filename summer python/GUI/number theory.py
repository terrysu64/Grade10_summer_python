#Name: Terry Su
#Date: August 20, 2020
#Purpose: a GUI program for number theory calculations

from tkinter import * 
from tkinter import messagebox 

#INIT

myWindow = Tk() 
myWindow.title('Number Theory')
myWindow.configure(background = "#009B77")
myWindow.resizable(0,0) 

objN = StringVar()      
objR = StringVar()      
objOutput = StringVar() 
objFeedback = StringVar()
fnt = IntVar(0)
attr = IntVar(0)

#OPERATIONS

def clearButtonClicked():
    objN.set("")
    objR.set("")
    objOutput.set("")
    objFeedback.set("")
    widScaleFeedback.set(0)


def calcFactorial(integer):
    intNumber = integer
    factorial = 1

    while intNumber > 0:
        factorial = factorial * intNumber
        intNumber -= 1

    return factorial

def calcPermutations(integerN, integerR):

    if integerN < integerR:
        temp = integerN
        integerN = integerR
        integerR = temp
    permutation = calcFactorial(integerN) / calcFactorial(integerN - integerR)

    return permutation

def permButtonClicked():
    strN = objN.get()
    strR = objR.get()

    if strN.isdigit() and strR.isdigit():
        intN = int(strN)
        intR = int(strR)

        if (intN > 75) or (intR > 75):
            objOutput.set("INVALID INPUT! NUMBER MUST BE LESS THAN EQUAL TO 75!")
        else:
            answer = int((calcPermutations(intN,intR)))
            objOutput.set("Your permutation of the two integers is: " + str(answer))
    else:
        objOutput.set("INVALID INPUT! ENTER TWO POSTIVE INTEGERS!")

def calcCombinations(integerN, integerR):

    if integerN < integerR:
        temp = integerN
        integerN = integerR
        integerR = temp
    combination = calcFactorial(integerN) / (calcFactorial(integerR) * calcFactorial(integerN - integerR))

    return combination


def combButtonClicked():
    strN = objN.get()
    strR = objR.get()

    if strN.isdigit() and strR.isdigit():
        intN = int(strN)
        intR = int(strR)

        if (intN > 75) or (intR > 75):
            objOutput.set("INVALID INPUT! NUMBER MUST BE LESS THAN EQUAL TO 75!")
        else:
            answer = int((calcCombinations(intN,intR)))
            objOutput.set("Your combination of the two integers is: " + str(answer))
    else:
        objOutput.set("INVALID INPUT! ENTER TWO POSTIVE INTEGERS!")

def calcGCD(integerM, integerN):

    if integerN == 0 or integerM == 0:
        integerN = "undefined"
    else:
        t = integerM % integerN

        while t != 0:
            integerM = integerN
            integerN = t
            t = integerM % integerN
    
    return integerN

def gcdButtonClicked():
    strN = objN.get()
    strR = objR.get()

    if strN.isdigit() and strR.isdigit():
        intN = int(strN)
        intR = int(strR)

        if (intN > 75) or (intR > 75):
            objOutput.set("INVALID INPUT! NUMBER MUST BE LESS THAN EQUAL TO 75!")
        else:
            answer = int(calcGCD(intN,intR))
            objOutput.set("Your GCD of the two integers is: " + str(answer))
    else:
        objOutput.set("INVALID INPUT! ENTER TWO POSTIVE INTEGERS!")


def calcLCM(integerM, integerN):

    if integerN == 0 or integerM == 0:
        leastCommonMultiple = "undefined"
    else: 
        leastCommonMultiple = integerM * integerN / calcGCD (integerM, integerN)
        leastCommonMultiple = int(leastCommonMultiple)

    return leastCommonMultiple

def lcmButtonClicked():
    strN = objN.get()
    strR = objR.get()

    if strN.isdigit() and strR.isdigit():
        intN = int(strN)
        intR = int(strR)

        if (intN > 75) or (intR > 75):
            objOutput.set("INVALID INPUT! NUMBER MUST BE LESS THAN EQUAL TO 75!")
        else:
            answer = int(calcLCM(intN,intR))
            objOutput.set("Your LCM of the two integers is: " + str(answer))
    else:
        objOutput.set("INVALID INPUT! ENTER TWO POSTIVE INTEGERS!")

def isRelativelyPrime(integerM, integerN):
    isPrime = False

    if calcGCD(integerM, integerN) == 1:
        isPrime = True
    return isPrime

def primeButtonClicked():
    strN = objN.get()
    strR = objR.get()

    if strN.isdigit() and strR.isdigit():
        intN = int(strN)
        intR = int(strR)

        if (intN > 75) or (intR > 75):
            objOutput.set("INVALID INPUT! NUMBER MUST BE LESS THAN EQUAL TO 75!")
        else:
            answer = isRelativelyPrime(intN,intR)

            if answer == True:
                objOutput.set("Your two numbers are relatively prime!")
            else:
                objOutput.set("Your two numbers are not relatively prime!")

    else:
        objOutput.set("INVALID INPUT! ENTER TWO POSTIVE INTEGERS!")

def aboutClicked():
    messagebox.showinfo("About This Program", "Hey! This is a fun program that preforms a variety of basic number theory calculations for you!")

def howToUseClicked():
    messagebox.showinfo("How to Use the Program?", "Don't know how the program works? Don't worry, your in good hands! \n \n 1) Input two integers less than equal to 75 in the two text boxes. \n \n"\
                        "2) Click one of the buttons at the bottom to perform the calculation you like. Your answer will then be calculated and printed in the label below the buttons. \n \n To change"\
                        "the font and design of the output, you may choose from the options on the right side of the program. \n \nIf you would like to rate the program, you can do so in the bottom"\
                        "right corner of the window. Just drag the scale to choose a rating from 1 to 10 and then click the submit button. Hope you enjoy the program!")

def displayFancyText():

    if attr.get() == 0:
        a = "normal"
    elif attr.get() == 1:
        a = "bold"
    else:
        a = "italic"

    if fnt.get() == 0:
        message.config(font=("Times",15,a))
    elif fnt.get() == 1:
        message.config(font=("Arial",15,a))
    else:
        message.config(font = ("Comic Sans MS", 15,a))


def submitButtonClicked():
    feedback = widScaleFeedback.get()
    objFeedback.set("THANKS FOR YOUR FEEDBACK 😀")

#INTERFACE
        
widLabelTheory = Label(myWindow,text="Number Theory", font = ("Times New Roman", 20, "bold", "italic"), fg = "#191919", bg = "#009B77")
    
widLabelN = Label(myWindow,text="Enter Your Value for N:", fg = "#191919", bg = "#009B77")
widLabelR = Label(myWindow,text="Enter Your Value for R:", fg = "#191919", bg = "#009B77")

widEntryN = Entry(myWindow, width=15, textvariable=objN)
widEntryR = Entry(myWindow,width=15, textvariable=objR)

widCalcPerm = Button(myWindow, text="Calculate Permutation",command=lambda:permButtonClicked(), fg = "#009B77")
widCalcComb = Button(myWindow, text="Calculate Combination",command=lambda:combButtonClicked(), fg = "#009B77")
widCalcLCM = Button(myWindow, text="Calculate LCM",command=lambda:lcmButtonClicked(), fg = "#009B77")
widCalcGCD = Button(myWindow, text="Calculate GCD",command=lambda:gcdButtonClicked(), fg = "#009B77")
widCalcPrime = Button(myWindow, text="Calculate Relative Prime",command = lambda:primeButtonClicked(), fg = "#009B77")

widClear = Button(myWindow, text="Clear", width=15, command=lambda:clearButtonClicked(), fg = "#009B77")
widExit = Button(myWindow,text="Exit", width=15, command=lambda:myWindow.destroy(), fg = "#009B77")

widLabelOutput = Label(myWindow, textvariable = objOutput, fg = "#191919", bg = "#009B77")

menuBar = Menu(myWindow)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Clear", command=lambda:clearButtonClicked())
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command=lambda:myWindow.destroy())
menuBar.add_cascade(label="File", menu=fileMenu)
helpMenu = Menu(menuBar, tearoff = 0)
helpMenu.add_command(label="About", command=lambda:aboutClicked())
helpMenu.add_command(label="How to Use Program?", command=lambda:howToUseClicked())
menuBar.add_cascade(label="Help", menu=helpMenu)

fontGroup = LabelFrame(myWindow, text="Font", padx=15, pady=15, borderwidth = 3, fg = "#191919", bg = "#009B77")
attrGroup = LabelFrame(myWindow, text="Attribute", padx=15, pady=15, borderwidth = 3, fg = "#191919", bg = "#009B77")

message = widLabelOutput

buttonTNR = Radiobutton (fontGroup,text = "Times New Roman",command = lambda:displayFancyText(), variable = fnt, value = 0, fg = "#191919", bg = "#009B77")
buttonArial = Radiobutton (fontGroup,text = "Arial",command = lambda:displayFancyText(),variable = fnt, value = 1, fg = "#191919", bg = "#009B77")
buttonComic = Radiobutton (fontGroup,text = "Comic Sans MS",command = lambda:displayFancyText(),variable = fnt, value = 2, fg = "#191919", bg = "#009B77")
buttonPlain = Radiobutton (attrGroup, text = "Plain",command = lambda:displayFancyText(),variable = attr,value = 0, fg = "#191919", bg = "#009B77")
buttonBold = Radiobutton (attrGroup, text = "Bold",command = lambda:displayFancyText(),variable = attr,value = 1, fg = "#191919", bg = "#009B77")
buttonItalic = Radiobutton (attrGroup, text = "Italic",command = lambda:displayFancyText(),variable = attr,value = 2, fg = "#191919", bg = "#009B77")

widLabelFeedback = Label(myWindow, text = "WHAT WOULD YOU RATE THIS PROGRAM?", font = ("Times New Roman", 14, "bold", "italic"), fg = "#191919", bg = "#009B77")
widScaleFeedback = Scale(myWindow, from_=0, to=10, orient = HORIZONTAL, length=275, cursor="heart", fg = "#191919", bg = "#009B77")
widSubmit = Button(myWindow, text="Submit", command=lambda:submitButtonClicked(), fg = "#009B77")
widLabelFeedbackOutput = Label(myWindow, textvariable = objFeedback, font = ("Times New Roman", 12, "bold"), fg = "#191919", bg = "#009B77")

widLabelTheory.grid(row=1,column=1, columnspan=2)

widLabelN.grid(row=2,column=1)
widEntryN.grid(row=2, column=2)

widLabelR.grid(row=3, column=1)
widEntryR.grid(row=3, column=2)

widCalcPerm.grid(row=4, column=1)
widCalcComb.grid(row=4,column=2)
widCalcLCM.grid(row=5,column=1)
widCalcGCD.grid (row=5, column=2)
widCalcPrime.grid(row=6, column=1, columnspan=2)

widClear.grid(row=7, column=1)
widExit.grid(row=7, column=2)
widLabelOutput.grid(row=8, column=1, columnspan=2)

myWindow.config(menu=menuBar)

fontGroup.grid(row=1, column=3, rowspan=4)
attrGroup.grid(row=1, column=4, rowspan=4)

buttonTNR.grid(row=0, sticky=W)
buttonArial.grid(row=1, sticky=W)
buttonComic.grid(row=2, sticky=W)
buttonPlain.grid(row=0, sticky=W)
buttonBold.grid(row=1, sticky=W)
buttonItalic.grid(row=2, sticky=W)

widLabelFeedback.grid(row=5, column=3, columnspan=2)
widScaleFeedback.grid(row=6, column=3, columnspan=2)
widSubmit.grid(row=7, column=3, columnspan=2)
widLabelFeedbackOutput.grid(row=8, column=3, columnspan=2)

mainloop() 
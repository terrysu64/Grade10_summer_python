#Name: Terry Su
#Date: August 10, 2020
#Purpose: GUI Canvas and Shapes from ICS3U course notes

#Description: This widget is used to draw shapes, such as lines and polygons in your application

#Import

from tkinter import*

#Canvas interface program and shapes

c = Canvas(None, width = 400, height = 200)
c.pack()

c.config(background = 'peach puff') #widgets can be given colours

c.create_line(0,100,400,100,fill = 'red') #horizontal line
#the cartesian plane on a computer interface has the origin located in the top left corner usually

for i in range(1,4):
    c.create_line(100*i, 0, 100*i, 400, fill = 'RoyalBlue1') #3 vertical lines

c.create_arc(20,20,80,80,start = 45, extent = 270, outline = 'black', fill = 'white', style = PIESLICE)
#the arc can have many different styles
#Note: (20,20,80,80) = (x1,y1,x2,y2,x3,y3......)
#Extent: width of PIESLICE arc in degrees
#The slice starts at the angle given by the start option and extends counterclockwise for extent degrees.

c.create_arc(120,20,180,80,start = 45, extent = 90, outline = 'black', width = 3.5 , style = CHORD)
#CHORD is a different type of arc

c.create_arc(220,20,280,80,start = 315, extent = -90, outline = 'blue', width = 2.0, style = ARC)
#ARC is just an arc

c.create_text(320,70,anchor = SW , text = 'Arcs', font = ('Arial', 24, 'bold'))
#text can be created on canvas

c.create_rectangle(20,120,80,180, width = 1.5, outline = 'blue', fill = 'red')

c.create_oval(120,120,180,180,width = 1.5,outline = 'black', fill = '')

c.create_polygon(230,120,270,120,290,150,270,180,230,180,210,150,width = 5, outline = 'purple')

c.create_oval(320,120,380,180,width = 1.5,outline = 'blue', fill = 'green')
#other shapes that can be generated on a canvas include: rectangles, ovals, and a custom polygon given several pairs of coordinates

mainloop()


#In addition to creating all manner of things like lines, polygons, ect, if you assign them to a variable it makes modifying easier
# i = create_line(20,20,400,20,fill = 'blue')
# c.coords( i , x,y.....)
# c.itemconfig( i, fill = 'green')
# c.delete(i)
# c.delete(ALL)

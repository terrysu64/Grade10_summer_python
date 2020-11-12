#Name: Terry Su
#Date: August 10, 2020
#Purpose: GUI Loading Bar(Canvas and Shapes) from ICS3U course notes

#Description: In game loading bar created using the tkinter canvas.

#Import

from tkinter import*
import time

#Initialize

root = Tk()
root.title('Loading Screen')

percentage = StringVar()
percentage.set(value = '0.0%')

#Interface Program

Label(root, textvariable = percentage, font = 'bold').pack()

main = Canvas(root, width = 410, height = 60)
main.pack()
main.config(background = 'white')

main.create_rectangle(5,5,405,55,width = 2.0, outline = 'black', fill = '')

bar = main.create_rectangle(10,10,10,50,width = 0,fill = 'green')

for x in range(10,410):
    main.coords(bar,10,10,x,50)
    percentage.set(str(100 / 400 * (x-9)) + '%') 
    main.update()
    time.sleep(0.1)

main.delete(ALL)
main.create_text(205,30,anchor = CENTER, text = 'COMPLETED!!!', font = ('Arial', 20, 'bold'))

mainloop()

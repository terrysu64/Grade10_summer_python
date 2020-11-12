#Name: Terry Su
#Date: July 7, 2020
#Purpose: Full speed python chapter 8 (classes)

#NOTES

#Object Oriented Programming(OOP) refers to a type of computer programming that revolves more around using and organizing data
#instead of procedure programming that purely uses algorithms to solve problems

#A class is a template for creating objects with related data/fields and functions thatcan organize that data

#A class can be created using the keyword 'class', the class name, and a colon
print('Class example')
class User:
    pass #pass is a line that does nothing, when defining a class we need 1 line minimum

User1 = User() #adds User1(object/instance) to User(class)
User1.first_name = 'Terry'
User1.last_name = 'Su'
User1.age = 15
#variables containing data attached to an object are called fields

print(User1.first_name, User1.last_name, ',age:', User1.age)
#fields should be lowercase and seperated with underscores with readability

first_name = 'Morgan'
last_name = 'Su'
age = 7.5
print(first_name, last_name, ',age:', age)
#these are different pieces of information than the previous fields because they are not attached to an object

#This data could have been stored equally in a dictionary named User1
#However, classes also hold many additional features such as:
#Methods, initialization and help text

class User:
    """ This class will create a user and store both its name and age"""
    #this is a help text using (""" """) that will provide information about the class
    
    def __init__(user, name, age):
        """ some basic information about the user """
        #__init__  is a built in function that initiallizes a new user/object(user) along with additional arguments(name, age)
        #the arguments will be stored as fields inside an object
        user.name = name
        user.age = age
        user.first_name = name.split(' ')[0]
        user.last_name = name.split(' ')[1]

    def hello(user):
        print('hello', user.name, '!!!')
        return ''
help(User)
Terry = User('Terry Su', 15)
Morgan = User('Morgan Su', 7.5)
print(Terry.name, Terry.first_name, Terry.age)
print(Morgan.name, Morgan.last_name, Morgan.age)
print(Terry.hello())
print()

#A class inheritance is a sub class that inherits all propreties, methods, objects and fields of a previous class
class ibm:
    """entering new workers into the system"""
    def __init__(worker, full_name, age):
        worker.full_name = full_name
        worker.age = age

    def greeting(worker):
        return print('Hello', worker.full_name,'!')
    

Zhongmin = ibm('Zhongmin Su', 44)
print(Zhongmin.greeting())
print()

class manager(ibm):
    #the manager class inhertied everything from the worker class
    """for managers to see more information about the worker"""
    def __init__(worker, full_name, age, employees=None):
        super().__init__(full_name, age)
        if employees is None:
            worker.employees = []
        else:
            worker.employees = employees
        password = input('what is the password : ')
        if password == 'oof':
             print('Hello', worker.full_name,'! Your employees of the day are', end=' ')
             for x in employees:
                print(x)
        else:
            return None

Guru = manager('the guru', 354, ['gavin ye', 'groose', 'morgan oof'])
print()
    
#QUESTIONS

#Exercises with classes
print('Class exercises')
print('Q1, Q2, Q3, Q4 done')
class Rectangle:
    """this is a class that can store coordinates of a rectangle and also calculate the width/height and area using functions"""
    print('enter diagonal coordinates')
    def __init__(rectangle, x1, y1, x2, y2):
        rectangle.x1 = x1
        rectangle.x2 = x2
        rectangle.y1 = y1
        rectangle.y2 = y2

    def width(rectangle):
        """this calculates the width"""
        if rectangle.x2 - rectangle.x1  == 0:
            print('it is not possible to have a width of 0', end ='')
        elif rectangle.x2 - rectangle.x1 > 0:
            print(rectangle.x2 - rectangle.x1, end ='')
        elif rectangle.x2 - rectangle.x1 < 0:
            print(rectangle.x1 - rectangle.x2, end = '')
        return ''
    
    def height(rectangle):
        """this calculates the height"""
        if rectangle.y2 - rectangle.y1  == 0:
            print('it is not possible to have a height of 0', end = '')
        elif rectangle.y2 - rectangle.y1 > 0:
            print(rectangle.y2 - rectangle.y1, end = '')
        elif rectangle.y2 - rectangle.y1 < 0:
            print(rectangle.y1 - rectangle.y2, end = '')
        return ''

    def area(rectangle):
        """calculates the area"""
        return (rectangle.y2 - rectangle.y1) * (rectangle.x2 - rectangle.x1)

help(Rectangle)
rectangle1 = Rectangle(1,0,3,4)
print((rectangle1.x1, rectangle1.y1), (rectangle1.x2, rectangle1.y2))
print(rectangle1.width())
print(rectangle1.height())
print(rectangle1.area())
print()

#Exercises with class inheritance
print('Class inheritance exercises')
print('Q1, Q2, Q3 done')

class square(Rectangle):

    def __init__(rectangle, x1, y1,x2,y2, size):
        super().__init__(x1,y1,x2,y2)
        rectangle.size = size
    
square1 = square(1,2,3,4,5)
print(square1.size)
print(square1.area())
    



    
    




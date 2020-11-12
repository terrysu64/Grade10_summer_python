#Name: Terry Su
#Date: June 24, 2020
#Purpose: Full speed python chapter 5 (functions and modules)

#NOTES

#A function is a block of code that is defined and then used to preform a single action.
#They are sequences of instructions that are executed when the function is called upon.
print('Function example')
def PrintFunction():
    print('This function prints this message here')
PrintFunction()
print()

print('Heres another example of a function')
def AddFunction():
    x = 1
    while x <= 3:
        print(x)
        x = x + 1
AddFunction()
print()

#function can be also used like actual f(x) functions in math
#there are one or more arguments/inputs to 'return' and output
print('Function with arguments')
def InputFunction(x):
    return ('the answer is', x*3 + 4)
    #basically f(x) = 3x + 4
print(InputFunction(3))
print()

print('Example with 2 arguments')
def InputFunction2(x,y):
    return x + y
add = 'the sum is', InputFunction2(4,45)
print(add)
print()

#There are also recursive functions
#A recursive function is a function that can call itself
#It breaks a problem down into smaller problems and calls itself repeatdly without looping
#there is always a base case and a recursive case that will eventually loop until it is the base base
print('Factorial recursive function')
def Factorial(x):
    if x == 0:
        return 1
    #base case
    else:
        return x * Factorial(x-1)
    #recursive case
#ex: 5! = 5 * 4 * 3 * 2 * 1
# = 5 * 4!
# 4! = 4 * 3 * 2 * 1
#  = 4 * 3!
#...
print(Factorial(6))
print()

#A module is an external python file that needs to be imported.
#It may contain variables, functions and much more.
print('A common module is the math module')
import math
print('cosine of 90 degrees')
print(math.cos(90))
print('square root of 16')
print(math.sqrt(16))
print()

print('Another module is the random module')
print('generates random float')
import random
print(random.random())
print('generates random integer between 0-20')
print(random.randint(0,21))
print()

#QUESTIONS

#Exercises with functions
print('Functions exercises')
#Q1
print('Q1')
def add3(a,b,c):
    return 'the sum of the 3 values is', a + b + c
print(add3(2,3,4))
print()

#Q2
print('Q2')
def Compare(x,y):
    if x > y:
        return 'the first number is larger'
    elif x == y:
        return 'the numbers are the same'
    else:
        return 'the second number is larger'
print(Compare(3,5))
print(Compare(2.1,2.0))
print(Compare(4,4))
print()

#Q3
print('Q3')
def IsDivisible(q,w):
    if q % w == 0:
        return 'the first number is divisible by the second'
    else:
        return 'the first number is not divisible by the second'
print(IsDivisible(4,2))
print(IsDivisible(5,3))
print()

#Q4
print('Q4')
def Average(List):
    return 'the average of the list is', sum(List) / len(List)
Number = [x for x in range(1,11)]
print(Average(Number))
print()

#Exercises with recursive functions
print('Recusive function exercises')
#Q1
print('Q1')
#already done in factorial recursive function example
print()

#Q2
print('Q2')
def ContinueAdd(x):
    if x == 0:
        return 0
    #base case
    else:
        return x + ContinueAdd(x-1)
    #recursive case
print(ContinueAdd(11))
print()

#Exercises with math module
print('Math module exercises')

#Q1
print('Q1')
import math
print(math.gcd(15,21),',', math.gcd(152,200), ',', math.gcd(1988,9765))
print()

#Q2
print('Q2')
print(math.degrees(2 * 3.14159))
print()

#Q3
print('Q3')
def Trig(x):
    return 'the trigonometric ratios of the value are', math.sin(x),math.cos(x),math.tan(x)
print(Trig(222))
print()










        


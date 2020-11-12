#Name: Terry Su
#Date: July 14, 2020
#Purpose: Full speed python chapter 10 (Generators)

#NOTES

#A python generator is a loop/iteration. It is a concise way of implementing an iterator.
#It uses the key word 'yield' allowing it to iterate over elements

#Example
print('Generator example')
#A generator function is defined like a normal function, but with the 'yield' keyword rather than 'return'.
def Range(x,y):
    while x <= y:
        yield x*x
        x += 1
        #yield is used when we want to iterate over a sequence but don't want to store the entire sequence in memory
        #it only runs when called 

Range1 = Range(2,10)
print(Range1)
#Generators behave like iterators, they return one element at a time manually
print(next(Range1))
print(next(Range1))
print(next(Range1))
print(next(Range1))
print(next(Range1))
print(next(Range1))
print()

#however a for loop may also be used on them
Range2 = Range(1,10)
List = []
for element in Range2:
    List.append(element)
print(List)
print()

#QUESTIONS
print('Iterator exercises')

#Q1
print('Q1')
def squares(x,y):
    while x <= y:
        yield x*x
        x += 1

square_range = squares(1,12)
List1 = []
for square in square_range:
    List1.append(square)
print(List1)
print()

#Q2
print('Q2')
def even(x,y):
    if x % 2 != 0:
        x += 1
    while x <= y:
        yield x
        x += 2
even1 = even(1,20)
for number in even1:
    print(number)
print()

#Q3
print('Q3')
def odd(x,y):
    if x % 2 == 0:
        x += 1
    while x <= y:
        yield x
        x += 2
odd1 = odd(1,20)
for number in odd1:
    print(number)
print()

#Q4
print('Q4')
def down(n):
    while n >= 0:
        yield n
        n -= 1
down1 = down(10)
for number in down1:
    print(number)
print()

#Q5
print('Q5')
import math
def fib(x):
    count = 3
    if x == 1:
        print(1)
    elif x == 2:
        print(1)
        print(1)
    else:
        print(1)
        print(1)
        while count <= x:
            yield int((1 / math.sqrt(5)) * ((1 + math.sqrt(5) ) / 2) ** (count + 1) - ((1 / math.sqrt(5)) * ((1 - math.sqrt(5)) / 2) ** (count + 1)))
            count += 1
fib1 = fib(9)
for element in fib1:
    print(element)
print()

#Q6
print('Q6')
def co(x):
    count = 0
    while count <= x:
        yield (count, count + 1)
        count += 1
co1 = co(10)
for coordinates in co1:
    print(coordinates)
    

            

        
        



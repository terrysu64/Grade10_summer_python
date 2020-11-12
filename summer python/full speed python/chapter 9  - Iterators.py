#Name: Terry Su
#Date: July 10, 2020
#Purpose: Full speed python chapter 9 (Iterators)

#NOTES

#An iterable is is anything capable of returning elements one at a time such as a list
#it can be iterated with a while loop, for loop and also an iterator
#An iterator is a for loop that returns elements one at a time manually by using the next() function

List = [1,3,5,76,2,4,56]
#the elements can be iterated with a for loop
print('Iterating using for loop')
for x in List:
    print(x, end=',')
print()
print()

IterList = iter(List)
#or an iterator stored in a variable
print('Iterating using manual iterator')
print(IterList)
print(next(IterList))
print(next(IterList))
print(next(IterList))
print(next(IterList))
print(next(IterList))
print()
#if there are no more elements there will be an error of StopIteration

#This is what an iterator is doing behind the scenes
List1 = [1,3,5,76,2,4,56]
IterList1 = iter(List1)
while True:
    try:
        Element = next(IterList1)
        print(Element)
    except StopIteration:
        break #break at StopIteration also prevents an error from occuring
print()
#Iterators can also be implemented as classes by using the __iter__ and __next__ functions
print('Iterator classes example')
class my_range:
    def __init__(userrange, x , y):
        userrange.x = x
        userrange.y = y

    def __iter__(userrange):
        #__iter__.usserange() is just another way of saying iter(userrange)
        return userrange

    def __next__(userrange):
        if userrange.x < userrange.y:
            value = userrange.x
            userrange.x += 1
            #userrange.x = userrange.x + 1
            return value
        else:
            raise StopIteration

Range = my_range(1,4)
print(Range.__next__())
#Range.__next__() is another way of saying next(Range)
print(Range.__next__())
print(Range.__next__())
print()
#however a for loop is much simpler

#QUESTIONS
print('Questions')
print('Q1')
class square:
    def __init__(Range, x , y):
        Range.x = x
        Range.y = y

    def __iter__(Range):
        return Range

    def __next__(Range):
        if Range.x <= Range.y:
            value = Range.x
            Range.x = Range.x + 1
            return value**2
        else:
            raise StopIteration

Range1 = square(1,10)
print(Range1.__next__())
print(Range1.__next__())
print(Range1.__next__())
print(Range1.__next__())
print(Range1.__next__())
print(Range1.__next__())
print(Range1.__next__())
print(Range1.__next__())
print()

print('Q2')
class even:
    def __init__(number, n):
        number.max = n
        number.count = 2

    def __iter__(number):
        return number

    def __next__(number):
        if number.count < number.max:
            value = number.count
            number.count += 2
            return value
        else:
            raise StopIteration
            
Even1 = even(13)
print(Even1.__next__())
print(Even1.__next__())
print(Even1.__next__())
print(Even1.__next__())
print(Even1.__next__())
print()

print('Q3')
class odd:
    def __init__(number, n):
        number.max = n
        number.count = 1

    def __iter__(number):
        return number

    def __next__(number):
        if number.count < number.max:
            value = number.count
            number.count += 2
            return value
        else:
            raise StopIteration
            
odd1 = odd(13)
print(odd1.__next__())
print(odd1.__next__())
print(odd1.__next__())
print(odd1.__next__())
print(odd1.__next__())
print()

print('Q4')
class reverse:
    def __init__(number1, x):
        number1.down = x

    def __iter__(number1):
        return number1

    def __next__(number1):
        if number1.down >= 0:
            value = number1.down
            number1.down = number1.down - 1
            return value
        else:
            raise StopIteration
reverse1 = reverse(12)
print(reverse1.__next__())
print(reverse1.__next__())
print(reverse1.__next__())
print()

print('Q5')
import math
class fib:
    def __init__(Range2, n):
        Range2.len = n
        Range2.Count = 0

    def __iter__(Range2):
        return Range2

    def __next__(Range2):
        if Range2.Count == 0 or Range2.Count == 1:
            value = Range2.Count
            Range2.Count += 1
            return 1
        elif Range2.Count > 1 and Range2.Count <= Range2.len:
            value = Range2.Count
            Range2.Count += 1
            return int((1 / math.sqrt(5)) * ((1 + math.sqrt(5) ) / 2) ** (value + 1) - ((1 / math.sqrt(5)) * ((1 - math.sqrt(5)) / 2) ** (value + 1)))
        else:
            raise StopIteration
fibo = fib(8)
print(fibo.__next__())
print(fibo.__next__())
print(fibo.__next__())
print(fibo.__next__())
print(fibo.__next__())
print(fibo.__next__())
print(fibo.__next__())
print(fibo.__next__())
print()

print('Q6')
class Tuple:
    def __init__(coordi, f):
        coordi.stop = f
        coordi.count = 0

    def __iter__(coordi):
        return coordi

    def __next__(coordi):
        if coordi.count <= coordi.stop:
            value = coordi.count
            coordi.count += 1
            return value, value + 1
        else:
            raise StopIteration
        
Range3 = Tuple(8)
print(Range3.__next__())
print(Range3.__next__())
print(Range3.__next__())
print(Range3.__next__())
print(Range3.__next__())
print(Range3.__next__())
print(Range3.__next__())
        



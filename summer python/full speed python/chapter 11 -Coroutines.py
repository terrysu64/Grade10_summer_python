#Name: Terry Su
#Date: July 15, 2020
#Purpose: Full speed python chapter 11 (Coroutines)

#NOTES

#Python coroutines are similar to generators, but instead of producing data they consume data.
#They are functions that are resumed everytime a value is sent using 'send()'

print('Coroutine example')
def coroutine():
    print('my coroutine')
    print('input a number')
    while True:
        num = yield #the yield expression pauses the program until a value is sent to it
        print('your number sire is', num)

co = coroutine()
next(co) #'next' is required to move the coroutine forward.
         #eventually the coroutine reaches the yield expression where it waits to receive input and resume
co.send(1)
co.send(6)
co.send(4)
co.close() #coroutines can be closed with the close() method
           #any more inputs will be denied with a StopIteration error
print()

#Pipelines are a series a coroutines where data is pushed down the line of corutines
#this uses the 'send()' method once again

print('Coroutine pipeline example')
def producer(consumer):
    print('Producer ready')
    while True:
        val = yield
        consumer.send(val**2)

def consumer():
    print('Consumer ready')
    while True:
        val = yield
        print('Consumer got', val)

consumer1 = consumer()
next(consumer1)
consumer1.send(4)
print()

producer1 = producer(consumer1)
next(producer1)
producer1.send(4)
print()



#QUESTIONS
print('Coroutine exercises')

#Q1
print('Q1')
def square():
    print('enter a number and its square will be returned')
    while True:
        num1 = yield
        print(num1 ** 2)

square1 = square()
next(square1)
square1.send(2)
square1.send(9)
square1.send(10)
square1.close()
print()

#Q2
print('Q2')
def minimize():
    print('Smallest number will be kept')
    num2 = yield
    mini = num2
    print(mini)
    while True:
        num2 = yield
        if num2 < mini:
            mini = num2
            print(mini)
        else:
            print(mini)

minimum = minimize()
next(minimum)
minimum.send(100)
minimum.send(101)
minimum.send(90)
minimum.send(2)
minimum.send(40)
print()

#QUESTIONS
print('Pipeline exercises')

#Q1
print('Q1')
def producer(consumer1, consumer2):
    print('Producer ready')
    while True:
        val = yield
        consumer1.send(val*val)
        consumer2.send(val*val)

def consumer_max():
    print('Max consumer ready')
    values_max = []
    try:
        while True:
            val = yield
            values_max.append(val)
            print('maximum:',max(values_max))
    except GeneratorExit:
        print('Generator is closed')

def consumer_min():
    print('Min consumer ready')
    values_min = []
    try:
        while True:
            val2 = yield
            values_min.append(val2)
            print('minimum:',min(values_min))
    except GeneratorExit:
        print('Generator is closed')

cons_max = consumer_max()
cons_min = consumer_min()
producer1 = producer(cons_max, cons_min)
next(cons_max)
next(cons_min)
next(producer1)
print()
producer1.send(4)
print()
producer1.send(2)
print()
producer1.send(34)
print()
producer1.send(22)
print()
cons_max.close()
cons_min.close()
print()

#Q2
print('Q2')
def producer(consumer1, consumer2):
    print('Producer ready')
    count = 0
    try:
        while True:
            val = yield
            if count % 2 == 0:
                try:
                    consumer1.send(val)
                except GeneratorExit(consumer1):
                    print('consumer1 is closed')
            else:
                try:
                    consumer2.send(val)
                except GeneratorExit(consumer2):
                    print('consumer2 is closed')
            count += 1
    except GeneratorExit:
        print('Producer closed')

def consumer():
    print('Consumer ready')
    values = []
    try:
        while True:
            num = yield
            values.append(num)
    except GeneratorExit:
        print(values)
        print('consumer closed')

consumer1 = consumer()
consumer2 = consumer()
producer2 = producer(consumer1, consumer2)
next(consumer1)
next(consumer2)
next(producer2)
print()

producer2.send(32)
producer2.send(43)
producer2.send(752)
producer2.send(7)
producer2.send(562)
producer2.send(4)
producer2.send(45)
producer2.send(34)
consumer1.close()
consumer2.close()


        

    
        

#Name: Terry Su
#Date: June 26, 2020
#Purpose: Full speed python chapter 6 (loops or iterations)

#NOTES

#There are two different type of loops. The first on is called the 'for' loop
#it allows you to iterate over all items of a given 'list' and allows you to do whatever with each element of the list
#unlike the VB for loop. The python for loop is not exactly a counter but is very similar and powerful.
print('For loop structure and example')
for value in [1,2,3,4]:
    print(value * 2)
#the for loop goes through every 'value' of the list one by one to repetedly print the desired output
for value2 in range(10):
    print(value)
#the range() is also a list
print()

print('Sum of a list using for loop example')
Sum = 0
for x in [y for y in range(1,11)]:
    Sum = x + Sum
print(Sum)
print()

print('Matching list index and value using for loop example')
List = [3,5,6,2,4,6,3]
for i in range(len(List)):
    print('Index: ', i, ', Value: ', List[i])
print()
    
#Another way of doing the same thing is by using the enumerate function
print(type(enumerate(List)))
print(list(enumerate(List)))
for Index,Value in enumerate(List):
     print('Index: ', Index, ', Value: ', Value)
print()

#The second type of looping in python is called the 'while' loop
#It allows you to execute code over and over again given a condition
#the condition usually includes numbers and relational operators to count
print('While loop example')
Counter = 0
StrCounter = ""
while Counter <= 10:
    StrCounter = StrCounter + ',' + str(Counter)
    Counter = Counter + 1
print(StrCounter)

#another way to print on the same line is by adding a end = ' ' at the end of a print statement
Counter = 0
while Counter <= 10:
    print(Counter, end=',')
    Counter = Counter + 1
print()
print()

#QUESTIONS

#For loop exercises
print('For loop exercises')
print()

#Q1
print('Q1')
def Add(x):
    Sum = 0
    for Element in x:
        Sum = Element + Sum
    return Sum
print(Add((list(range(11)))))
print()

#Q2
print('Q2')
def Max(List):
    MaxVal = List[0]
    for x in List:
        if MaxVal <= x:
            MaxVal = x
    return MaxVal
print(Max([f for f in range(25) if f % 2 != 0]))
print()

#Q3
print('Q3')
def Max2(List2):
    MaxVal2 = List2[0]
    Index = 0 
    for q in range(len(List2)):
        if MaxVal2 <= List2[q]:
            MaxVal2 = List2[q]
            Index = q
    return Index, MaxVal2
print(Max2([3,43,45,55,4,55,345,5,5]))
print()
#this can also be done with the built in max function

#Q4
print('Q4')
def Reversed(List3):
    List3.reverse()
    return List3
#the reverse function modifies the original list
print(Reversed([1,2,3,4,5,6]))
print()

#Q5
print('Q5')
def Sort(List4):
    List4.sort()
    return List4
print(Sort([1,4,7,3,3,5]))
print()

#Q6
print('Q6')
def Sort(List4):
    List4.sort(reverse=True)
    return List4
print(Sort([1,4,7,3,3,5]))
print()

#While loop exercises
print('While loop exercises')
print()

#Q1
print('Q1')
def even_odd(x):
    Counter = 0
    while Counter < x:
        print(x - Counter, end=',')
        if (x - Counter) % 2 == 0:
            print('even number')
        else:
            print('odd number')
        Counter = Counter + 1
    return ''   
print(even_odd(10))
print()

        



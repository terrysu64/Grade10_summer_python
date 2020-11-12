#Name: Terry Su
#Date: July 1, 2020
#Purpose: Practice questions for lists 

#1. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
print('Q1 done')
List1 = [0,1,2,3,4,5,6,7,8,9,10]
for Index in [5, 4, 0]:
    List1.remove(List1[Index])
print(List1)
print()

#2. Write a Python program to print the numbers of a specified list after removing even numbers from it
print('Q2 done')
List1 = [0,1,2,3,4,5,6,7,8,9,10]
for Number in List1:
    if Number % 2 == 0:
        List1.remove(Number)
print(List1)
print()

#3. Write a Python program to get the difference between the two lists
print('Q3 done')
List1 = ['a','b','c','d','e','f','g']
List2 = ['a', 'c', 'f']
List3 = []
for Element in List1:
    if Element not in List2:
        List3.append(Element)
print(List3)
print()

#4. Write a program to convert a comma separated string into a list.
#Sample String: "hello,world,this,world"
#Expected Output: [Hello, world, this, world]
print('Q4 not done')
String1 = 'hello,world,this,world'
Comma = 0
List1 = []
while Comma != - 1:
    Comma = int(String1.find(','))
    List1.append(String1[0:(Comma)])
    String1 = String1.replace(String1[0:Comma + 1], '' ,1)
print(List1)
print()

#5. Write a Python program to convert a list of characters into a string
#Sample list: [a, b, c, d]
#Expected Output: "abcd"
print('Q5 done')
List = ['a','b','c','d']
for x in List:
    print(x,end='')
print()
print()

#6. Write a Python program to append a list to the second list
#Sample list one: [1, 2, 3, 4]
#Sample list two: [5, 6, 7, 8]
#Expected Output: [1, 2, 3, 4, 5, 6, 7, 8]
print('Q6 done')
List1 = [1,2,3,4,5]
List2 = [6,7,8]
for x in List2:
    List1.append(x)
print(List1)
print()

#7. Write a Python program to create a list of sublists
#Sample list one: [1, 2, 3, 4]
#Sample list two: [5, 6, 7, 8]
#Expected Output: [ [1, 2, 3, 4], [5, 6, 7, 8] ]
print('Q7 done')
List1 = ['a','b','c']
List2 = ['e','f','g']
print([List1, List2])
print()

#8. Make a list that takes out a random number out of 100 and finds it
print('Q8')
import random
List1 = [x for x in range(101)]
print(List1)
x = random.randint(0,101)
List2 = [y for y in range(101) if y != x]
print(List2)
for element in List1:
    if element not in List2:
        print('the missing number is', element)




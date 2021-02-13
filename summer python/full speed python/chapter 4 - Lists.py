#Name: Terry Su
#Date: June 23, 2020
#Purpose: Full speed python chapter 4 (lists)

#NOTES

#Python lists are data structures that group sequences of elements.
#They are arrays (hold multiple elements at once)
#You can mix different datatypes/elements in a list although they are usually the same.

#lists are formed using square brackets and are defined under a variable
print('List example')
List1 = ['apple', 'banana', 'orangutan', 'oof', 'terry', 'dsf']
print(type(List1))
print(List1)
print()

#The specific elements of a list can also be acessed by their positions where 0 is the index of the first element
print('Acessing specific elements of a list')
print(List1[0])
print(List1[1])
print()

#Portions of the list/sublists can also be acessed by 'slicing', and using a start and end index
print('Acessing specific elements of a list using start/end indexes')
print(List1[0:3])
print()

#Arithmetic operations with lists are also possible
print('Arithmetic operations with lists')
print(List1 * 3)
print(List1 + ['hi', 'bye'])
print()

#A concise way to create lists is by creating a 'List Comprehension'
#An expression and optional conditions are given within square brackets by using a few key words
#'for', 'in', and 'if'
print('List comprehensions using for loops, ranges, and conditions')
print([x for x in range(11)])
print([y*2 for y in range(11) if y % 2 == 1])
print()

#a range can also be converted in to a list
print('Range converted into a list')
print(list(range(20)))
print()

#a way of acessing both index and value of a list at once is to use enumerate()
print('Enumerater function')
for i,v in enumerate(List1):
    print(i,v)
print('\n')

#QUESTIONS

#Exercises with lists
print('Exercises with lists')
L = [1,4,9,10,23]
#Q1
print('Q1')
print(L[1:3])
print(L[3:5])
print()

#Q2
print('Q2')
print(L + [90])
print()

#Q3
print('Q3')
AverageL = sum(L) / len(L)
print(AverageL)
print()

#Q4
print('Q4')
print(L[0:1] + L[3:5])
print()

#list comprehension exercises
print('Exercises with list comprehensions')
#Q1
print('Q1')
print([x*x for x in range(1,11)])
print()

#Q2
print('Q2')
print([x*x*x for x in range(1,11)])
print()

#Q3
print('Q3')
print([x for x in range(1,21,2)])
print([x for x in range(2,21,2)])
print()

#Q4 (textbook answer wrong)
print('Q4')
print(sum([x*x for x in range(21) if x % 2 == 0]))
print()

#Q5 (textbook answer wrong too)
print('Q5')
print([x*x for x in range(0,21,2) if x % 3 != 0]) 





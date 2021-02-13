
#Name: Terry Su
#Date: June 22, 2020
#Purpose: Full speed python chapter 3 (strings and numbers)

#NOTES

#There are many data types in python, the most baisic are integers, floats, strings, booleans

#integers are whole numbers
print('Integers')
a = 2
print(type(a))
print()

#floats are real numbers with decimals
print('Floats')
b = 2.5
print(type(b))
print()

#strings are letters or words
print('Strings')
c = "dffdsfsdv"
print(type(c))
print()

#booleans are either True or False (extra)
#values besides 0 and '' are considered True by default
print('Booleans')
d = True
print(type(d))
print()

#numbers can be used to preform mathematical operations
print('Arithmetic operations with datatypes')
print('addition', a + b)
print('multiplication', a*b)
print('exponents', a**b)
print()

#data types can also be interchanged for example:
print('exponents', int(a**b))
print('exponents', str(a**b))
print()

#However strings and number data types cannot be mixed or else there will be a logic error
#ex : (3 + 'hi') does not work

#Multiplication is an exception however.
print(c*5)
print()

#string[start:end:step] (index)
#examples:
print(x[1:4:2])
print(x[1:]) #from index 1 till very end
print(x[1:-1]) #from index 1 till very end -1 index

#btw slicing also works with lists

#QUESTIONS

#Exercises with numbers
print('Exercises with numbers')
#Q1
print('Q1')
Average = (12 + (14/6) + 15) / 3
print(Average)
print()

#Q2
print('Q2')
Pi = 3.1415
Volume = (5**2 * Pi) * 4/3
print(Volume)
print()

#Q3
print('Q3')
print('1', 1 % 2)
print('5', 5 % 2)
print('20', 20 % 2)
print()

#Q4
print('Q4')
x = 0
y = 2
print(x < 1/3 < y)
print()

#Exercise with strings
print('Exercises with strings')
#Q1
print('Q1')
s = 'abc'
print(len(s))
#To substring a string a format of string[start: end: step] is followed
print(s[0:1]*3 + s[1:2]*3 + s[2:3]*3)
print()

#Q2
print('Q2')
s = 'aaabbbccc'
#the find method is used to find the position of a substring in a string
print(s.find('b'))
print(s.find('ccc'))
#the replace method is used in the form of string.replace("orignial", "new", # of times)
print(s.replace('a', 'X'))
s = 'aaabbbccc'
print(s.replace('a', 'X', 1))
print()

#Q3
print('Q3')
s = 'aaa bbb ccc'
#the upper method turns an entire string into uppercase in the form of string.upper()
print(s.upper())
print(s.replace('aaa bbb ccc' , 'AAA bbb CCC'))


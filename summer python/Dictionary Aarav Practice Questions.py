#Name: Terry Su
#Date: July 2, 2020
#Purpose: Practice questions for dictionaries

#1. Write a Python script to sort (ascending and descending) a dictionary by value
print('Q1 done')
Dic1 = {1: 11, 2: 3, 3: 23, 4: 6, 5: 53, 6: 99}
print(Dic1)
print(sorted(Dic1.values()))
print()

#2. Write a Python script to add a key to a dictionary
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}
print('Q2 done')
D1 = {0: 10, 1: 20}
D1[2] = 30
print(D1)

#3. Write a Python script to concatenate following dictionaries to create a new one.
#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print('Q3 done')
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
print({**dic1, **dic2, **dic3})
print()

#4. Write a Python script to check whether a given key already exists in a dictionary
print('Q4 done')
D1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def CheckDic(x):
    if x in D1:
        print('your input is a key in this dictionary', end='')
    else:
        print('your input was not found in this dictionary', end='')
    return''
print(CheckDic(3))
print(CheckDic(10))
print()

#5. Write a Python program to iterate over dictionaries using for loops
print('Q5 done')
D1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for Key,Value in D1.items():
    print(Key,':',Value)
print()

#6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
#Sample Dictionary ( n = 5) :
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print('Q6 done')
n = 10
Dic1 = {}
for x in range(n + 1):
    Dic1[x] = x*x
print(Dic1)
print()

#7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
print('Q7 done')
n = 15
Dic1 =  {}
for x in range(1, n + 1):
    Dic1[x] = x*x
print(Dic1)
print()

#8. Write a Python script to merge two Python dictionaries
print('Q8 done')
Dic1 = {'one':1,'two':2}
Dic2 = {'three':3,'four':4}
for x in Dic2.keys():
    Dic1[x] = Dic2[x]
print(Dic1)
print()

#9. Write a Python program to remove a key from a dictionary
print('Q9 done')
Dic1 = {'one':1,'two':2}
print(Dic1)
del Dic1['two']
print(Dic1)
print()

#10. Write a Python program to sort a dictionary by key
print('Q10 not done')
print()

#11. Write a Python program to get the maximum and minimum value in a dictionary
print('Q11 done')
Dic1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(max(Dic1.values()))
print(min(Dic1.values()))
print()

#12. Write a Python program to check a dictionary is empty or not
print('Q12 done ')
Dic1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Dic2 = {}
if bool(Dic1) == False:
    print('your dictionary is empty')
else:
    print('your dictionary has at least one pair')
if bool(Dic2) == False:
    print('your dictionary is empty')
else:
    print('your dictionary has at least one pair')
print()

#13. Write a Python program to combine two dictionary adding values for common keys
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
print('Q13 done')
Dic1 = {'a': 100, 'a': 200, 'a':300, 'b':232,'f':123}
Dic2 = {'a': 300, 'b': 200, 'd':400}
Dic3 = {}
for Key in Dic1.keys():
    if Key in Dic2.keys():
        Dic2[Key] = Dic1[Key] + Dic2[Key]
        Dic3[Key] = Dic1[Key] + Dic2[Key]
    else:
        Dic3[Key] = Dic1[Key]
print(Dic3)
print()

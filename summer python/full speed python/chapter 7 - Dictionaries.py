#Name: Terry Su
#Date: June 30, 2020
#Purpose: Full speed python chapter 7 (dictionaries)

#NOTES

#a map or so called dictionary in python is a datatype in python
#It stores key-value pairs of data, an input(key) which is mapped to an output(value)

#Example
#Dictionaries use curly brackets, colons and commas to store and seperate data
print('Example of a dictionary storing ages of people')
Ages = {
    'Terry': 15,
    'Morgan': 12,
    'Oof': 101,
    'Prefect': 24,
    'Mop': 23123
    }
print(type(Ages))
print(Ages)
print()

#Dictionaries can have any datatype as key or value
DataDic = {
    3:'three',
    'fruits':['apple','bapple','anana'],
    'drip':3.132132
    }
print(DataDic)
print()

#Retreiving data or value from a dictionary is also the same as from a list
#Except the key is entered instead of the index
print('Retreiving a value from a dictionary')
List = [x*3 for x in range(10)]
print(List[2])
print('Terry is', Ages['Terry'], 'years old.')
print()

#If a key is not in the dictionary there will be an error
#here is a possible way to prevent it
print('Preventing dictionary error')
def CheckDic(x):
    if x in Ages:
        print(Ages[x], end='')
    else:
        print('your input was not found in this dictionary', end='')
    return''
print(CheckDic('Morgan'))
print(CheckDic('bruhhhh'))
print()

#You can also iterate over contents(key:value) of the dictionary by using 'items' function
print('Iteration over all contents of a dictionary')
for name,age in Ages.items():
    print(name, '=',age)
print()

#Sub-dictionaries can also be created by using a dictionary itself as a value

print('Sub-dictionary example')
Information = {
    'Morgan Su': {'school': 'swl', 'favorite game':'GD', 'face':'oof'},
    'Terry Su': {'school': 'mmhs', 'favorite game':'none', 'face':'bruh'},
    'Bob Su': {'school': 'idk', 'favorite game':'minecraft', 'face':'f'}
    }
for key,value in Information.items():
    print(key, ':', value)
print(Information['Terry Su'])
print()

#QUESTIONS

#Exercises with dictionaries
print('Exercises with dictionaries')

#Q1
print('Q1')
StudentAges = {
    'Peter' : 10,
    'Anna': 11,
    'Morgan': 13,
    'Gavin Ye': 18,
    'Barry Bee': 17,
    'Ananas': 14
    }
print('there are', len(StudentAges), 'students on the list')
print()

#Q2
print('Q2')
def Average(x):
    Sum = 0
    Count = 0
    for student,age in x.items():
        Sum = Sum + age
        Count = Count + 1
    print('the average age is', Sum // Count)
    return''
print(Average(StudentAges))
print()

#Q3
print('Q3')
def Max(x):
    print(max(x.values()))
    return''
print(Max(StudentAges))
print()

#Exercises with sub-dictionaries
print('Exercises with sub-dictionaries')

#Q1
print('Q1')
Information = {
    'Morgan Su': {'School': 'swl', 'Favorite game':'GD', 'Age':2},
    'Terry Su': {'School': 'mmhs', 'Favorite game':'none', 'Age':25},
    'Bob Su': {'School': 'idk', 'Favorite game':'minecraft', 'Age':44}
    }
print('there are', len(Information), 'students')
print()

#Q2
print('Q2')
def Average2(x):    
    Sum = 0
    Count = 0
    for Name in x:
        Sum = x[Name]['Age'] + Sum
        Count = Count + 1
    print(Sum // Count)
    return ''
print(Average2(Information))
print()

#Q3
print('Q3')
def School(x,School):
    for Name in x:
        for Element in x[Name]:
            if x[Name][Element] == School:
                print(School, Name)
    return''
print(School(Information, 'idk'))
print()



#Name: Terry Su
#Date: July 16, 2020
#Purpose: CCC 2020 junior questions

#Q1
print('Q1')
small = int(input('enter the number of SMALL treats Barley received: '))
while small < 0 or small >= 10:
    print('your input was not valid, try again.')
    small = int(input('enter the number of SMALL treats Barley received: '))
    
medium = int(input('enter the number of MEDIUM treats Barley received: '))
while medium < 0 or medium >= 10:
    print('your input was not valid, try again.')
    medium = int(input('enter the number of MEDIUM treats Barley received: '))
    
large = int(input('enter the number of LARGE treats Barley received: '))
while large < 0 or large >= 10:
    print('your input was not valid, try again.')
    large = int(input('enter the number of LARGE treats Barley received: '))

print()
total = small + (2 * medium) + (3 * large)
if total >= 10:
    print('happy')
else:
    print('sad')
print()

#Q2
print('Q2')
P = int(input('what is the total of infected people you want to calculate: '))
N = int(input('how many people have the disease currently: '))
R = int(input('how many others does each infected person infect daily: '))
day = 0
next_group = N
while N <= P:
    N += (next_group * R)
    next_group *= R
    day += 1
print(day)
print()

#Q4
print('Q3')
drop_number = int(input('how many drops of paint have been flicked: '))
count = 0
while count < drop_number:
    print(count)
    count += 1
    



    

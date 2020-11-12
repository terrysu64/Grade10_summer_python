#Name: Terry Su
#Date: August 19, 2020
#Purpose: CCC 2018 junior questions

#Q1
print('Q1')
phone1 = input('enter number 1: ')
phone2 = input('enter number 2: ')
phone3 = input('enter number 3: ')
phone4 = input('enter number 4: ')

if (phone1 == 8 or phone1 == 9) and (phone4 == 8 or phone4 == 9) and phone2 == phone3:
    print('ignore')
else:
    print('accept')
print()

#Q2
print('Q2')
N = int(input('How many parking spaces are there: '))
yesterday = input('Which ones were parked at yesterday: ')
today = input('Which ones were parked at today: ')

common = 0
count = 0
yesterdayL = []
todayL = []

for x in range(0, N):
    yesterdayL.append(yesterday[count:count + 1])
    todayL.append(today[count:count + 1])
    count += 1

for x in range(0,N):
    if yesterdayL[x] == todayL[x] and yesterdayL[x] == 'C':
        common += 1

print(common)
print()

#Q3
print('Q3')
city = input('Enter city distances: ')
copy = []
distance = []
num = ''
count = 0

for x in range(0,len(city)):
    copy.append(city[count:count + 1])
    count += 1

count = 0
for x in copy:
    if x == ' ':
        distance.append(num)
        num = ''
    else:
        num += x
distance.append(num)
print(distance)

d1 = int(distance[0])
d2 = int(distance[1])
d3 = int(distance[2])
d4 = int(distance[3])

print(0,d1,d1+d2,d1+d2+d3,d1+d2+d3+d4)
print(d1,0,d2,d2+d3,d2+d3+d4)
print(d1+d2,d2,0,d3,d3+d4)
print(d1+d2+d3,d2+d3,d3,0,d4)
print(d1+d2+d3+d4,d2+d3+d4,d3+d4,d4,0)

#Q4
print('Q4')


    
    




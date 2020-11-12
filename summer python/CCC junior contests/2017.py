#Name: Terry Su
#Date: August 26, 2020
#Purpose: CCC 2017 junior questions

#Q1
print('Q1')
x = int(input('enter x coordinate: '))
y = int(input('enter y coordinate: '))

if x == 0 and y == 0:
    print('orgin')
elif x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
print()

#Q2
print('Q2')
num = int(input('enter your number: '))
s = int(input('enter you number of shifts: '))
Sum = num
count = 1

for x in range(0,s):
    Sum += num * (10 ** count)
    count += 1
print(Sum)
print()

#Q3
print('Q3')
start = input('enter starting coordinates: ')
end = input('enter ending coordinates: ' )
charge = int(input('enter electric charges: '))
startL = []
endL = []
x = 0
y = 0

for d in range(0,2):
    start.strip()
    startL.append(int(start[0:start.find(' ')]))
    startL.append(int(start[start.find(' ') + 1: len(start)]))

    end.strip()
    endL.append(int(end[0:end.find(' ')]))
    endL.append(int(end[end.find(' ') + 1: len(end)]))

x = endL[0] - startL[0]
if x < 0:
    x = x * (-1)
    
y = endL[1] - startL[1]
if y < 1:
    y = y * (-1)

if (y + x) <= charge and ((x + y) - charge) % 2 == 0:
    print('Y')
else:
    print('N')
print()

#Q4
print('Q4')
minutes = int(input('how many minutes have passed: '))
time = [12,':',0,0]
broken_time = []
count = 0

for x in range(0,minutes):

    #time moving
    time[0] = int(time[0])
    time[3] += 1
    
    if time[3] == 10:  #minutes to tens minutes
        time[3] = 0
        time[2] += 1
        
    if time[2] == 6: #ten minutes to hours
        time[2] = 0
        time[0] += 1

    if time[0] == 13: #reset hours from 12 to 1
        time[0] = 1

    #appending each digit to new list
    broken_time = []
    if len(str(time[0])) == 2:
        time[0] = str(time[0])
        broken_time.append(time[0][0:1])
        broken_time.append(time[0][1:2])
    else:
        broken_time.append(0)
        broken_time.append(time[0])
        
    broken_time.append(time[2])
    broken_time.append(time[3])

    #real stuff check arithmetic or no
    broken_time[0] = int(broken_time[0])
    broken_time[1] = int(broken_time[1])

    if broken_time[0] == 0:
        if broken_time[3] - broken_time[2] == broken_time[2] - broken_time[1]:
            count += 1
    else:
        if broken_time[3] - broken_time[2] == broken_time[2] - broken_time[1] and broken_time[2] - broken_time[1] == broken_time[1] - broken_time[0]:
            count += 1

print(count)
print()

#Q5
print('Q5')
num = int(input('enter the fence numbers u got: '))
lengths = input('enter their lengths: ')
lengthsL = []
count = 0

for x in range(0,num):
    lengthsL.append(int(lengths[count:count+1]))
    count += 2
print(lengthsL)



    

    

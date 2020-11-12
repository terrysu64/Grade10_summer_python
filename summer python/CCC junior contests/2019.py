#Name: Terry Su
#Date: July 29, 2020
#Purpose: CCC 2019 junior questions

#Q1
print('Q1')
apple3 = int(input('how many 3s did the apples score: '))
apple2 = int(input('how many 2s did the apples score: '))
apple1 = int(input('how many 1s did the apples score: '))
apple_total = (apple3 * 3) + (apple2 * 2) + apple1
print()

banana3 = int(input('how many 3s did the bananas score: '))
banana2 = int(input('how many 2s did the bananas score: '))
banana1 = int(input('how many 1s did the bananas score: '))
banana_total = (banana3 * 3) + (banana2 * 2) + banana1
print()

if apple_total > banana_total:
    print('A')
elif apple_total < banana_total:
    print('B')
else:
    print('T')
print()

#Q2
print('Q2')
elements = []
L = int(input('enter the number of lines: '))

for x in range(0,L):
    elements.append(x)
for y in elements:
    elements[y] = input('enter symbol #' + str(y + 1) + ': ')
print()

for symbol in elements:
    print(int(symbol[0:1]) * symbol[2:3])
print()
 
#Q3
print('Q3')
elements = []
L = int(input('enter the number of lines: '))

for x in range(0,L):
    elements.append(x)
for y in elements:
    elements[y] = input('enter message #' + str(y + 1) + ': ')
print()

for message in elements:
    copy_message = message
    output = ''
    for num in range(0,len(message)):
        length = len(copy_message)
        count = 0
        symbol = copy_message[0:1]
        while copy_message.find(symbol) >= 0 and symbol == copy_message[0:1] and symbol != '':
            count += 1
            copy_message = copy_message[1:length]
            length -= 1
        if count != 0:
            output += str(count) + ' ' +  symbol + ' '
    print(output)
print()

#Q4
print('Q4')
grid = [1,2,3,4]
flipsL = []
flips = input('Enter flips: ')

count = 0 
for x in range(0,len(flips)):
    flipsL.append(flips[count:count+1])
    count += 1

for x in flipsL:
    if x == 'H':
        grid0 = grid[1]
        grid1 = grid[0]
        grid2 = grid[3]
        grid3 = grid[2]

        grid[0] = grid0
        grid[1] = grid1
        grid[2] = grid2
        grid[3] = grid3
        
    elif x == 'V':
        grid0 = grid[2]
        grid1 = grid[3]
        grid2 = grid[0]
        grid3 = grid[1]

        grid[0] = grid0
        grid[1] = grid1
        grid[2] = grid2
        grid[3] = grid3

print(grid[0], grid[1])
print(grid[2], grid[3])
print()

    
    
    
        

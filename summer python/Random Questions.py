#Name: Terry Su
#Date: July 15, 2020
#Purpose: Random questions for fun 

#Q1
#create a function that identifies an inputed prime number
def prime(x):
    divi_count = 0
    for divisor in range(2,x):
        if x / divisor == x // divisor:
            divi_count += 1
    if divi_count == 0:
        return 'prime number'
    else:
        return 'factorable'

print(prime(7))
print(prime(4))
print(prime(9))
print(prime(13))
print(prime(2))

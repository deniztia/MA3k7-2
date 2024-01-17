import numpy as np

num = {}  # Use a dictionary to store the numbers

num[1] = int(input('Enter a number:'))

if num[1] < 10:
    num[2] = int(input('Enter second number:'))
    
    if num[2] < 10:
        for i in range(3, 11):
            num[i] = num[i-2] + num[i-1]
            if num[i] > 9:
                num[i] -= 10
    else:
        num[2] = int(input('The number must be an integer less than 10, enter a number:'))
        
        for i in range(3, 11):
            num[i] = num[i-2] + num[i-1]
            if num[i] > 9:
                num[i] -= 10
else:
    num[1] = int(input('The number must be an integer less than 10, enter a number:'))

    if num[1] < 10:
        num[2] = int(input('Enter second number:'))
        
        if num[2] < 10:
            for i in range(3, 11):
                num[i] = num[i-2] + num[i-1]
                if num[i] > 9:
                    num[i] -= 10
        else:
            num[2] = int(input('The number must be an integer less than 10, enter a number:'))
            
            for i in range(3, 11):
                num[i] = num[i-2] + num[i-1]
                if num[i] > 9:
                    num[i] -= 10
    else:
        print('Both numbers must be less than 10.')

for i in range(1, 11):
    print(num[i])

#left triangle
'''
for i in range(1,6):
    for j in range(0,i):
        print('*',end='')
    print('')
    '''


'''
b = 0
# reverse for loop from 5 to 0
for i in range(5, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('')'''

#    right triangle
'''
b=0
for i in range(5,0,-1):
    for j in range(0,i-1):
        print(' ',end='')
    for k in range(0,b+1):
        print('*',end='')
    print('')
    b+=1
'''
'''
#inverted right
b=0
for i in range(5,0,-1):
    for j in range(0,b):
        print(' ',end='')
    for k in range(0,i):
        print('*',end='')
    print('')
    b+=1
'''
#diamond

for x in range(5):
    print(" " * (5 - x), "*" * (2*x + 1))  
#for x in range(5 - 2, -1, -1):
#    print(" " * (5 - x), "*" * (2*x + 1))

#at every step star is increasing by odd number,,so 2n+1
#hence printing the spaces and then stars,,and then consecutive next line

'''
for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()

'''
#pattern print
#expected otpt
'''
# # # # * 
# # # * * 
# # * * * 
# * * * * 
* * * * *
'''
'''
for i in range(5):
    for j in range(4-i):
        print('#',end=" ")
    for j in range(i+1):
        print('*',end=" ")
    print()

'''

#expected otpt
'''
        * 
      * * 
    * * * 
  * * * * 
* * * * *
'''
'''
for i in range(5):
    for j in range(4-i):
        print(' ',end=" ")
    for j in range(i+1):
        print('*',end=" ")
    print()
'''
'''
for i in range(5):
    for j in range(10-i):
        print(' ',end=" ")
    for j in range(i+1):
        print('*',end=" ")
    print()
'''

###################


#1
for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()

#2
for i in range(5):
    for k in range(4-i):
        print('#',end='')
    for j in range(i+1):
        print('*',end='')
    print()

#3
for i in range(5):
    for k in range(4-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()

#4
for i in range(5):
    for j in range(5-i):
        print('*',end='')
    print()

#5.
for i in range(1,6):
    for j in range(6-i):
        print(' ',end='')
    for k in range(i):
        print(k,end=' ')
    print()

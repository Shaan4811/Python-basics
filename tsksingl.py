#1,Write a Python function to find the Max of three numbers.
'''
def maxi(n):
    return max(n)
a=(int(input('entre the lenghth of list')))
z=[]
for i in range(a):
    b=int(input('enter the lis:'))
    z.append(b)
print(z)
print(f'greatest number in the list {z} is {maxi(z)}')
    
'''

'''
def maxi(n):
    z=0
    for i in n[0:]:
        if i>z:
            z=i
    return z
f=int(input('enter the length:'))
x=[]
for i in range(f):
    j=int(input('enter the nmbr'))
    x.append(j)
print(f'greatest number is {maxi(x)}')    
'''    

#Write a Python function to sum all the numbers in a list.
'''
def summ(n):
    z=0
    for i in n:
        z=z+i
    return z
a=int(input('enter the lenghth of list'))
b=[]
for i in range(a):
    c=int(input('enter the numbers'))
    b.append(c)
print(f'sum is {summ(b)}')    
        
'''

#Write a Python function to multiply all the numbers in a list.
'''
def mull(n):
    z=1
    for i in n:
        z=z*i
    return z
a=int(input('enter the length of list'))
b=[]
for i in range(a):
    c=int(input('enter the numbers'))
    b.append(c)
print(f'product of the list {b} is {mull(b)}')    
'''
#Write a Python program to reverse a string.
'''
a='1234pqrst'
def reva(n):
    z=n[::-1]
    return z
print(reva(a))
'''
'''
a='1234pqrst'
for i in a[::-1]:
    print(i,end='')
'''


#5.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
'''
def facto(x):
    if x==1:
        return 1
    else:
        return x*facto(x-1)
a=int(input('enter the numeber:'))    
print(facto(a))    
 '''       
    
#Write a Python program to print the even numbers from a given list.
'''
def even(n):
    j=[]
    for i in n:
        if i%2==0:
            j.append(i)
    return j        
a=int(input('enter the length of list:'))
b=[]
for i in range(a):
    c=int(input('enter the numbers:'))
    b.append(c)
print(even(b))    

'''

#Write a Python function to create and print a list where the values are square of numbers.
'''
def squre(n):
    j=[]
    for i in n:
        f=i**2
        j.append(f)
    return j
a=int(input('enter the length of list'))
b=[]
for i in range(a):
    c=int(input('enter the numbers:'))
    b.append(c)
print(f'square of the list {b}is {squre(b)}')    
'''
#Write a Python function that takes a number as a parameter and check the number is prime or not.
'''
def prm(n):
    j=[]
    for i in n:
        if i%i==0 and i%1==0:
            return i
            #j.append(i)
    #return j
a=int(input('enter the length of list:'))
b=[]
for i in range(a):
    c=int(input('enter the numbers:'))
    b.append(c)
print(f'prime of the list {b} is {prm(b)}')    
'''            
#Write a Python function to check whether a number falls in a given range

'''
def rang(start,end,num):
    if start<num<end:
        print(f'the number {num} lies between{start} and{end}')
    else:
        print('number is not in their')
a=int(input('give the starting of the range:'))
b=int(input('give the last number of range:'))
c=int(input('enter the nmbr:'))
rang(a,b,c)
'''




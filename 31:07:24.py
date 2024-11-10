#1.Write a Python function to find the Max of three numbers.
'''
def maxnum(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
z=int(input("enter the third number:"))
print("max of three number is",maxnum(x,y,z))
'''
#2,Write a Python function to multiply all the numbers in a list.
'''
def mul(numbers):
    total=1
    for i in numbers:
        total*=i
    return total
length=int(input('enter the length oflist'))
num_list=[]
for i in range(length):
    temp=int(input('enter the numbers in list:'))
    num_list.append(temp)
print('product of numbers present in list is:',mul(num_list))
'''
#3.function to reverse a string

'''s='1234abcd'
def rev(a):
    return a[::-1]
print(rev(s))'''

#4. factorial of a number
'''
a=int(input('enter a number:'))
def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
print(f'factorial of {a}:',fact(a))
'''
#5. prime or not

'''a=int(input('enter anumber : '))
def prime(x):
    if x%1==0 and x%x==0:
        print(f'{a} is prime')
    else:
         print(f'{a} is not prime')
prime(a)'''      

#6. even no. in a list //////

'''def evenlist(a):
    li=[]
    a=int(input('enter the values of list seperated by comma : '))
    li.append(a)
    for i in li:
        if li[i]%2==0:
            print(li[i])
evenlist(1)'''
#7,Write a Python program to print the even numbers from a given list.
'''
def even(list):
    new_list=[]
    for i in list:
        if i%2==0:               
            new_list.append(i)
    return new_list
li=[]
n=int(input("Enter size of list "))
for i in range(n):
    temp=int(input("Enter element of list "))
    li.append(temp)
print("Even numbers in ",li,even(li))
'''


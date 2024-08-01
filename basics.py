#escape sequences \n \t
'''print("hello")
print('hh')
print('333')
print("helllo\nworld")
print("hi""+""shh")
print("\thhhhh")
print("jjjj"'+'"hhhh")
print("2"+"4")
print("hhhh"+'22')'''
#print('eee'+11) STRING & INTEGER nadakoola,
'''print("hi"*8)'''
#print("hi"*8) multplicatin matree nadakkum.

#''',"""  (3 quote itta fullaytt unread aaavum)

#ARITHMATIC OPERATORS
 #1.addition
 #2.sub
 #3.mul(*)
 #4.floor division(integer value aaakum,. eduthulla values)denoted by //
#eg;
'''print(5/2)
print(5//2)'''
#5.modulo (reminder value kittan) denoted by %
'''print(5%2)'''
#6.exponential(2^5)
'''print(2**5)'''
#7.root(root of kaanan vendi)
'''print(4**(1/2))'''

# BOOLEAN OPERATORS(<,>,<=,>=,==,!=)   
'''print(7>2)
print(7<2)
print(7>=2)
print(7<=2)
print(7!=7)
print(7==2)'''#comparison operator


#VARIABLES (used for temporary storage,can reassign values but stored in different memory address)

'''a=10
print(a)
print(a+20)
b=20
print(a+b)'''
#diiferent memory address ,eg
'''a=10'''#putyath varumbam payeeth garbage value aavum
'''print(id(a))'''
'''a=30'''# memory address change aavum,putyath store aakumbm putya memory spacil aahn store aava.didinot replace.payayth garbage value aaavum
'''print(id(a))'''

'''a=10
b=30
c=a+b
print("result is",c)
h=a%b'''#modulo
'''print("result is",h)
x=a**b'''#exponential
'''print("result is",x)
y=a**(1/2)'''#root
'''print("result is",y)'''


#TYPE CONVERSION(convert one data type into other)
'''print(int(2)+int(4))
print(int(3.3)+int(2.3))
print(float(5)+float(4))'''

#INPUT FUNCTION

'''a=int(input("enter your frst number:"))#int koduthillel concatination aavum,
b=int(input("enter your secnd number:"))
c=a+b
d=a*b
e=a-b
f=a/b
g=a//b
h=a%b
j=a**(1/2)
print('result for a+b is',c)
print('result for a*b is',d)
print('result for a-b is',e)
print('result for a/b is',f)
print('result for a//b is',g)
print('result for a%b is',h)
print('result for a**(1/2)b is',j)'''

#SWAPPING(using third variable
'''a=5
b=10
print("before swapping")
print('value of a:',a)
print('value of b:',b)
print('__________________')
print("AFTER SWAPPING")
temp=a
a=b
print("value of a:",a)
b=temp
print('value of b:',b)'''
#SWAPPING(without 3rd varble)
'''x=int(input('enter your frst nmbr:'))
y=int(input("enter your secnd number:"))
print("before swapping")
print('value of x:',x)
print('value of y:',y)
print('__________________')
print("AFTER SWAPPING")
x,y=y,x
print('value of x:',x)
print('value of y:',y)'''
#CONDITIONAL STATEMENT
'''
1,if
2,ladder if
3,if else
4,ladder else if
5,elif
'''
#SYNTAX
#1,if
'''
if condition:
    statement
    '''

#Eg
'''if 10>2:
    print('10 is greater')
print("pgm finished")    
'''
#
'''if 5!=5:
    print("they are not equal")
print("pgm is finished")'''
#2,ladder if
'''
if condition:
    statement
    if condition:
        statement
        if condition:
            statement
'''
#eg
'''num=3
if num>2:
    print("3 is greater")
    if num>1:
        print('3 is greater')
        if num==3:
            print('it is same')
print("pgm finished")'''            

#another
'''num=3
if num>2:
    print("3 is greater")
    if num<1:
        print('3 is greater')
        if num==3:
            print('it is same')
print("pgm finished")'''
#3,if else
''''
if condition:
    statement
else:
    statement
'''
#eg
'''
x=int(input("enter your frst number:"))
y=int(input("enter your 2nd number:"))
if x==y:
      print("square")
else:
    print("rectangle")
'''    
"""x=int(input("enter the number:"))
if x%2==0:
    print("even")
else:
    print("odd")
"""
#4,if else ladder
'''
if condition:
    statement
else:
    if condition:
        statement
    else:
        statement
'''
#eg
'''
num=int(input('enter a number:'))
if num>12:
    print('hello')
else:
    if num<2:
        print('welcome')
    else:
        if num==10:
            print('hi')
        else:
            print('python')
'''
#5,elif
'''
if condition:
    statement
elif condition:
    statement
elif condition:
    statement
else:
    statement
'''
#eg
'''
colour=input('enter a colour:')
if colour=="red":
    print('colour is red')
elif colour=='blue':
    print('colour is blue')
elif colour=='green':
    print('colour is green')
else:
    print('colour is not RGB')
'''
#inplace operator
'''    
a=10
a+=5
print(a)#15
b=10
b-=5
print(b)#5
c=20
c/=2
print(c)#10
d=2
d*=10
print(d)#20
e=100
e**=2
print(e)#1000
f=200
f//=3
print(f)#66
g=100
g%=3
print(g)#1
'''
#Logical operator
#and,or,not
'''print(5>3 and 5==5)'''#True(and operator returns true if both operands are true)
'''print(5<3 or 5==5)'''#True(or operator returns true if atleast one operand is true,both false then false)
'''print(not 3==3)'''#False(not operator returns the opposite boolean value of its operand)

#Identity operator
# is,is not
'''
a=10
b=5
c=10
print(id(a))'''# id represent memory  address
'''print(id(b))
print(id(c))'''
'''print(a is c)'''# is returns true if both varialbles memmory address is same
'''print(a is not b)'''#isnot  returns  true if both memory adddress is not same
 
#String formatting
# format(),f-string method
'''name=input("enter your name")
age=int(input("enter your age"))
print("my name is {} and i'm {} years old".format(name,age))
print("my name is {} and i'm {} years old".format(age,name))# in format method age,name replace cheyth kaynja maarypoovum so next method use cheyya
'''
#f string method
'''print(f"my name is {name} and i'm {age} years old")'''

#16/07/2024

#check vowel or not
# data in operator
'''
data=input('enter a letter:')
vowel="aeiouAEIOU"
if data in vowel:
    print("it is vowel")
else:
    print('not vowel')
            
'''

#which is greater
'''
x=int(input("enter the number"))
y=int(input("enter the number"))
z=int(input("enter the number"))
if x>y and x>z:
    print(f"{x} is greater")
elif y>x and y>z:
    print(f"{y} is greater")
else:
    print(f"{z} is greater")
'''
#Loops
#while loop
"""
initialisation
while condition(limit):
     statment
     increment
"""
#eg
'''
i=1
while i<=10:
    print('hello')
    i+=1
print("finished")
'''

# 1-10 nmbrs
'''
i=1
while i<=10:
    print(i)
    i+=1
'''
#1-10 even nmbrs
'''
i=1
while i<=10:
    if i%2==0:
        print(i)
    i+=1
'''
#mul
'''
i=int(input("Enter the number to be multiplied"))
j=int(input("Enter the limit"))
z=1
x=0
while z<=j:
    x=i*z
    print(f"{i}*{z}={x}")
    z+=1
'''
#18/7/24
'''
while 1==1:
    print('hello')
    break
'''

#
'''
i=1
while i<=10:
    if i==5:
        break
    print(i)
    i+=1
'''

#continue
'''
i=0
while i<9:
    i+=1
    if i==3:
        continue
    print(i)
'''
#
'''
i=0
while i<=10:
    i+=1
    if i==1:
        print("skipping 2")
        continue
    if i==5:
        print('hello')
        break
    print(i)
'''
#
'''
i=10
while i>0:
    if i==5:
        i-=1
        break
    print(i)
    i-=1
print('thankyou')
'''


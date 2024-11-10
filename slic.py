#01/08/2024

#list comprehensions
#syntax:new_list=[expression for item in iterable if condition==True]
'''
fruits=['apple','banana','kiwi','mango','berry']
'''
'''
new_list=[]
for i in fruits:
    if 'a' in i:
        new_list.append(i)
print(new_list)
'''


'''
new_list=[i for i in fruits if 'a' in i]
print(new_list)
'''

'''
new_list=[i for i in fruits if 'banana' not in i]
print(new_list)
'''

#q
'''
numbers=[4,2,8,5]
squares=[i**3 for i in numbers]
print(squares)
'''
#vowels
'''
data ='codeme'
vowel="aeiouAEIOU"
new_list=[i for i in data if i in vowel]
print(new_list)
'''

#1-10 even nmbrs
'''
num=[i for i in range(1,11) if i%2==0]
print(num)
'''
#10,20,30,40,50
'''
num=[i for i in range(10,51,10)]
print(num)
'''

#list slicing(start:end:stop)
'''
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(a[:])
print(a[3:])
print(a[:7])
print(a[4:10])
print(a[3:12:2])
print(a[::2])
print(a[3::2])
print(a[:14:3])
'''
#Reverse slicing
'''
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
print(a[::-1])
print(a[-2:])
print(a[:-3])
print(a[-5:-2])
print(a[3:1:-1])
print(a[2:-2])
print(a[5:2:-1])
print(a[-1:-4:-1])
print(a[-4:-1:2])
print(a[-2:-5:-1])
print(a[-1:-6:-1])
print(a[-6:-2:-1]) #empty list,bcz starting cheruthum ending valuthum.
print(a[4:2])#empty list,bcz starting valthum ending cheruthum ayoond
'''
#q
'''
a='how are you'
print(a[0:])
print(a[8:])
print(a[2:10])
print(a[-1:])
print(a[-1:-8:-2])
print(a[-8:-1:2])
print(a[::-1])
'''

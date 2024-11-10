 #1,Create a list containing the first 10 even numbers.
'''
a=[]
for i in range(1,21):
    if i%2==0:
        a.append(i)
print(a)        
'''        
#Write a program that removes duplicates from a list without using a set.
'''
a=[1,2,'hell',2,'hi',1]
b=dict.fromkeys(a)
a=list(b)
print(a)
'''
'''
a=[1,2,'hell',2,'hi',1]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)        
'''    
#Reverse a list in-place (without creating a new list).
'''
a=[1,2,'hell',2,'hi',6]
a.reverse()
print(a)
'''
#Swap the first and last elements of a tuple.
'''
a=(1,2,5,4,3,8)
b=list(a)
b[0],b[-1]=b[-1],b[0]
a=tuple(b)
print(a)
'''
#Count the number of occurrences of a specific value in a tuple.
'''
a=('hell','abd','abd',5,77)
b=a.count('abd')
print(b)
'''
#Check if two tuples are equal, considering both element order and values.
'''
a=('hell','abd','abd',5,77)
b=('hell','abd','abd',5,77)
if a==b:
    print('equal')
else:
    print('false')
'''
#Merge two dictionaries into a new dictionary, combining values for duplicate keys
'''
x={'name':2,'age':'20',"place":656}
y={'name':3,'age':22,"place":7}
for i in y:
    if i in x:
        x[i]=x[i]+y[i]
    else:
        x.update({i:y[i]})
print(x)    
'''

'''another method'''
'''
a={'name':'muhammad','age':'20',"place":'kozhikode'}
b={'name':'shaan','age':22,"place":'calicut'}
a.update(b)
print(a)
'''
#Find the key with the highest value in a dictionary.
'''
a={'apple':2,'mango':3,'jack':4,'hi':1}
b=max(a,key=a.get)
print(b)
'''
#Create a dictionary from two lists, where the first list contains keys and the second list contains values.

'''
keys=['name','age','place']
values=['shaan','22','atholi']
a={}
for i in range(len(keys)):
    a[keys[i]]=values[i]
print(a)    
'''
#Check if a specific key exists in a dictionary.
'''
a={'hello':22,"hi":2,'subject':'english'}
b=input('enter the key:')
if b in a:
    print('exists')
else:
    print('not exist')
'''    








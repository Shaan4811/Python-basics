#Data structures

'''
1,List
2,Tuple
3,Dictionary
4,Set

'''

#List(ordered,indexed,duplication allowed,mutable(change))
'''
a=["hello",23,"red",22.22,True,"black",33,"red"]
print(a)
print(type(a))
'''
#Create  a list by using list function
'''
b=list((1,2,3,4,5))
print(b)
'''

#Item get from a list by index
'''
print(a[0])
print(a[3])
'''
#19/07/24

#length
'''
print(len(a))
'''
#new item add into list

#1,append()->item added into last position
'''
a.append('orange')
print(a)
a.append(100)
print(a)
'''
#insert()-> an item  add into specified position
'''
a.insert(1,'apple')
print(a)
'''
#replace an item in a list
'''
a[2]='gray'
print(a)
'''
#an item delete from list

#1,pop()->last item deleted
'''
a.pop()
print(a)
'''
#2,pop(index)
'''
a.pop(4)
print(a)
'''
#3,remove->specified item deleted
'''a.remove("black")
print(a)
a.remove(23)
print(a)
'''
#index()-> find index number
'''
print(a.index('black'))
'''
#count()
'''
print(a.count(('red'))
'''
#Number list
'''
num=[23,5,1,2,9,5]
'''
#sum
'''
print(sum(num))
'''
#max
'''
print(max(num))
'''
#min
'''
print(min(num))
print(num[1]+num[2])
'''
#sort
'''
num.sort()
print(num)
'''
#sorted
'''
print(sorted(num))      
'''
#del -> delet whole list
'''del a
print(a)'''

#thaye thaye kitttan
'''
a=["hello",23,"red",22.22,True,"black",33,"red"]
i=0
print(len(a)-1)
max_length=len(a)-1
while i<=max_length:
    print(a[i])
    i+=1
'''
#another method in for loop
'''
a=["hello",23,"red",22.22,True,"black",33,"red"]
for i in a:
    print(i)
'''
#range(start,end,step)

'''print(list(range(12)))
print(list(range(3,20)))
print(list(range(3,20,3)))
'''
'''
for i in range(1,11): #print 1 to 10
    print(i)

for i in range(11): # print 0 to 10
    print(i)

for i in range(2,11,2): #print even numbers from 2
    print(i)

for i in range(1,11): # print even numbers
    if i%2==0:
        print(i)    
'''
#colors
'''
b=['red','black','white']
c=[]
for i in b:
    z=len(i)
    c.append(z)
print(c)    
'''
#2,TUPLE(ordered,immutable, allow duplicate values,indexed)
#creation of tuple
'''
a=('apple','banana','cherry',1,2,3,True,False)
print(a)'''
'''
a = ("apple", "banana", "cherry", "apple", "cherry")
print(a)
'''

#length
'''print(len(a))'''

#Create Tuple With One Item
'''a = ("apple",)'''# coma, ittilel string aaykm one item varumbam
'''print(type(a))'''

#NOT a tuple
'''tuple = ("apple")
print(type(tuple))'''

#define by using tuple() function

'''a=tuple(('apple'))'''# rand brackets,tuple function bracket and item bracket
'''print(a)'''

#Access Tuple Items by index number
'''print(a[1])'''

#access item byNegative Indexing(-1 refers to the last item, -2 refers to the second last item etc.)
'''print(a[-1])'''#-1 refers to the last item
'''print(a[-2])'''#-2 refers to the second lasst item

#Range of Indexes
'''print(a[2:5])'''#-> index number from 2 to 5 is printed,2 print aavum 5 print avoola
'''print(a[:5])'''#-> upto index 5 vare print aavum,01234
'''print(a[2:])'''#-> print index number 2 to last,23456

#Range of Negative Indexes
'''print(a[-4:-1])'''#-> -4 to 01 print aaavm,-4 printavm -1 print avoola


#Check item is present in the tuple
'''
if 'apple' in a:
    print("yes,'apple'is in there")
else:
    print("no,it is not present")
'''
#change tuple values(frst list aaaka nnt add akka nnit tuple aaka,bcz unchangable)
'''
x=('apple','banana','cherry',1,2,3,True,False)
y=list(x)
y[1]='kiwi'
x=tuple(y)
print(x)
'''
#add item to tuple
'''
x=('apple','banana','cherry',1,2,3,True,False)
y=list(x)
y.append('orange')
x=tuple(y)
print(x)
'''

#add tuple to tuple
'''
x=('apple','banana','cherry',1,2,3,True,False)
y=('black',)
x+=y
print(x)
'''
#remove item from tuple
'''
x=('apple','banana','cherry',1,2,3,True,False)
y=list(x)
y.pop(2)
y.remove('apple')
x=tuple(y)
print(x)
'''
#del operation
'''
x=('apple','banana','cherry',1,2,3,True,False)
del x
print(x)
'''
#clear(tupleil clear illa,list aayt convert aakett clear cheyyanm)
'''
x=('apple','banana','cherry',1,2,3,True,False)
y=list(x)
y.clear()
x=tuple(y)
print(x)
'''



#22/07/24

#Dictionary (key:value) (ordered,unindexed,key unique,mutable)
'''
student={'name':'john','age':20,'place':'calicut',23:76,'location':'calicut'}'''
'''print(type(student))
print(student)'''

#1,value access from a dictionary by using key
'''print(student['age'])
print(student['location'])'''
'''print(student['data'])'''#key error,bcz data is not defined

#2.get()

'''print(student.get('place'))
print(student.get(23))'''
'''print(student.get('data'))'''#none will occur
# creating a dictionary by using dict function
'''a=dict([('employee','tom'),('salary',100000)])
print(a)'''
'''
B=dict([('a','b'),(3,4),('d','f'),{2:33,4:'hell'},[1,2]])
print(B)
'''
#1,updating a value of key
'''student["age"]=[90,22,33]
print(student)'''

#2,updating a key value pair in dictionary
'''student['color']='red'
print(student)'''

#2,update()
'''student.update({'subject':'english'})
print(student)'''

#clear-> dictionary remains,data deletd
'''student.clear()
print(student)'''

#len
'''print(len(student))'''

#deleting a pair from dictionary

#1,popitem() ->last pair deleted
'''student.popitem()
print(student)'''

#2,pop()
'''student.pop('age')
print(student)'''

#3,del

'''del student['name']
print(student)'''
#del -> deleting dictionary
'''del student'''
#copy
'''sam=student.copy()
print(sam)'''

#any function()-> eetelum 1 true aayal true aaykm
'''mydict={False:'red',False:'black'}
print(any(mydict))

mydict={True:'red',False:'black'}
print(any(mydict))'''

#all function()-> randum true aayal true return cheyym
'''mydict={True:'red',False:'black'}
print(all(mydict))

mydict={True:'red',True:'black'}
print(any(mydict))'''

#sorted
'''d={1:'red',8:'black',3:'violet',23:'black',5:'gray'}
print(sorted(d))'''

'''
student={'name':'john','age':20,'place':'calicut',23:76,'location':'calicut'}
'''
'''for i in student:
    print(i)'''#keys matree print aavm
    
'''for i in student.values():
    print(i)'''#values only print aaavm
    
'''for i in student.keys():
    print(i)'''#keys only print aavm

'''for i in student.items():
    print(i)'''#items full display cheyym

'''
print(student.keys())
print(student.values())
print(student.items())
'''






#set (collection of unique data)(unorderd,unindexed,duplication not allowed,mutable)
'''
mixed_set={'hello','red',23,'blue',45.9,12,True,'red'}
print(mixed_set)
x=set() #empty set
print(type(mixed_set))
'''
#create a set by using set function
'''
a=[1,45,3,7,0,9]
b=set(a)
print(b)
'''

#add new item into an set

#1,add()
'''
mixed_set={'hello','red',23,'blue',45.9,12,True,'red'}
mixed_set.add('apple')
mixed_set.add(90)
mixed_set.add(('html','css'))
print(mixed_set)
'''

#2,update
'''
mixed_set={'hello','red',23,'blue',45.9,12,True,'red'}
mixed_set.update('kiwi')
print(mixed_set)


mixed_set.update(('orange','banana'))
print(mixed_set)

'''
#delete an item from set

#1,discard()
''''
mixed_set={'hello','red',23,'blue',45.9,12,True,'red'}
mixed_set.discard('hello')
print(mixed_set)'''

'''
mixed_set.discard('hi')
print(mixed_set) ''' #error occur avoola,illatha sadanm ahnelm

#2,remove()
''''
mixed_set.remove('hello')
print(mixed_set)'''
'''
mixed_set.remove('hi')
print(mixed_set)'''# illlatha sadnm aahnel error aavum

#clear,del,len,copy


#union(|)
'''
a={20,30,60,35,25,90,45}
b={99,66,30,77,45,90,11}
print(a|b)'''
#intersection(&)
'''print(a&b)'''
#difference(a-b,b-a) ail ullathm b il llathathm,b il ullathm a il illlathathm
'''print(a-b,b-a)'''
#symmetric difference(^)  a il ullathm bil ullathathm koodi set aka
'''print(a^b)'''



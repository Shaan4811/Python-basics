#2/08/24

#Exception Handling
'''
try:
    print('hello')
    print(5/0)
except ZeroDivisionError:
    print('error handling')
finally:
    print('hi')
'''    

#Try,except,finally
'''
a='hello'
b=2
try:
    print(a+b)
except TypeError:
    print('error handling')
finally:    
    print('python')
'''

#q
'''
a=['hello','red','kiwi']
print(a[1])
try:
    print(a[3])
except IndexError:
    print('error handling')
finally:    
    print(a[0])
'''

#q
'''
def fun(a):
    if a<4:
        b=a/(a-3)
        print(f'value of {b}:')
    else:
        print('greater value')
try:    
    fun(3)
except ZeroDivisionError:
    print('error handling')
finally:
    fun(5)
    fun(2)
'''

#Raise
'''
print('hello')
raise TypeError('error detected')
print('hi')
'''


'''
try:
    print(5/0)
except Exception as e:
    print('error has occured')
    raise NameError('cant divide with 0')
'''
'''
def divide(a,b):
    if b==0:
        raise Exception("cannot divide by zeo")
    returna/b
try:
    result=divide(10,0)
except Exception as e:
    print("errror occures",e)
print(20,5)
'''


    

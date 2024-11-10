'''class Student:
    x=5
    b='Hello'
s1=Student()
s2=Student()
print(s1.x)
print(s1.b)
print(s2.b)

class Car:
    x='suv'
    y='sedan'
c1=Car()
print(c1.x)'''

#07 - august

'''class Sample():
    a=5
s1=Sample()
s2=Sample()
print(s1.a)
s1.a=25
print(s1.a)
print(s2.a)'''

#self instance

'''class Sample:
    a=5                       #attribute
    def index(self):          #method
        print('Hello World')
s1=Sample()
print(s1.a)
s1.index()'''

'''class Sample:
    a=5                       #attribute
    def index(self):           #method
        a='hello'
        print('value of a : ',a)
s1=Sample()
print(s1.a)
s1.index()'''

'''
class Sample:
    a=5                       #attribute
    def index(self):           #method
        a='hello'
        print('value of a : ',self.a)
s1=Sample()
print(s1.a)
s1.index()

'''


#08/08/2024

#class


#create a calass
'''
class Room:
    length =0.0
    breadth=0.0



    #method to calculate area

    def calculate_area(self):
        print('Area of Room =',self.length * self.breadth)

#create object of room class

study_room = Room()
bed_room = Room()

#assign values to all properties

study_room.length = 42.5
study_room.breadth = 30.8
bed_room.length = 20.5
bed_room.breadth = 40

#access method inside class

study_room.calculate_area()
bed_room.calculate_area()
'''


#
'''

class Room:
    def fun(self,length,breadth):
        self.l = length
        self.b = breadth

r2 = Room()
r1 = Room()
r1.fun(40,20)
print(r1.l)
print(r1.b)
r2.fun(30,10)
print(r2.b)
print(r2.l)
'''           

#
'''
class Room:
    def fun(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print(f'area is {self.length*self.breadth}')    
r2 = Room()
r1 = Room()
r1.fun(40,20)
print(r1.length)
print(r1.breadth)
r2.fun(30,10)
print(r2.breadth)
print(r2.length)
r3=Room()
r3.fun(99,80)
r3.area()   
'''
#Constructor- function/mathod that call at time object creation
'''

class Person:
    work_place = 'IBM'  #class variables
    def __init__(self,name,age):
        self.name = name  #instance variable
        self.age = age
    def display(self):
        print('Name of person',self.name)
        print('Age of person',self.age)
        print('Workplace of person is',self.work_place)
        
p1=Person('ravi',21)
p1.display()
        
'''
#------------------------------------------------------------------------------
# class methods demo
'''
class Student:
    # class variable
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance method
    def show(self):
        # access instance variables and class variables
        print('Student:', self.name, self.age, Student.school_name)

    # instance method
    def change_age(self, new_age):
        # modify instance variable
        self.age = new_age


    #class method
    @classmethod
    def modify_school_name(cls, new_name):
        #modify class variables
        cls.school_name = new_name

s1 = Student('harry',12)

#call instance methods

s1.show()
s1.change_age(14)

#call class method
Student.modify_school_name('XYZ School')

#call instance methods
s1.show()
'''

#-----------------------------------------------------------------------
#09/08/24


#inheritance

#Synatx
'''
class Superclass:
    #attribute and methods
class Subclasss(Superclass):
    #attributes and methods

'''    


'''
class Animal:
    def bark(self):
        print('animal barking')
class Human(Animal):
    def speak(self):
        print('speaking')
h=Human()
h.bark()
h.speak()
'''

#
'''
class Animal:
    #attribute and method of the parent class

    def eat(self):
        print('i can eat')

#inherit from animal
class Dog(Animal):

    #new method in subclass
    def display(self):
        #access name attribute of superclass using self
        print('My name is',self.name)

#create an object of the subclass        
labrador= Dog()

#access superclass atrribute and method

labrador.name='rohu'
labrador.eat()

#call subclass method

labrador.display()
'''


#
'''
class Vehicle:

    def __init__(self,name,year,color):
        self.name=name
        self.year=year
        self.color=color

    def display(self):
        print('Name of a vehicle:',self.name)
        print('Year launch vehicle:',self.year)
        print('Color of he car is:',self.color)

class Car(Vehicle):
    def __init__(self,name,year,color,brand):
        self.brand = brand
        #invoking parent class constructor
        Vehicle.__init__(self,name,year,color)
    def display(self):
        print('Name of a vehicle:',self.name)
        print('Year launch vehicle:',self.year)
        print('Color of he car is:',self.color)
        print('brand of vehicle is:',self.brand)
a=Car('polo','1987','red','vw')
a.display() #method overriding
'''

#---------------------------------------------------------------------------------

#operator overloading
'''
a=10
b=5
c=a+b #addition
a='a'
b='v'
c=a+b #concatenation
# same operator with different operation
'''
#method overloading(it only work for certain condition)
'''
def room(a,b):
    return a+b
def room(a,b,c):
    return a+b+c


'''

#______________________________________________--------------__

'''
# parent class
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name, self.age)

# child class
class Student(Person):
  def __init__(self, name, age):
    self.sName = name
    self.sAge = age
    # inheriting the properties of parent class
    super().__init__("Rahul", age)

  def displayInfo(self):
    print(self.sName, self.sAge)

obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()
'''

#---------------------------------------------------------------------------------

#Multiple inheritance

#Syntax
'''
class Parent1:
    #statement
class Parent2:
    #statement
class Child(Parent1,parent2):
    #statement
'''


#
'''
class Calculation:
    def sum(self,a,b):
        return a+b
class Calculation2:
    def mul(self,a,b):
        return a*b
class Derived(Calculation,Calculation2):
    def divide(self,a,b):
        return a/b

d=Derived()
print(d.sum(1,3))
print(d.mul(1,3))
print(d.divide(10,2))
'''


#---------------------------------------------------------------------------------

#Multilelvel inheritance


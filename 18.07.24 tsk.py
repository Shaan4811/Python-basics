#MUHAMMAD SHAAN KC
# Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.
'''
i=input('enter a number:')
if i=='1':
    print("monday")
elif i=='2':
    print("tuesday")
elif i=='3':
    print("wednesday")
elif i=='4':
    print("thursday")
elif i=='5':
    print("friday")    
elif i=='6':
    print('saturday')
elif i=='7':
    print('sunday')
else:
    print('input valid number')
'''    
#Write a program to accept a number from 1 to 12 and display name of the month and days in that month
'''
j=int(input("Enter a number between 1 to 12:"))
if j==1:
    print("january and no of days:31")
elif j==2:
    print("february and no of days:28")
elif j==3:
    print("march and no of days:31")
elif j==4:
    print("april and no of days:30")
elif j==5:
    print("may and no of days:31")
elif j==6:
    print("june and no of days:30")
elif j==7:
    print("july and no of days:31")
elif j==8:
    print("august and no of days:31")
elif j==9:
    print("september and no of days:30")
elif j==10:
    print("october and no of days:31")
elif j==11:
    print("november and no of days:30")
elif j==12:
    print("december and no of days:31")
else:
    print("invalid input")      
'''
#Accept any city from the user and display monument of that city.
''' City                                 Monument
Delhi                               Red Fort
Agra                                Taj Mahal
Jaipur                              Jal Mahal'''

'''
k=(input("Enter a city name from Delhi,Agra,Jaipur:"))
if k=="Delhi":
    print("monument for this city is Redfort")
elif k=="Agra":
    print("monument for this city is Tajmahal")
elif k=="Jaipur":
    print("monument for this city is Jalmahal")
else:
    print("invalid input")
'''
#Write a program to check whether a number entered is three digit number or not.
'''
number = input("Enter a number: ")
if 100 <= num <= 999:
    print(f"{num} is a three-digit number.")
elif:
    print(f"{num} is not a three-digit number.")
elif:
    print("Invalid input. Please enter a valid number.")
'''
#Write a program to check whether a person is senior citizen or not.
'''
age = int(input("Enter your age: "))
if age >= 60:
    print("You are a senior citizen.")
else:
    print("You are not yet a senior citizen.")
'''
#Write a program to find the lowest number out of two numbers excepted from user.
'''
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
lowest_number = min(num1, num2)
print(f"The lowest number between {num1} and {num2} is {lowest_number}.")
'''
#Write a program to check whether a number (accepted from user) is positive or negative
'''
number = float(input("Enter a number: "))  
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("The number is zero.")
'''
#Write a program to check whether a number  is prime or not.
#Write a program to print first 10 integers and their squares using while loop.
'''
i=1
while i <= 10:
    square = i ** 2
    print(f"{i} squared is {square}")
    i += 1
'''
#Write a Program to print all the characters in the string ‘PYTHON’ using while loop.
'''
string = 'PYTHON'
length = len(string)
i = 0
while i < length:
    print(string[i])
    i += 1
'''
#Write a program to accept 10 numbers from the user and display the largest & smallest number number.
'''
i=1
while i<=10:
    if i%2==1:
        print(i)
    i+=1
----------------------------------------------------------'''
'''
i=1
while i<=10:
    print(i)
    i+=1
----------------------------------------------------------'''
'''
i=0
while i<10:
    print(i)
    i+=1

----------------------------------------------------------'''
'''
i=1
z=0
k=2
while i<=10:
    z=i*i
    print(f"{i}^{k}={z}")
    i+=1
----------------------------------------------------------'''
'''
L=[23,45,32,25,46,33,71,90]
i=0
while L[i]<=7:
    if L[i]%2==1:
        print(L[i])
    i+=1
'''



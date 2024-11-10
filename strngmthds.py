#capitalize(Converts the first character to upper case)
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

#casefold(Converts string into lower case)
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#center(Returns a centered string)
txt = "banana"
x = txt.center(20)
print(x)

#count(Returns the number of times a specified value occurs in a string)
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#encode(Returns an encoded version of the string)
txt = "My name is Ståle"
x = txt.encode()
print(x)

#endswith(Returns true if the string ends with the specified value)
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

#expandtabs(Sets the tab size of the string)
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

#find(Searches the string for a specified value and returns the position of where it was found)
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

#format(Formats specified values in a string)
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#index(Searches the string for a specified value and returns the position of where it was found)
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

#isalnum(Returns True if all characters in the string are alphanumeric)
txt = "Company12"
x = txt.isalnum()
print(x)

#isalpha(Returns True if all characters in the string are in the alphabet)
txt = "CompanyX"
x = txt.isalpha()
print(x)

#isascii(Returns True if all characters in the string are ascii characters)
txt = "Company123"
x = txt.isascii()
print(x)

#isdecimal(Returns True if all characters in the string are decimals)
txt = "1234"
x = txt.isdecimal()
print(x)

#isdigit(Returns True if all characters in the string are digits)
txt = "50800"
x = txt.isdigit()
print(x)

#isidentifier(Returns True if the string is an identifier)
txt = "Demo"
x = txt.isidentifier()
print(x)

#islower(Returns True if all characters in the string are lower case)
txt = "hello world!"
x = txt.islower()
print(x)

#isnumeric(Returns True if all characters in the string are numeric)
txt = "565543"
x = txt.isnumeric()
print(x)

#isprintable(Returns True if all characters in the string are printable)
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

#isspace(Returns True if all characters in the string are whitespaces)
txt = "   "
x = txt.isspace()
print(x)

#istitle(Returns True if the string follows the rules of a title)
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

#isupper(Returns True if all characters in the string are upper case)
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

































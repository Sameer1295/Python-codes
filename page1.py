"""
this page will have all practice codes 
of basic python
"""
# assign values to var with datatype
x = int(1)
y = float(20.3)
z = str(33)

# many values to many  vars
x, y, z = "Orange", "Banana", "Cherry"
# print(y)

# one value to multiple vars
x = y = z = "Orange"

# unpack a list
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
# print(z)

# concatenation
str1 = "hello i am"
str2 = "Sameer"
int1 = 1
# print(str1+str2)
# print(str1+int1) this will return error as str + int

# Global variable keyword
def myfunc():
    global xx
    xx = "awesome"

myfunc()
# print('I am '+xx)

#python numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# print(a)

#Looping Through a String
strr = "SuperKings"
# for x in strr:
#     print(x.upper())

# print("Kings" in strr)
# print("expensive" not in strr) #returns True or False

# print(strr[:3]) #first 3 letters
# print(strr[2:5]) # from position 2 to 5
# print(strr[-5:-1]) #slicing from end

a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!'] spslits with comma

#format strings
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# for loop with break stmt
for x in range(6):
  print(x)
  if x == 3: break
else:
  print("Finally finished!")

# creating a function
batsman = ['Sehwag','Gambhir','V Kohli','Raina']
slot = [0,1,2,3]
def lineup(batters):
    for x in batters:
        print(x)

lineup(batsman)

#python functions and lambda continue from here...



































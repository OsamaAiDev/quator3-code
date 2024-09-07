# from ast import List
import re


# name: str = "Osama"
# print(name)

# age: int = 27


# qualification: str = "BSE Computer Science"

# # \ means line continue next logic is on new line we can't write any words after \ otherwise error
# message: str = "Hi there my name is " + name \
# + " my age is "+ str(age)

# print(message)

# new_message = f"""Hi my name is {name} and my age
# is {age} and i love this expression {2+2}"""

# print(new_message)

# # print escape character in string use \ before special character

# my_data = "Hi it\"s me"
# print(my_data)

# # if string conist on more than one line then use multi formatted string boundary 
# another_message = f"Hi my name is {name} and my age is {age} and i love this expression {2+2}"

# print(another_message)

# # old way of string formatting in c and java
# id: int = 1

# card: str = """
# Name: %s
# Age: %d
# Id: %d

# """ %(name, age, id)

# print(card)
# print(type(card))

# # string method
# # {} are called placeholders
# # and it based on index
# print("Hello {} your age is {}".format(name, age))
# print("Hello {1} your age is {0}".format(name, age))

# # we can also define placeholder by ourself and assign values to them
# name : str = "Osama"
# age : int = 26

# print("Age is {a} and my name is {b}".format(a = age, b = name))

# # print(id("123")) # error int obj is not callabe because i created variable with same name

# # dir func return list which contain all the methods and attributes of specified object

# # print(dir(str))
# print( len([i for i in dir(str) if "__" not in i]))

# prefix remove from the start
# if the value does not match then return whole string
# it does not modify the original string return new string
# web : str  = "https://google.com"
# print(web.removeprefix("https://"))
# print(web)
# name : str = "   Osama         Arshad    Khan   "
# name1 : str = re.sub(' {2,100}', " ", name).strip()
# print(name1)

message: str ="""Hello welcome to my world
my name is osama
this is my message"""
# message2: str ="Hello welcome to my world
# my name is osama
# this is my message" # error
message3: str ="Hello welcome to my world \
my name is osama \
this is my message"

print(message3)

code: str = """
print("Hello World")
no1: int = 1
no2: int = 2
print(no1 + no2)
"""

exec(code)
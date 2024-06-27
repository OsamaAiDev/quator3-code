import pandas as pd

# return the ascii code of the char

# print(ord("a"))
# ord("a") # direct bhe print kr da ga

# is ma ascii code ka character return kr da ga
# if the ascii code is incorrect then it show value error
# print(chr(345144))

# it is called operation we have operator and operands to perform operation

# print(2+2)
# 2+2 # direct bhe result a jaye ga

# tables = pd.read_html("https://www.w3schools.com/python/python_operators.asp") # return list
# print(type(tables))

# print(tables[0])

# floor division point value hata kr return kr deta ha value
# print( 12 // 5)
# power exponentiation is ke precedence right to left hoti h or bake operators ke left to right

# print (2**2)

# in python we dont have === concept

# if 2 === 2:
#     print("hello")

# identity operator
# is operator check krta ha backend pr dono varibale ka memnory same hn?
# a : str = "abc"
# b : str = "abc"

# print(a is b)


# python membership operator

names : list[str] = [chr(i) for i in range(65, 91) ]

# print(names[0])

# In python we use PEMDAS rule

# agr tuble sath [] use kia hn tu item ke type define krne pare ge
# agr sirf tuple likha ha type ka tor pr tu n no items dal sakta hn

# my_tuple: tuple = 12, 2, 12.0, "osama"
# print(my_tuple)

# unzip concept backend pr touple bana or ek ek ka value nikal kr variable ko assign kr de
# jitne values hn utna he variables dena para ga warna value error

a , b, c = 12, "a", 12.0

my_scores: tuple[int, int, int] = (12, 21, 22)

# * ko jb string ka sath use krta hn tu utne time iteration ho jati h

# print("a" * 3)

print("osama" * 3)

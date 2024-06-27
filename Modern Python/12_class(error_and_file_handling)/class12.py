
# abhe custom exception class bhe bana sakta hn
# class NumberErrror(Exception):
#     pass
# input: int = int(input("Enter no between 1 and 10 "))

# if(input<1 or input>10):
#     # user agr violation krta ha tu us ko error phank do
#     # raise ValueError("Enter a value between 1 and 10")
#     raise NumberErrror("Enter a value between 1 and 10")
# else:
#     print(input)


from typing import TextIO


data:TextIO = open("abc.txt") # created a connectivity with abc file
print(data.read()) # read all the data
data.close() # close the connectivity cursor dobra file ke begining pr chala gia

# file open ke or us ka name file likh dia jo ka ek local var h
# with block benefit h connection auto close kr da ga block sa bahr jana pr
# with open("./abc.txt") as file:
#     print(file.read())

# # read line line read krna ka bd \n dal deta h is lia hm na print func ka \n ko ktm kr fia end sa
# with open("./abc.txt") as file:
#     print(file.readline(), end="") # read only one line at a time generator func 

# with open("./abc.txt") as file:
#     print(file.readlines()[:3]) # iteration kr ka list ma dal ga or ma us ma sa first 3 lines read kr raha hn data understand krna ka lia

# open file in write mode read nai kr sakta hn is ma porana sara data ura kr new data add kr da append nai krta
# with open("./abc.txt", "w") as file:
#     file.write("alo")
#     file.read() # error

# r+ read write  yaha pr write kia 
# with open("./abc.txt", "r+") as file:
#    file.write("Pakistan")
#    file.seek(0) # set cursor back to 0 index
#    print(file.read())

# agr file exist nai krti file created new file exist krti h file already tu error
# with open("./abc.txt", "x") as file:
#    file.write("Hello world")

# # r read b binary + means all mode
# with open("./abc.txt", "rb+") as file:
#    print(file.read())
   
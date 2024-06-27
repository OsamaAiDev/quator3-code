from typing import List, Any

names: List[Any] = ["osama", "bilal", "arsahd"]

for name in names:
    # print(name)
    break

# print(name)

# old way to perform same operation

# start: int = 0

# while start < len(names):
#     print(names[start])
#     start += 1

# perform operation on elements
    
# for name in names[:2]:
#     print(f'Welcome dear {name.title()}')

# database: List[tuple[str, str]] = [("osama", "123"),("osama", "123"),("osama", "123")]

# for row in database:
#     # unzip
#     name, password= row
#     print(f"Hello your name is {name} and passwod {password}")

    
data_base : list[tuple[str, str]] = [("osama", "123"),
                                     ("qasim", "234"),
                                     ("zia", "1243")
                                     ]
# input_user_name = input("Enter user name")
# input_user_password = input("Enter user password")

# for row in data_base:
#     # unzip
#     user_name, password = row

#     if(user_name == input_user_name and password == input_user_password):
#         print("Valid User")
#         break
# else:
#     print("Username Not Found Or Invalid UserName")

# un necessary indentation cause an error in python

#  print("hello")
    
# Numbers with loop generator func does not run its self we have to perform iteration
# range(start, end, step)
    
# numbers = range(10)
# print(numbers)

# for number in numbers:
#     print(number)

# numbers: List[int] = list(range(1,11))
# print(numbers)

# enumerate generator func map index with item

# persons : list[str] = ["osama", "arshad"]
# list(enumerate(persons))

# for index, person in enumerate(persons):
#     print(index, person)

# numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(max(numbers))

# tuple is immutable we cannot append and update items

my_tuple: tuple[Any] = (1,2,(1,2), "1")

print(my_tuple[2])

another_tuple: tuple[Any] = my_tuple[:] # deep copy
print(another_tuple)
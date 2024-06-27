from typing import Any, List

numbers: List[Any] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(numbers[:]) # if we not specify any return return whole list
# print(numbers[::]) # if we not specify any return return whole list
# print(numbers[-1:-5:-2]) # for negative indexing step value is imp otherwise return empty list

#list func perform iteration on iterative data type
# print(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

# print list in reverse order

# print(numbers[::-1])

# list is mutable in python

# numbers[0] = 100
# agr index exist nai krta tu error is tarha sa element add nai kr sakta hn list ma 
# agr index exist krta h tu update kr da ga value

# numbers[10] = 12 # index error we can't add item if this index isn't exist in list

# print(numbers)

# del delete krna ka bd return nai krta h
# names : list[Any] = ["osama", "arshad"]
# delete_value = del names[0] # error
# del names[0]
# print(names)

# a : str = print("Hello") # non return func

# print(a)

# list_methods =  [i for i in dir(list) if "__" not in i]
# print(list_methods)

# help

# display the documentation of functions, class, module or object or kws.
a: int = 12
# help(a) 

# show all the kw in python
# help("keywords")

# show all the modules in python
# help("modules")
# help("del")

# show all the symbols we can use in python

# help("symbols")
# help("+=")
# help(print)

# pop method remove and return last item if we pass index no then remove val from that index

names: List[Any] = ["osama", "bilal", "kaka"]

removed_item: str = names.pop(0)
# print(names)

# append add one element at the end of list and it can take only one arg
names.append("atif")
# print(names)

# add element at specific index if index not exisit then add element at the last no error
names.insert(10, "akif")
# print(names)
# print(len(names))

#  del kw pore list delete kr da memeory sa is lia name erorr aye ga
# del names

# print(names)

# clear method all element delete kr da list sa pr list exist kre ge
names.clear()

# print(names)

# yaha copy by reference h shallow copy
a : list[str] = ["a", "e"]
b : list[str] = a
b[0] = "ps"

# print(a)
# print(b)

# copy method copy all the elements from the item and assign them to new list and return it

a : list[str] = ["a", "e"]
b : list[str] = a.copy() # deep copy
b[0] = "osama"

# print(a)
# print(b)

# count method count the no of occurrence of a specified item in list
names : list[str] = ["osama", "osama", "bilal"]
# print(names.count('osama'))


# extend method extend the list by adding the elements of another list
# extend method sirf ek argument leta ha agr string pass ke "ali" tu hr index sa char utha kr list ma add kre ga
owners : list[str] = ["osama", "osama", "bilal"]
employees : list[str] = ["zia", "qasim"]
owners.extend(employees)
# owners.extend("alif")
# print(owners)

# remove element with the help of text val and this func does not return anything it remove only 1st occurance
# agr element list ma na mila tu value error da ga
#  remove method sirf ek argument la ga
# owners : list[str] = ["osama", "osama", "bilal"]

# print(owners.remove("osama"))
# print(owners)

# find index no with the help of text it return 1st match index no
# we can also pass start searching index as a second argument
# agr element na mila tu value error
owners : list[str] = ["osama", "osama", "bilal"]

print(owners.index("osama"))
print(owners.index("osama",1))

# reverse order ma print kr da ga
names : list[str] = ["kake", "osama", "bilal"]
names.reverse() # in-memory = change real data

# sort elements in ascending order
names : list[str] = ["kake", "osama", "bilal"]
names.sort() # in-memory = change real data
print(names)

# sort elements in descending order
names : list[str] = ["kake", "osama", "bilal"]
names.sort(reverse=True) # in-memory = change real data
print(names)



# list ma index pr val store hoti hn ya nai pta kis index pr kia val h wo name h id h etc

# set pr iteration perform  hoti h or index basis pr value access nai kr sakta
# set duplicate data remove kr deta ha

import pprint
from typing import Dict, Optional, Union


scores: set = {2,3,567,56,78,2,3}
# print(scores)

# type alias define custom data type

Key = Union[str, int]
Value = Union[str, float, list, tuple]

my_dict: Dict[Key, Value] = {"name": "osama",
                             "age": 27,
                             "id": 1,
                             "scores": [22, 33, 44,48]}
# access value

# print(my_dict["name"])

# update value

# my_dict["age"] = 26

# print(my_dict["age"])

# add new key,value

# my_dict["color"] = "brown"



# print(my_dict)

dictionary_methods = [i for i in dir(my_dict) if "__" not in i]
# print(dictionary_methods)
# pprint.pprint(my_dict)

abc : set = {1,2,3,2,2,2,1}
# print(abc)
# xyz : list[int] = list(abc)
# print(xyz)

# for a in abc:
#     print(a)

# agr key exists nai krti tu key error aye ga
# print(my_dict["abc"])

# is lia get method use kre ga is sa run time error nai aye ga
# agr key exisit nai krti tu none return kre ga second parameter ma bata bhe sakta hn agr key na tu ya print krna

# print(my_dict.get("abc", "key not found"))

# return all the keys
# all_keys = my_dict.keys()
# print(all_keys, type(all_keys))
# all_values = my_dict.values()
# print(all_values, type(all_values))
# all_items = my_dict.items()
# print(all_items, type(all_items))




# Key = Union[int,str] # create custom type
# Value = Union[int, str, list, dict, tuple, set]

# data : Dict[Key,Value] = {
#                         "fname":"Muhammad Aslam",
#                         "name":"Muhammad Qasim",
#                         "education": "MSDS"}




# for k,v in data.items():
#     print(k,v)


# print({v:k for k,v in my_dict.items()})

a : int = 7
b : int = 9

a, b = b, a # shuffle

print(a,b)

keys : list[str] = ['id','name','fname','course']
bio_data : Dict[str, str | int] = {}

bio_data = bio_data.fromkeys(keys)
# print(bio_data)

another_dict: Dict[str, int] = {"ff":1}

# dict ke pore key val delete kr ka ya keys add kr da ga
another_dict = another_dict.fromkeys(keys)
print(another_dict)
# TypedDict introuducce in python 3.8 use to the structure of a dictionary

from typing import Dict, TypedDict, NotRequired, Required, Union

class Person(TypedDict):
    name: str
    id: int
    roll_no: NotRequired[int]

person: Person = {"name": "osama", "id": 1, "roll_no": 12}

# print(person)

# Another way to create typeDict
# total false kr dn ga sare key optional ho jaye ge
# agr ma chah raha hn sirf specific key is required ho tu required use kro ga
Vote = TypedDict("Vote", {"for": str, "against": Required[str]}, total= False)

my_vote: Vote = {"against": "nawaz"}

my_dict: Dict[str, str] = {"name": "osama"}
# key is must in pop method sirf value return kre ga deleted item ke
# print(my_dict.pop("name"))

# pop item last item key,val remove kr ka tuple ke form ma return kr de ga 
# removed_item: tuple = my_dict.popitem()

# agr key exist nai krti tu add kr da ga or us ke val return kra ga agr exist krti h key tu us ke val return kr da add nai kre ga
a: str = my_dict.setdefault("name2", "hello")
# print(a)
# print(my_dict)

# update method sa multiple key ke val ko update kr sakta hn or sath ma new bhe add kr sakta hn

data1: Dict[str, Union[str, int]] = {"name": "osama", "age": "27", "id": 1}
data2: Dict[str, str] = {"name": "chal", "edu": "bsc"}
data1.update(data2)
# print(data1)
# data1["id"] += 2
# print(data1)

# convert dic to json obj

import json

data: Dict[str, Union[str, int]] = {"name": "osama", "age": "27", "id": 1}
json_data: str = json.dumps(data)
print(json_data, type(json_data))







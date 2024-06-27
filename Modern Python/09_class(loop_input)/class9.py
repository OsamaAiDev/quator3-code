import sys

# print("Line 1")
# print("Line 2")
# print(sys.argv)

my_set: set = {1,2,3,4,5,6,7,8,9,10}


# for no in my_set:
#     print(no)

# loop work on iterativate data type 
# list, tuple, dict, str, set/

# my_tuple: tuple[int] = (1, 2, 3, 4) # error

from typing import Literal

# Change the type annotation to match the tuple structure
my_tuple1: tuple[Literal[1], Literal[2], Literal[3], Literal[4]] = (1, 2, 3, 4)

# Or change the tuple structure to match the type annotation
my_tuple: tuple[int, int, int, int] = (1, 2, 3, 4)


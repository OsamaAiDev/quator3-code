# Union type meaans multiple data type ma sa single value assign krna chah rahe hn varaibale ko

from typing import List, Union

# my_score: Union[int, float, str, None] = input("Enter your score")

# ma pipe symbol bhe use kr sakta hn union ke jaga

my_score: int | float | str | None = "1200"

# we can also define our own custom type called type alias

percentage_type = Union[int, float]

# my_percentage: List[percentage_type] = input("Enter your percentage")

# we have a func called zip use to combine same length lists
# same index ka elements ek dosra ka sath combine ho jata hn
# return ek tuple krta ha

percentages = [33, 34, 80, 70, 60]

grades = ["A", "B", "C", "D", "E", "F"]

# for per in zip(percentages, grades):
#     print(per)


grad_per = list(zip(percentages, grades))
print(grad_per)

# sorted func by default first column ke base pr sorting krta ha agr kese or column ke base pr krne ha tu us ka lia key ka parameter
# h jo lambda func la ga or is ke body ma  bata dn ga kis column ke base pr kro agr descending order ma chahia data
# to reverse parameter ke value true kr dn ga.

# grad_per = sorted(grad_per, key=lambda x: x[0], reverse=True)

# print(grad_per)


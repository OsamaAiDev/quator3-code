# generator func

from ast import Tuple
from typing import Callable, Generator, Iterator, List, Sequence
import sys

def creator():
    my_list: List[int] = []
    i: int = 1
    while i <= 200:
        my_list.append(i)
        i += 1
    return my_list

my_list: List[int] = creator()
# sys means sys system 1656 bytes la rahe h memory me list 200 int save kia hn memory ma
# print(sys.getsizeof(my_list))

# is he tarha agr operation perform krna ha tu element pr kra ga ya efficient way nai h memory bht use ho rahe h

new_list: List[int] = [i+10 for i in creator()]
# print(new_list)

# yield point pr func stop ho jaye ga first call ma phr dobara call kre ga phr yield pr stop previous step remeber rhk ta h 
# generator func
# jb 200 no generate krna ha tu ek sath q store kr dn pehla sa memory ma is lia list use nai krta generator ma
# next sa next iteration pr jaye ga.

# is tarha sa efficient memory manage ho ge jb chahia tb he generate kro

# ya ek generator obj return krta ha
def generator_no2() -> Generator[int, None, None]:
    i: int = 1
    while i <= 200:
        yield i
        i += 1
def generator_no() -> Iterator[int]:
    i: int = 1
    while i <= 200:
        yield i
        i += 1

# print(generator_no())
x: Iterator[int] = generator_no()
# print(next(x))
# list 2 sa start ho ge q k already one time chal chuka ha
# print(list(x))


"""
decorator function takes another func as an argument and returns a function is lia varaible ma assign kr dn ga
main func execute krna sa pehla bad ma koi km krna chah raha hn is lia use krta hn is ko. Is ma main func ko wrap kr deta
hn dosra func ma us ko decorate kr deta hn enhance kr deta hn jese transaction sequence of step ha.
"""

def hello_decorator(func):
    def wrapper():
        print("transaction started")
        func()
        print("transaction completed")
    return wrapper

@hello_decorator
def hello():
    print("processing transaction")

# hello call kia is na decorator func ko call kia us ma jo bhe statements thi wo call ho gai
# hello()
# yaha manually kia ha func pass or phr manually call kia h
# hello1 = hello_decorator(hello)
# hello1()


"""
recursion means func call its self again and again in its body
"""

"""
higher order func take another func as an argument or return a func called higher order func
In python also trated as object
"""

# ex 1
# def lower(text: str) -> str:
#     return text.lower()

# def hello(func)->None:
#     text = func("hello")
#     print(text)

# hello(lower)

# ex 2

"""
divisor func ko argument 2 pass kia h tu wo x parameter ma a jaye ga or ya 2 yaha rahe ga jb tk program exec ho raha ha 
ya phr hm re assign nai krta hm skip kr raha hn divident func ko q k usa abhe call nai kr raha hn hm return kr raha hn divident
func is lia is ko ek variable ko assign kr dia ha or hm variable call kr sakta hn agr us ka pass func ka memory address ha
"""
# def divisor(x: int):
#     def divident(y: int):
#         return y/x
#     return divident

# divider = divisor(2)
# print(divider(9))


# the func that pass an argumenet to another func called callback func and the func that accept it as an argument called
# higher order func

"""
fun create kia h do cheza la ga as an argument name and callback func or phr us callback func ko call kia h
higher order func ma

"""

def tone_inspired(name: str) -> str:
    return f"your work has inspired me alot {name}"

def greet_me(name: str, callbackfunc)->None:
    greeting: str = callbackfunc(name)
    print(greeting)

greet_me("osama", tone_inspired)

# map example
# map func takes two things callback func and an input 
# maps perform iteration on all list element one by one take first item apply str.lower method and so on...

# names_with_small_caps: List[str] = list(map(str.lower, ["Osama", "BILAL", "Arshad"]))
    
# def add_two_numbers(no1: int, no2: int) -> int:
#     return no1 + no2

# print(add_two_numbers(1,2)) #here 1 and 2 are called positional arguments
# print(add_two_numbers(no1= 1,no2=2)) #here 1 called keyword arguments agr kw args use kia ha tu bake sub bhe kw he hona chahia postional kre ga tu error

# optional parameter
# optional parameter must be last in the parameter list

# def add_two_numbers(num1: int, num2:int = 0) -> int:
#     print(num1, num2)
#     return num1 + num2

# add_two_numbers(7,2)


# lambda func one line anonymous func only take memory when exec and destroy from memory after execution
# we cannot use return statement inside lambada

add_numbers: Callable[[int, int], int] = lambda no1, no2: no1+no2


# https://stackoverflow.com/questions/33833881/is-it-possible-to-type-hint-a-lambda-function

data : list[int] = [1,2,3,4,5,6,7,8,9,10]
data = list(map(lambda x: x**2, data))

# pass unlimited arguments
# unlimited positional arguments

def abc(*nums: int):
    print(nums, type(nums))
    total = 0
    for n in nums:
        total += n

    return total


abc(1,2,3,3,5,6)

# here a,b argument is req
def my_function(a, b, *abc, **xyz):
    print(a,b, abc, xyz)

my_function(1,2, 7,9,9,9, c=20, d= 30, x=100)


from typing import Dict


# def greet(**xyz: str) -> None:
#     print(xyz, type(xyz))

# Corrected function call
# greet(country='pakistan')

from typing import Dict

def greet(**xyz: str) -> None:
    print(xyz)

greet(a="pakistan", b='China')

# factorial recursion func here we define the condition so func will not become infinite

def factorial(n: int) -> int:
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
    

result: int = factorial(5)
# output
"""
5 * factorial(4) => return 5 * 24
4 * factorial(3)  => 4 * 6
3 * factorial(2) => 3 * 2
2 * factorial(1) =>  2 * 1
"""
print(result)
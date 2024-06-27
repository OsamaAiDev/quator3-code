from  class01_q5 import main

# test 1
def test_function1():
    r = main.my_first_func()
    assert r == "Hello world"

# test 2
def test_function2():
    r = main.my_first_func()
    assert r != "Pakistan"

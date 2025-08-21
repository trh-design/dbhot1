#!/usr/bin/python3

def other():
    num = 10
    def inner():
        nonlocal num
        num = 100
        print(num)
    inner()
    print(num)
other()
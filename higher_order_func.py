#!/usr/bin/env python
def calc(a, b, f):
    return f(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print calc(5, 9, add)
print calc(5, 9, subtract)
print calc(5, 9, multiply)
print calc(5, 9, divide)

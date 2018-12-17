#!/usr/bin/env python
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print my_abs(-1)
print my_abs(0)
print my_abs(1)
# print my_abs('abc')
# print my_abs(None)

def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x, x
    else:
        return x, -x

print my_abs2(-1)
print my_abs2(0)
print my_abs2(1)
# print my_abs2('abc')
# print my_abs2(None)

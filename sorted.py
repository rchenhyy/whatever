#!/usr/bin/env python
def cmp_ignore_case(x, y):
    return cmp(x.upper(), y.upper())

list = ['Abc', 'efg', 'EDC', 'HHH', 'aaa', '...']
print list
print sorted(list)
print sorted(list, cmp_ignore_case)

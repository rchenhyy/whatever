#!/usr/bin/env python

def str2int(s):
    def fn(a, b):
        return a * 10 + b
    return reduce(fn, map(int, s))

print str2int('01237890')

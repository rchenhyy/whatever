#!/usr/bin/env python
def lazy_calc(n):
    func_list = []
    for i in range(n):
        # use an extra arg-binding function to make enclosure f different
        def ff(j):
            def f():
                return j * j
            return f
        func_list.append(ff(i))
    
    return func_list

list = lazy_calc(10)
for f in list:
    print f, ':', f()   # invoke f

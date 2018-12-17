#!/usr/bin/env python
def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['', 'AAA', '', None, '1', '1.23', 'abc'])

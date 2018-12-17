g = (i ** 2 for i in range(10, 20))
for i in g:
    print(i)

nested = [[11, 22, 33], [44], [55, [666], [777, [8888]]], 1, 2, 3, 4]


def flatten(ll):
    if isinstance(ll, list):
        for l in ll:
            for i in flatten(l):  # just to consume the generator, yield operator succeeds another
                yield i
    else:
        yield ll


g = flatten(nested)
for i in g:
    print(i)

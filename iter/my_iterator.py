class MyIterator:
    def __init__(self, start, end):
        self._next = start
        self._end = end

    def __iter__(self):
        return self

    def next(self):
        if self._next > self._end:
            raise StopIteration()
        n = self._next
        self._next += 1
        return n


for i in MyIterator(0, 10000):
    print i

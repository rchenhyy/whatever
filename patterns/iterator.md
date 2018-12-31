## 迭代器模式

> In object-oriented programming, the iterator pattern is a design pattern in which an iterator is used to traverse a container and access the container's elements. The iterator pattern decouples algorithms from containers; in some cases, algorithms are necessarily container-specific and thus cannot be decoupled.

#### 基本理解

* 对容器或任意可迭代对象的通用迭代行为的抽象；独立的迭代状态；内置的语法支持

#### 几个目标

* 通用迭代行为，算法无关
* 简单的迭代模式/协议

#### 相关讨论

* 迭代器（Iterator） vs 可迭代对象（Iterable）
* 迭代器（Iterator） vs 生成器（Generator）
* 关于并发修改冲突
* 不可重复的迭代
* 无穷的迭代
* 函数式编程
* 流式计算
* 懒加载
* 迭代工具包（itertools）

#### 应用场景

* 集合类框架
* 数据流

#### 实现

1. 基于内置迭代器协议

    ```python
    # an iterable class, holding data from a file
    class DataSet(object):

        def __init__(self, filename, lines=None, id=None):
            self.id = id or 0
            self.filename = filename
            self.lines = lines
            if not self.lines:
                with open(self.filename, 'r') as f:
                    self.lines = f.readlines()
    
        def __repr__(self):
            return 'DataSet(id={!r}, filename={!r}, size={!r})'.format(self.id, self.filename, len(self))
    
        def __len__(self):
            return len(self.lines)
    
        # implements the __iter__ method to become an iterable class; here we simply return an iterator of a list
        def __iter__(self):
            # @see protocol about an Iterator(the next/__next__ method, and the StopIteration Exception)
            return iter(self.lines)
    
        def __getitem__(self, item):
            if isinstance(item, slice):
                # TO.DO. avoid empty data set
                return DataSet(id='%s-%s' % (item.start or 0, item.stop or len(self)),
                               filename=self.filename, lines=self.lines[item])
            return self.lines[item]
         
     
    # suppose there is a file named 'test.txt' in current dir
    for item in DataSet('test.txt'):
        print item
    for item in DataSet('test.txt')[:10]:
        print item
    ```

2. 基于生成器

    ```python
    # a generator function is analogous to an iterable class, while a generator is analogous to an iterator
    def fibonacci(end=None):
        a, b = 1, 1
        while True:
            yield a    # function with a yield keyword is a generator function
            if end is not None and b >= end:
                break
            a, b = b, a + b
         
   
    for num in fibonacci(100): # call the generator function to provide a generator/iterator
        print num
    ```
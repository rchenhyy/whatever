## 单例模式
> In software engineering, the singleton pattern is a software design pattern that restricts the instantiation of a class to one object. This is useful when exactly one object is needed to coordinate actions across the system. The concept is sometimes generalized to systems that operate more efficiently when only one object exists, or that restrict the instantiation to a certain number of objects. The term comes from the mathematical concept of a singleton.

#### 基本思路
* 控制/收敛实例化的过程
* 缓存唯一实例

#### 几个目标
* 单实例
* 懒加载
* 可复用
* 线程安全

#### 相关讨论
* 对象相等性问题
* 不可变类型
* 无状态
* 与单例有关的语言机制：模块加载、类定义、...

#### 应用场景
* 无状态服务
* 全局配置

#### 几种实现方式

1. 面向过程 - 模块变量


    class Singleton(object):
        pass


    INSTANCE = Singleton()  # defined as a module level variable; supposed to be the only instance, but no guarantee


2. 面向过程 - 类方法1


    class Singleton(object):
        pass
        
        @classmethod
        def instance(cls, *args, **kwargs): # using factory method; to initialize instance conditionally
            if not hasattr(Singleton, '_instance'):
                Singleton._instance = Singleton(*args, **kwargs)
            return Singleton._instance


3. 面向切面 - 类装饰器

        
    @singleton  # using class decorator
    class Foo(object):
        pass
    
    
    def singleton(cls):
        _instances = {} # holding the only instance for each singleton class
        
        def _singleton(*args, **kwargs):
            if cls not in _instances:
                _instances[cls] = cls(*args, **kwargs)
            return _instances[cls]
        return _singleton   # warnings: the returned valued is a function; attrs in cls will be lost


4. 面向对象 - 类方法2（与类实例化有关的几个方法：__new__, __init__, __call__）


    class Singleton(object):
        '''
        the process of instantiation in python: meta_cls.__call__ -> cls.__new__ -> cls.__init__
        using __new__ method of a class (meta_cls: type, cls: Singleton)
        '''
        
        def __new__(cls, *args, **kwargs):
            if not hasattr(Singleton, '_instance'):
                Singleton._instance = Singleton(*args, **kwargs)
            return Singleton._instance


5. 面向对象 - 元类


    class SingletonType(type):
        '''
        the process of instantiation in python: meta_cls.__call__ -> cls.__new__ -> cls.__init__
        using __call__ method of a meta class (meta_cls: SingletonType, cls: Singleton)
        '''        
        
        # cls is any instance of SingletonType; cls(...) = SingletonType.__call__(cls, ...)
        def __call__(cls, *args, **kwargs):
            if not hasattr(cls, '_instance'):
                # delegate to super type (typically <type 'type'>)
                cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
            return cls._instance
            
            
    class Foo(metaclass=SingletonType):
        pass

        
* 线程安全版的单例模式（使用双重检查锁：线程安全 && 仅第一次初始化时加锁）


    import threading
    
    class SingletonType(type):
        # using a shared lock to ensure thread-safety; will be shared among different singleton types
        _instance_lock = threading.Lock()
        
        def __call__(cls, *args, **kwargs):
            # double-check locking
            if not hasattr(cls, '_instance'):
                with _instance_lock:
                    if not hasattr(cls, '_instance'):
                        cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
            return cls._instance
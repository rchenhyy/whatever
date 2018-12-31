## 代理模式

> In computer programming, the proxy pattern is a software design pattern. A proxy, in its most general form, is a class functioning as an interface to something else. The proxy could interface to anything: a network connection, a large object in memory, a file, or some other resource that is expensive or impossible to duplicate. In short, a proxy is a wrapper or agent object that is being called by the client to access the real serving object behind the scenes. Use of the proxy can simply be forwarding to the real object, or can provide additional logic. In the proxy, extra functionality can be provided, for example caching when operations on the real object are resource intensive, or checking preconditions before operations on the real object are invoked. For the client, usage of a proxy object is similar to using the real object, because both implement the same interface.

#### 基本理解

* 代理着重于控制对资源的访问，被代理的对象类型不限：一个网络连接、一个大对象、一个受保护的资源...
* 代理可以做单纯的转发（forwarding），或者提供额外的逻辑
* 代理和被代理者接口一致

#### 几个目标

* 控制对资源的访问
* 使用方无感知
* 动态逻辑
* 优化访问

#### 相关讨论

* 代理 vs 委托
* 按实现方式分类：1）静态代理 2）动态代理
* 按使用场景分类：1）远程代理 2）虚拟代理 3）保护代理 4）智能代理（引用代理？！）

#### 应用场景

* RPC框架
* ORM框架
* 访问控制
* 资源管理

#### 实现（结合具体场景）

1. 静态代理

    ```python
    class Query(object):
        def select(self, name):
            pass
        
        def update(self, name, value):
            pass
        
        def insert(self, name, value):
            pass
        
        def delete(self, name):
            pass
     
    # target class
    class NormalQuery(Query):
        def select(self, name):
            print 'select', name
        
        def update(self, name, value):
            print 'update', name, value
        
        def insert(self, name, value):
            print 'insert', name, value
        
        def delete(self, name):
            print 'delete', name
 
    # proxy class, has the same interface(Query) as the target class
    class NoDeleteQuery(Query):
 
        def __init__(self, target): # pass a real object(target) to the constructor
            self.target = target   # type: Query
 
        def select(self, name):
            return self.target.select(name)
        
        def update(self, name, value):
            return self.target.update(name, value)
        
        def insert(self, name, value):
            return self.target.insert(name, value)
        
        def delete(self, name):
            raise NotImplementedError(message='Delete op not allowed!')
    ```

2. 动态代理

    ```python
    # Dynamic proxy in python compared with java: https://www.v2ex.com/t/459342
    # proxy class, with no definite interface(in agreement with specific protocol, instead)
    class NoDelete(object):
       
        def __init__(self, target):
            self.target = target
        
        # analogous to the InvocationHandler in Java Dynamic Proxy
        def __getattr__(self, item):
            attr = getattr(self.target, item)
            
            if callable(attr) and item == 'delete':
                # guard of the delete operation 
                def no_delete(*args, **kwargs):
                    raise NotImplementedError(message='Delete op not allowed!')
                return no_delete
            else:
                return attr
    ```

---

* 远程代理

    ```python
    class Client(object):
        # TODO
        pass
    ```
    
* 虚拟代理 - 延迟加载 & 缓存

    ```python
    # attr descriptor
    class LazyProperty(object):
        # TODO
        pass
    ```
    
*. 保护代理

    ```python 
    # @see NoDelete
    ```
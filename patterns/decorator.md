## 装饰器模式

> In object-oriented programming, the decorator pattern is a design pattern that allows behavior to be added to an individual object, dynamically, without affecting the behavior of other objects from the same class. The decorator pattern is often useful for adhering to the Single Responsibility Principle, as it allows functionality to be divided between classes with unique areas of concern. The decorator pattern is structurally nearly identical to the chain of responsibility pattern, the difference being that in a chain of responsibility, exactly one of the classes handles the request, while for the decorator, all classes handle the request.

#### 基本理解

* 不改变原类，使用一个包装类，动态地给一个类的对象添加一些额外的职责（通常是在外围/切面）；比生成（静态）子类更为灵活

#### 几个目标

* 运行时修饰/添加行为
* 无需子类化
* 不跳过/屏蔽原对象的行为

#### 相关讨论

* 多层装饰 vs 多层继承
* 装饰器模式 vs 代理模式（尤其动态代理）

#### 应用场景

* IO流
* UI组件

#### 实现

1. 使用猴子补丁+装饰器函数

    ```python
    from pyutil.springdb import SpringDBClient
    
    ABASE_CONF = {
        'China-North-LF': {
            'zone': 'online',
            'cluster': "abase_content_nearline",
            'table': "main",
        },
        'Aliyun_SG': {
            'zone': '/opt/tiger/ss_conf_aliyun_sg/ss',
            'cluster': 'abase_hawk_aliyun_sg',
            'table': 'review_pipeline',
        },
        'Aliyun_VA': {
            'zone': '/opt/tiger/ss_conf_maliva/ss',
            'cluster': 'abase_hawk_mva',
            'table': 'review_pipeline',
        }
    }
    
    
    def _get_abase_client(dc='China-North-LF', **kwargs):
        abase_conf = ABASE_CONF.get(dc, {})
        cluster = abase_conf.get('cluster')
        table = abase_conf.get('table')
        zone = abase_conf.get('zone')
    
        SpringDBClient.set_zone(zone)
        _springdb_client = SpringDBClient(cluster, table, **kwargs)
        return _springdb_client
    
    abase_client_lf = _get_abase_client('China-North-LF')
    abase_client_sg = _get_abase_client('Aliyun_SG', socket_timeout=5, socket_connect_timeout=3, find_connection_timeout=3)
    abase_client_va = _get_abase_client('Aliyun_VA', socket_timeout=5, socket_connect_timeout=3, find_connection_timeout=3)
    abase_client = abase_client_lf
    
    
    # wrap abase functions, to add additional logic of retrieving results from other clients
    def _wrapped(func, name):
        def _func_with_retry(*args, **kwargs):
            rs = func(*args, **kwargs)
            if rs:
                return rs
            # if not rs, try other clients
            try:
                backups = [abase_client_sg, abase_client_va]
                for client in backups:
                    rs = getattr(client, name)(*args, **kwargs)
                    if rs:
                        return rs
            except:
                pass
    
        return _func_with_retry
    
    
    abase_client.get = _wrapped(abase_client.get, 'get')
    abase_client.scanrow = _wrapped(abase_client.scanrow, 'scanrow')    # add additional behavior at runtime
    ```

2. 使用装饰器类

    ```python
    class ClientDecorator(object):
    
        def __init__(self, client, backups, decorated_methods):
            self.client = client
            self.backups = backups
            self.decorated_methods = decorated_methods
    
        def __getattr__(self, item):
            attr = getattr(client, item)
            if callable(attr) and item in self.decorated_methods:
                return self._wrapped(item, attr)
            return attr
        
        def _wrapped(self, name, func):
            def _func_with_retry(*args, **kwargs):
                rs = func(*args, **kwargs)
                if rs:
                    return rs
                # if not rs, try other clients
                try:
                    for backup in self.backups:
                        rs = getattr(backup, name)(*args, **kwargs)
                        if rs:
                            return rs
                except:
                    pass
                    
            return _func_with_retry
            
        # any other extensional methods here
        def get_with_default(self, default, *args, **kwargs):
            rs = self.get(*args, **kwargs)
            return rs if rs is not None else default
    
    
    abase_client = object()   # suppose this is an abase client
    abase_client_backups = (object(), object())
    client = ClientDecorator(abase_client, abase_client_backups, ('get', 'scanrow'))    # add additional behavior at runtime
    ```
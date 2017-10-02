#API Reference  api 参考
----------------------


The official Redis command documentation does a great job of explaining each command in detail.

redis-py exposes two client classes that implement these commands.

The [StrictRedis] class attempts to adhere to the official command syntax. There are a few exceptions:



官方文档为每一个Redis操作命令已经做了非常详尽的解释，在这里不过多介绍,如需要了解，可以去官方文档查看(挖坑！)
redis-py 创建了两个用来执行REDIS数据库操作的两个类，[StrictRedis] 类尝试与官方提供的操作接口最大化拟合
下面有一部分解释：

[SELECT] : Not implemented. See the explanation in the Thread Safety section below.

处于线程安全的原因，并没有提供SELECT语句的替代接口，在后面会有详细的解释

[DEL]: 'del' is a reserved keyword in the Python syntax. Therefore redis-py uses 'delete' instead.

del 作为 python中的关键字，所以 REDIS 中相应操作接口替换为 delete

CONFIG GET|SET: These are implemented separately as config_get or config_set.

[GET]和[SET] 可以利用 [config_get] 和 [config_set] 调用

MULTI/EXEC: These are implemented as part of the Pipeline class. The pipeline is wrapped with the MULTI and EXEC statements by default when it is executed, which can be disabled by specifying transaction=False. See more about Pipelines below.

[MULTI]/[EXEC] 作为 [Pipeline] 类的一部分，[Pipeline] 类将[MULTI]/[EXEC] 做了封装处理，并且在类创建的时候自动被调用
这项功能可以在创建时声明 transaction=False. 详情见下方的 [Pipeline] 介绍

SUBSCRIBE/LISTEN: Similar to pipelines, PubSub is implemented as a separate class as it places the underlying connection in a state where it can't execute non-pubsub commands. Calling the pubsub method from the Redis client will return a PubSub instance where you can subscribe to channels and listen for messages. You can only call PUBLISH from the Redis client (see this comment on issue #151 for details).
与之前的 [Pipeline] 类似， [PubSub] 作为一个独立的底层链接类，在

SCAN/SSCAN/HSCAN/ZSCAN: The *SCAN commands are implemented as they exist in the Redis documentation. In addition, each command has an equivilant iterator method. These are purely for convenience so the user doesn't have to keep track of the cursor while iterating. Use the scan_iter/sscan_iter/hscan_iter/zscan_iter methods for this behavior.

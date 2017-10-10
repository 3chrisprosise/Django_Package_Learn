# REDIS 数据库常用命令
-----------------------
#### 登陆命令  redis-cli  -h 10.55.91.107 -p 6379 -a 123456
 1. APPEND 字符串追加，没有则创建，返回操作执行完毕后的长度

 2. AUTH 'password'  为服务请求设置密码

 3. BGREWRITEAOF AOF重写由 Redis 自行触发，BGREWRITEAOF 仅仅用于手动触发重写操作。

 4. BGSAVE 后台保存DB。会立即返回 OK 状态码。无论是否完成 如果操作成功，可以通过客户端命令LASTSAVE来检查操作结果。

 5. CLIENT LIST 返回所有连接到服务器的客户端信息和统计数据。
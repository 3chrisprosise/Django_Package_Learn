from django.shortcuts import render, render_to_response
import json
from django.conf import settings
from django.core.cache import cache
from django.utils.timezone import deactivate
from django_redis import get_redis_connection
import redis
from Django_Package_Learn import settings

REDIS_HOST = settings.REDIS_HOST
REDIS_PORT = settings.REDIS_PROT
REDIS_DB = settings.REDIS_DBS
REDIS_PASSWD = settings.REDIS_PASSWD



def test_DJredis(req):
    '''
    use Django-redis
    :param req: 
    :return: 
    '''
    if req.method == "GET":
        new_keyvalue = cache.set("name1", '1111', timeout=20)
        cache.set("astring", '1111', timeout=20)   # timeout 为 None 时 永不更新
        # time_out = cache.ttl("astring")  # 获取超时时间
        cache.persist("astring")  # 设置永不更新
        # time_out = cache.ttl("astring")
        cache.expire("astring", timeout=5)  # 重新设置超时时间
        time_out = cache.ttl("astring")
        # django-redis 支持使用全局通配符的方式来检索或者删除键.
        keys = cache.keys("astring")  # 返回一个list，所有匹配的值
        delete_number = cache.delete_pattern("name1")  # 删除键和值，并且返回删除数量  当用通配符号时可能不止删除一个
        change_key = cache.set("astring", "value1", nx=True)# 创建新的key 和 value，当且仅当 key 不存在，返回值为是否创建成功，None代表键值已经存在

        r = get_redis_connection("default")  # Use the name you have defined for Redis in settings.CACHES
        connection_pool = r.connection_pool
        print("Created connections so far: %d" % connection_pool._created_connections)   # 查看当前连接数

        delete_number = cache.delete_pattern("*")

        # 至此 ，Django_redis 的全部常用功能没了
        return render_to_response('Redis.html', {'time_out': time_out, 'keys': keys, 'delete': delete_number})


def test_redis(req):
    R = redis.Redis(host="10.55.91.107", port= 6379, password="123456")
    # result = R.ping()
    # result = R.getset('a','b') # 没有则创建
    # result = R.getbit('a',3)
    result = R.mget('a','b','c','d','e')
    result = R.setex('aa','aa',30)  # 这里的参数顺序与原版稍有不同
    ttl = R.ttl('aa')
    value = R.get('aa')
    R.set('a','a')
    ttl = R.setnx('a','aa')
    result = R.get('a')
    R.delete('a')
    value = R.setnx('a', 'aa')
    status = R.get('a')

    R.flushdb()
    result = R.set('a','aaaaa')
    ttl = R.get('a')
    value = R.setrange('a', 3,'bbb')  # 替换部分值
    status = R.get('a')

    R.flushdb()
    result = R.set('a','aaaaaaaaa')
    ttl = R.get('a')
    value = R.strlen('a')
    status = R.strlen("NoExist")  # 不存在的值返回长度为0

    R.flushdb()
    result = R.mset({'a':'a','b':'b','c':'c','d':'d'})
    ttl = R.get('a')
    value = R.get('b')
    status = R.get('c')

    result = R.msetnx({'a': 'b', 'mysql': 'mysql', 'mongedb':'mongodb'})  # 这里由于 a 的存在导致了创建不成功，返回false
    ttl = R.get('a')
    value = R.get('mysql')
    status = R.get('mongedb')

    R.flushdb()

    result = R.msetnx({'a': 'b', 'mysql': 'mysql', 'mongedb': 'mongodb'})
    ttl = R.get('a')
    value = R.get('mysql')
    status = R.get('mongedb')   # 清空数据库之后就成功了

    R.flushdb()
    result = R.psetex('a',10000,'hello')
    ttl = R.pttl('a') # 以毫秒为单位查询生存时间 查询共用了两毫秒的时间
    value = R.get('a')
    status = R.flushdb()

    result = R.set('a','20')
    ttl = R.get('a')
    value = R.incr('a')  # 这里直接返回增加一后的值，如果不存在的值，默认为0
    status = R.get('a')

    R.flushdb()
    result = R.set('a','20')
    ttl = R.get('a')
    value = R.incrby('a',5)  # 自由设置增量
    value = R.incrbyfloat('a', 5.5)  # 自由设置增量,允许浮点数
    result = R.set('a', '20')
    value = R.decr('a')  # 自动减1 ，只能操作整形数字
    value = R.decr('a',2)  # 自动减2 ，自由设置减少的数值，只能减少整数
    value = R.incrbyfloat('a',-2.2)  # 可以用这种方法实现减少自定义的效果
    value = R.append('a','aa')  # 返回增加后的长度
    status = R.get('a')

    R.flushdb()
    # 开始操作哈希表
    result = R.hset('hash', {'name','id','likes'},{'Chris','0321','20'})
    ttl = R.ttl(R.hgetall('hash'))
    value = R.hget('hash','id')
    status =R.hkeys('hash')

    R.flushdb()
    result = R.hset('hash', {'name', 'id', 'likes'}, {'Chris', '0321', '20'})
    ttl = R.hdel('hash','name')  # 这边稍有不理解，为什么删除不掉？
    value = R.hgetall('hash')
    status = R.hkeys('hash')

    return render_to_response('Redis.html', {"result": result,"ttl": ttl, "value": value, "status":status})
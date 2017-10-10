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

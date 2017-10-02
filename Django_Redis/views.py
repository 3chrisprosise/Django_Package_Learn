from django.shortcuts import render, render_to_response
import json
from django.conf import settings
from django.core.cache import cache
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
        cache.set("astring", '1111', timeout=20)   # timeout 为 None 时 永不更新
        # time_out = cache.ttl("astring")  # 获取超时时间
        cache.persist("astring")  # 设置永不更新
        # time_out = cache.ttl("astring")
        cache.expire("astring", timeout=5)  # 重新设置超时时间
        time_out = cache.ttl("astring")
        # django-redis 支持使用全局通配符的方式来检索或者删除键.

        return render_to_response('Redis.html', {'time_out': time_out})

from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

from django.core.mail import send_mail

def Email(req):
    result = send_mail('Django邮件测试', u'请不要回复', '1337074512@qq.com', ['1079535307@qq.com'], fail_silently=False)
    # 收件人为一个列表，发送成功返回状态 1
    return HttpResponse(result)

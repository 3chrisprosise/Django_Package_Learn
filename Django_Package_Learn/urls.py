"""Django_Package_Learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from Django_Package_Learn import settings
from Django_Package_Learn.settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^editor/', include("Ckeitor_Learn.urls")),
    url(r'^all_auth/', include("All_auth.urls")),
    url(r'^email_sender/', include("Email_Sender.urls")),
    url(r'^redis/', include("Django_Redis.urls")),
    url(r'^wechat/', include("Wechat_Sdk.urls")),

    # Start Of Media URL
    url(r'^media/(?P<path>.*)$',  serve, {"document_root": MEDIA_ROOT}),

    # Start Of CK_editor url
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# coding:utf-8
"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
#from article import views
from article.views import *
from datetime import datetime
#import article
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home,name = 'home'),
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
    url(r'^archives/$', archives,name = 'archives'),
    url(r'^aboutme/$', about_me, name = 'about_me'),
    url(r'^tag/(?P<tag>\w+)/$', search_tag, name = 'search_tag'),
    url(r'^search/$',blog_search, name = 'search'),
    url(r'^feed/$', RSSFeed(), name = "RSS"),  #新添加的urlconf, 并将name设置为RSS, 方便在模板中使用url
]

"""site_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf (url 권한 위임)
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lotto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.index),
    path('hello/', views.hello, name='hello_main'),
    path('lotto/', views.index, name='index'), #/lotto
    path('lotto/new/', views.post, name='new_lotto'),
    path('lotto/<int:lottokey>/detail/', views.detail, name='detail'),
]
### 서로 다른 url에 서로 다른 함수들이 매칭됨(url 마다 매칭되는 함수) ###
### url.py에서 views.py로 파일이 옮겨 ###

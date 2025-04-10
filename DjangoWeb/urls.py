
from django.urls import path
from django.contrib import admin

#from DjangoProject.urls import urlpatterns
app_name = 'DjangoWeb'  # 声明一下路径

from .views.verify import showWIFIList,checkWIFI  # 引入你的视图函数
urlpatterns =[
    # 渲染WIFI展示页面
    path('showWifiList/', showWIFIList, name='showWifiList'),
    #检查WIFI的密码是否正确
    path('check/', checkWIFI, name='check'),
]
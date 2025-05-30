import json
import subprocess
from django.shortcuts import render
from django.http import JsonResponse

"""现在出现的问题是：在本地运行的话，是需要去先和远程服务器建立通信，然后在执行shell命令：nmcli device wifi list 
等获取之后再进行断开连接进行返回，"""



'''单纯的一个去获取模块上的WIFI列表去供给用户去进行选择'''

def showWIFIList(request):
    # 获取服务器上的WiFi
    # result2 = get_wifi_list()
    return render(request, "showWifiList.html", {"wifi_list": "111"})


def checkWIFI(request):
    if request.method == 'GET':
        pass




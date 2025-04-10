import json
import subprocess
from django.shortcuts import render
import paramiko
from django.http import JsonResponse

"""现在出现的问题是：在本地运行的话，是需要去先和远程服务器建立通信，然后在执行shell命令：nmcli device wifi list 
等获取之后再进行断开连接进行返回，"""


def get_wifi_list():
    wifi_list = []
    # 创建 SSH 客户端对象
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 自动接受未知主机
    client.connect('10.1.1.220', username='root', password='Das747880')
    stdin, stdout, stderr = client.exec_command('nmcli device wifi list')
    output = stdout.read().decode()
    lines = output.splitlines()
    for line in lines[1:]:
        parts = line.split()
        if len(parts) >= 7:
            wifi_list.append({
                'bssid': parts[0],
                'ssid': parts[1],
                'signal': parts[6],
                'security': parts[7] if len(parts) > 7 else 'None',
            })
    client.close()
    return wifi_list

'''单纯的一个去获取模块上的WIFI列表去供给用户去进行选择'''

def showWIFIList(request):
    # 获取服务器上的WiFi
    result2 = get_wifi_list()
    return render(request, "showWifiList.html", {"wifi_list": result2})


def checkWIFI(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        wifi_name = data.get('wifiName')
        wifi_password = data.get('wifiPassword')

        print(wifi_name)
        print(wifi_password)

        # 检查是否有 WiFi 名称和密码
        if not wifi_name or not wifi_password:
            return JsonResponse({"code": 400, "message": "WiFi 名或密码缺失"})

        # result = subprocess.run(
        #     ['nmcli', 'device', 'wifi', 'connect', wifi_name, 'password', wifi_password],
        #     capture_output=True,
        #     text=True
        # )

        # 打印命令输出，查看连接是否成功
        # print("查看result的值", result)
        # print("stdout:", result.stdout)
        # print("stderr:", result.stderr)

        # 检查命令的返回码来决定是否成功
        # if result.returncode == 0:
            # 如果 WiFi 连接成功，返回成功页面（可以根据需求调整）
            # return render(request, "success.html")
    #     else:
    #         # 如果连接失败，返回错误页面并显示错误信息
    #         return render(request, "404.html", {"error_message": result.stderr})
    #
    # else:
    #     return JsonResponse({"code": 405, "message": "仅支持 POST 请求"})

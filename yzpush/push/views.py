# coding:utf-8

from django.http import JsonResponse
import json


CONFIG = {
    'url': 'https://open.youzanyun.com/auth/token',
    'headers': {'Content-Type': 'application/json'}
}

myClientId = "f8aedf4734cadd7e83"  # 应用的 client_id
myClientSecret = "01b19295d9b729b4fa2e6f36969b5e3f" # 应用的 client_secret

# 定义功能
def recv_data(request):
    if request.method == 'POST':
        result_sucess = {"code":0,"msg":"success"}
        result_fail = {"code":0,"msg":"failed"}
        data = request.body
        print(type(data))
        #处理业务逻辑
        print("200 OK")
        return JsonResponse(result_sucess)
    else:
        print("Get")
        return JsonResponse(result_fail)

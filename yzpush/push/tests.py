# coding:utf-8

import requests

res = requests.post('http://127.0.0.1:8000/notify/')
print(res.text)
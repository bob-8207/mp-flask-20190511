#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:BOB-Y
# datetime:2019/4/26 12:39
# software: PyCharm


import requests
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16117088'
API_KEY = 'BD75u2GtZXoOjQXIGipIG2po'
SECRET_KEY = 'XIhhOjZVdKGbXjGTYQWEfrlOcZM7uqWV'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
class Picocr(object):
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content('d:\\7.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """

    client.basicGeneral(image);
"""
print(xx)
yy = str(xx)
yy = yy.encode()
mediaFile = open("d:\\7.txt", "wb")
mediaFile.write(yy)
"""
""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image, options)

url = "http//www.x.com/sample.jpg"

""" 调用通用文字识别, 图片参数为远程url图片 """
client.basicGeneralUrl(url);


""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为远程url图片 """
client.basicGeneralUrl(url, options)


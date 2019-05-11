#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:BOB-Y
# datetime:2019/4/26 18:11
# software: PyCharm

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16117088'
API_KEY = 'BD75u2GtZXoOjQXIGipIG2po'
SECRET_KEY = 'XIhhOjZVdKGbXjGTYQWEfrlOcZM7uqWV'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 调用车牌识别 """
def CarOCR(picPath):

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    return client.licensePlate(get_file_content(picPath))

"""调用车牌识别，参数为图片的二进制格式"""
def CarOCRfile(picData):

    return client.licensePlate(picData)

""" 调用通用文字识别, 图片参数为本地图片 """
def PicOCR(picPath):

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    return client.basicGeneral(get_file_content(picPath))

""" 调用通用文字识别, 图片参数为本地图片二进制格式 """
def PicOCRfile(picData):

    return client.basicGeneral(picData)






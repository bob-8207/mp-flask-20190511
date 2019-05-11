# -*- coding: utf-8 -*-
# filename: media.py
from OCRclass import CarOCR, PicOCR, CarOCRfile, PicOCRfile
#import os
#import base64
#from aip import AipOcr
import urllib2
import json
from basic import Basic
import time
import random
from mysqldb import DBmysql
import pymysql
pymysql.install_as_MySQLdb()

class Media(object):

    def get(self, accessToken, mediaId, fromUser):
        print "保存图片函数启动"
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
        urlResp = urllib2.urlopen(postUrl)
        exclude_code = ''.join(str(random.choice(range(10))) for _ in range(10))
        now_datetime= (time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())))
        pic_code = str(now_datetime) + "-" +str(exclude_code)
        pic_name = pic_code +".jpg"
        pic_path = "/usr/local/bin/pic/"

        headers = urlResp.info().__dict__['headers']
        if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
            jsonDict = json.loads(urlResp.read())
            print jsonDict
        else:
            buffer = urlResp.read()   #素材的二进制
            mediaFile = file( pic_path + pic_code +".jpg", "wb")
            mediaFile.write(buffer)

        #ocr_data = CarOCR(pic_ocr_path)
        ocr_data = CarOCRfile(buffer)  # 调用OCRclass包中的汽车牌照CarOCRfile函数
            #ocr_data = {"log_id": 3207340712179817916, "words_result": {"color": "blue", "number": "京N8P8F8", "probability": [0.9999920129776001, 0.9999918937683105, 0.9999599456787109, 0.9999456405639648, 0.9998923540115356, 0.9998760223388672, 0.9998669624328613], "vertexes_location": [{"y": 188, "x": 53}, {"y": 191, "x": 862}, {"y": 470, "x": 859}, {"y": 470, "x": 52}]}}
            # ocr_data = {"log_id": 4850683191653209340, "error_code": 282102, "error_msg": "detect plate number error"}

        if "error_code" in ocr_data.keys():  # 判断CarOCR函数返回的JSON数据中是否包含车牌信息（包含"cerror_code"健说明没有）
            ocr_data = PicOCRfile(buffer)  # 判断没有车牌信息后，调用OCRclass包中的PicOCR函数进行通用图片识别
            license_plate_color = "None"
            license_plate_number = "None"
            print ("图片内容没有车牌信息！")
            print ocr_data
        else:
            for value in ocr_data["words_result"].values():  # 遍历JSON数据包健值，提取车牌颜色和号码信息
                license_plate_color = ocr_data["words_result"]["color"]
                license_plate_number = ocr_data["words_result"]["number"]
            print (license_plate_color,license_plate_number)

        # 处理OCR返回的JSON数据，实例化为JSON对象才能插入数据库
        json_data = json.dumps(ocr_data, encoding="UTF-8", ensure_ascii=False)

        # 调用Mysql接口保存数据
        ccur = DBmysql('192.168.1.221', 3306, 'root', 'cmdbcmdb', 'WECHAT_DATA')
        ccur.cur.execute(
            'INSERT INTO PIC_RECORD(openid,SAVE_PATH,PIC_NAME,UPLOAD_TIME, LICENSE_PLATE_COLOR, LICENSE_PLATE_NUMBER, JSON_DATA) VALUES(%s, %s, %s, %s, %s,%s, %s)',
            (fromUser, pic_path, pic_name, now_datetime, license_plate_color, license_plate_number, json_data))
            #ccur.cur.execute('select * from PIC_RECORD')
        ccur.close()
        print "数据库操作成功！！！"
        #for s in ccur.cur.fetchall():
            #print(s)

if __name__ == '__main__':
    myMedia = Media()
    accessToken = Basic().get_access_token()
    mediaId = "TXASKPVFqsl19vNOtFLKxc0hv1FmTNUjgx_FSZCeQPpYes7Asx_K1IdmcZgWx36i"
    fromUser = 'xxxxxxxxxxxx'
    myMedia.get(accessToken, mediaId, fromUser)

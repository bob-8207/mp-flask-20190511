# -*- coding: utf-8 -*-
# filename: media.py
import urllib2
import json
from basic import Basic

class Media(object):

    #def __init__(self, accessToken, mediaId):
     #   self.accessToken = accessToken
      #  self.mediaId = mediaId

    #accessToken = Basic().get_access_token()

    def get(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
        urlResp = urllib2.urlopen(postUrl)

        headers = urlResp.info().__dict__['headers']
        if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
            jsonDict = json.loads(urlResp.read())
            print jsonDict
        else:
            buffer = urlResp.read()   #素材的二进制
            mediaFile = file("/usr/local/bin/pic/test_media.jpg", "wb")
            mediaFile.write(buffer)
            print "get successful"

"""
if __name__ == '__main__':
    myMedia = Media()
    accessToken = Basic().get_access_token()
    mediaId = "eVohjAMtS7ToFpOCrHdZvlvTbIXcyOF-4p6q-iwJY3xJsfEur1_SxMaeRLKKpXMA"
    myMedia.get(accessToken, mediaId)
    
"""
#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:BOB-Y
# datetime:2019/4/22 13:22
# software: PyCharm


import receive
import reply
from basic import Basic
from media import Media

myMedia = Media()
accessToken = Basic().get_access_token()
mediaId = "V5EpKZGrKkyYVEt_WlS25UsMJwdhCn50TS0isCeoYvuy0lq9xJwZuUaeM7SdKzFK"
myMedia.get(accessToken, mediaId)


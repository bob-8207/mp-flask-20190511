# -*- coding: utf-8 -*-
# filename: handle.py
import web

import receive
import reply
from basic import Basic
from media import Media


class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            myMedia = Media()
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'event':
                    print ('yes!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    content = "Hi, thanks for attention Fancytech WeChat!          ∩( ・ω・)∩萌萌哒"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'text':
                    content =  "Hi, Can I help you ?          ∩( ・ω・)∩萌萌哒"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    content = "图片已经接收...Thanks♪(･ω･)ﾉ"
                    mediaId = recMsg.MediaId
                    accessToken = Basic().get_access_token()
                    myMedia.get(accessToken, mediaId, toUser)
                    replyMsg = reply.TextMsg(toUser,fromUser, content)
                    #replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()

                else:


                    return reply.Msg().send()

            else:
                print "暂且不处理"
                return reply.Msg().send()
        except Exception, Argment:
            return Argment
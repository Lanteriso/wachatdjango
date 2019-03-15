import itchat
from tuling import getResponse
from itchat.content import *




@itchat.msg_register(itchat.content.TEXT,TEXT,isGroupChat=True)
def text_reply(msg):
    print(msg)
    print(getResponse(msg["Text"])["text"])
    return getResponse(msg["Text"])["text"]
itchat.auto_login(hotReload=True)
itchat.run()

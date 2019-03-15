from django.shortcuts import render
import itchat

from itchat.content import *

import requests
def getResponse(_info):
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
    	'key'    : '47ff9524b0c040bbb9d68483e84a41ea',
    	'info'   : _info, # 这是我们发出去的消息
    	'userid' : 'wechat-robot',
	}
	r = requests.post(apiUrl, data=data).json()
	return r


@itchat.msg_register(itchat.content.TEXT,TEXT,isGroupChat=True)
def text_reply(msg):
    print(msg)
    print(getResponse(msg["Text"])["text"])
    return getResponse(msg["Text"])["text"]

# Create your views here.
def home(request):
    if request.method == "POST":
        itchat.auto_login(hotReload=True)
        itchat.run()
    return render(request,'wechat/home.html')


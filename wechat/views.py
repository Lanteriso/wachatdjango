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



# Create your views here.
def home(request):
	print("来了")
	@itchat.msg_register(itchat.content.TEXT, TEXT, isGroupChat=True)
	def text_reply(msg):
		return getResponse(msg["Text"])["text"]
	itchat.auto_login(enableCmdQR=True)
	print("登陆中")
	itchat.run()
	print("登陆结束")
	return render(request, 'wechat/qr.html')
def qr(request):

	import shutil

	shutil.copy('QR.png', 'static/QR.png')
	return render(request,'wechat/home.html')




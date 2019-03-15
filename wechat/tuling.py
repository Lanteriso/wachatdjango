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

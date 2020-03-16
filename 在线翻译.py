#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests,urllib2,urllib
import urlparse
import json
import sys
from Tkinter import *


root = Tk()
v1 = StringVar()
v2 = StringVar()
#result = r['translateResult'][0][0]['tgt']
#json_string = json.dumps(r.text)


def pc():
	text1 = v1.get()
	url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
	data = {}
	head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0'}
	data['action'] = 'FY_BY_REALTlME'
	data['bv'] = 'e2a78ed30c66e16a857c5b6486a1d326'
	data['client'] = 'fanyideskweb'
	data['doctype'] = 'json'
	data['from'] = 'AUTO'
	data['i'] = text1
	data['keyfrom'] = 'fanyi.web'
	data['salt'] = '15841477289142'
	data['sign'] = 'a02991826298e4300d4f87c5c978e39f'
	data['smartresult'] = 'dict'
	data['to'] = 'AUTO'
	data['ts'] = '1584147728914'
	data['version'] = '2.1'
	r = requests.post(url,data,headers=head)
	r = json.loads(r.text)
	result = r['translateResult'][0][0]['tgt']
	print(result)
	v2.set(result)
	

L1 = Label(root,text='请输入翻译内容:').grid(row=0,column=0,padx=10,pady=5)
e1 = Entry(root,textvariable=v1).grid(row=0,column=1,padx=10,pady=5)
L2 = Label(root,text="翻译的结果:").grid(row=1,column=0,padx=10,pady=10)
e2 = Entry(root,textvariable=v2).grid(row=1,column=1,padx=10,pady=5)
b1 = Button(root,text="翻译",command=pc).grid(row=2,column=0,padx=10,pady=10)

mainloop()


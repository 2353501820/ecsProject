# -*- coding: utf-8 -*-
'''
----------------------
file : tool.py
author : gaobo
time : /09:22
----------------------
'''

import random
class Tool:
	'''
	小工具
	'''
	@classmethod
	def birthday(cls):
		'''
		随机生日
		:return:生日
		'''
		a = random.randint(0,9)
		b = random.randint(0,9)
		d = random.randint(1,9)
		e = random.randint(0,2)
		f = random.randint(1,9)
		bir = '19{}{}-0{}-{}{}'.format(a,b,d,e,f)
		return bir

if __name__ == '__main__':
	a =Tool.birthday()
	print(a)
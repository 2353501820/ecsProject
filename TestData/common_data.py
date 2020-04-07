#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: common_data.py
# author:gaobo
# time:2019/03/05

#测试服务器网址
login_url = 'http://192.168.1.14:8080/sso/login'


#正常登录的用户名和密码
uesname = 'gaobo1'
passward = '123456'

#无名氏 为1即添加无名氏，其余为新增正常患者
anonymous_person = 0
#test_2_exitandswitch.py 需要用到的元素id
emergency_alert = [{'button':'openIndex'},
					{'button':'addPatient'},
				   {'button': 'historyrecord'},
				   {'button':'statisticalreport'},
					{'button':'events'},
				   ]
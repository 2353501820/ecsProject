#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: login_data.py
# author:gaobo
# time:2019/03/05


#正常登录的用户名和密码

suc_datas = {'username':'gaobo1','passward':'123456'}


#异常的用户名和密码:用户名和密码为空/密码为空/用户名为空/密码错误
datas = [
	{'username':'','passward':'','check':'用户名或密码错误！'},
	{'username':'gaobo1','passward':'','check':'用户名或密码错误！'},
	{'username':'','passward':'123456','check':'用户名或密码错误！'},
	{'username': 'gaobo1', 'passward': '987654321', 'check': '用户名或密码错误！'}]










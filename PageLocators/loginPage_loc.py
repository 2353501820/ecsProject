#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: loginPage_loc.py
# author:gaobo
# time:2019/03/06
from selenium.webdriver.common.by import By
class LoginPageLoc:
	pass
	#用户名框
	username = (By.XPATH,'//input[@id="username"]')
	#密码框
	password = (By.XPATH, '//input[@id="password"]')
	#登录按钮
	login_button = (By.ID,'sButton')


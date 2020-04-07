#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File:main.py
# Author：GaoBo
# Time:2019/02/28


from PageLocators.loginPage_loc import LoginPageLoc as loc
from Common import basepage

class LoginPage(basepage.BasePage):

	#登录功能
	def login(self,username,password):
		self.wait_elemVisible(loc.login_button, model_name='登录按钮')
		self.input_text(loc.username,username,model_name='用户名框')
		self.input_text(loc.password,password, model_name='密码框')
		self.click_element(loc.login_button,model_name='登录按钮')

	#获取页面错误提示
	def get_error_msg(self):
		text = self.swtich_alert(model_name='登录错误提示弹窗')

		return text
	#获取登录页面是否存在
	def get_loginpage(self):
		try:
			self.wait_elemVisible(loc.login_button, model_name='登录按钮')
			return True
		except:
			return False





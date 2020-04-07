#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File:main.py
# Author：GaoBo
# Time:2019/02/28

import unittest

from PageObjects.login_page import LoginPage
from PageObjects.switch_page import SwitchPage
from TestData import login_data as LD
import pytest

@pytest.mark.usefixtures("function_env")
@pytest.mark.usefixtures("class_env")
class TestLogin():

	#登录失败的用例
	@pytest.mark.yanshi
	@pytest.mark.parametrize('data',LD.datas)
	def test_login_fail(self,data,class_env):
		#登录功能
		lp = LoginPage(class_env)
		lp.login(data['username'], data['passward'])
		# 错误提示是否正确
		assert data['check'] == lp.get_error_msg()

	#登录成功的用例
	@pytest.mark.yanshi
	def test_loging_success(self,class_env):
		#登录功能
		LoginPage(class_env).login(LD.suc_datas['username'],LD.suc_datas['passward'])
		# 切换页面成功出现身份
		assert SwitchPage(class_env).get_workstation_img()



if __name__ == '__main__':
	pytest.main(['test_login.py'])




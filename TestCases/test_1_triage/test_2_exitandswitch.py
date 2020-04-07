#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: test_2_exitandswitch.py
# author:gaobo
# time:2019/03/18
import pytest
from PageObjects.triage.index_page import IndexPage
from PageObjects.login_page import LoginPage
from PageObjects.switch_page import SwitchPage
@pytest.mark.usefixtures('common_env')
class TestExitAndSwitch:
	"""
	切换和退出
	"""

	@pytest.mark.results
	def test_exit(self,common_env):
		#点击个人信息
		IndexPage(common_env).click_userinfor()
		#点击退出
		IndexPage(common_env).click_exit()
		#验证是否到登录页
		assert LoginPage(common_env).get_loginpage()
		pass

	@pytest.mark.results
	def test_switch(self,common_env):
		# 点击个人信息
		IndexPage(common_env).click_userinfor()
		# 点击切换
		IndexPage(common_env).click_switch()
		# 验证是否到切换页
		assert SwitchPage(common_env).get_workstation_img()
		pass

if __name__ == '__main__':
	pytest.main(['test_2_exitandswitch.py'])

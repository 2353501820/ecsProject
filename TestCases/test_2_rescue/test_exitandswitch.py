#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: test_2_exitandswitch.py
# author:gaobo
# time:2019/03/18
import pytest
from PageObjects.login_page import LoginPage
from PageObjects.switch_page import SwitchPage
from PageObjects.rescue.index_res_page import IndexResPage
@pytest.mark.usefixtures("common_env")
class TestExitAndSwitch:

	# @pytest.mark.test_switch_ward
	# def test_switch_ward(self,common_env):
	# 	'''
	# 	选择病区
	# 	:param common_env:
	# 	:return:
	# 	'''
	# 	irp = IndexResPage(common_env)
	# 	text = irp.choose_ward()
	# 	choose_text = irp.get_index_ward_text()
	# 	assert text == choose_text

	def test_switch_and_exit(self,common_env):
		'''
		先切换再退出
		:param common_env:
		:return:
		'''
		IndexResPage(common_env).swtich_res() # 点击切换
		SwitchPage(common_env).choose_rescue()
		IndexResPage(common_env).exit_res()# 点击退出
		# 验证是否到登录页
		assert LoginPage(common_env).get_loginpage()
		pass

if __name__ == '__main__':
	pytest.main(['-m','test_switch_ward'])
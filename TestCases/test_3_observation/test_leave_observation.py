#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: test_leave_observation.py
# author:gaobo
# time:2019/03/08


import unittest
from PageObjects.login_page import LoginPage
from PageObjects.switch_page import SwitchPage

import pytest
from TestData import login_data as LD
from PageObjects.observation.index_obs_page import IndexObsPage
from PageObjects.observation.patient_obs_page import PatientObsPage
'''
@pytest.mark.usefixtures("function_env")
class TestLeaveObservation:
	#离开留观室
	def test_leave_observation(self,function_env):
		# 登录
		LoginPage(function_env).login(LD.suc_datas['username'], LD.suc_datas['passward'])
		# 选择留观室
		SwitchPage(function_env).choose_observation()
		# 选择患者
		IndexObsPage(function_env).chooes_patient()
		#选择离开留观室
		PatientObsPage(function_env).leave_observation()


'''

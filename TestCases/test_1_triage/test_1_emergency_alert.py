#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: test_1_emergency_alert.py
# author:gaobo
# time:2019/03/14
import pytest
from PageObjects.triage.index_page import IndexPage
from TestData import common_data as CD
@pytest.mark.usefixtures('class_env')
@pytest.mark.usefixtures('function_env')
class TestEmergencyAlert:

	#在不同页面点击危急报警提示，点击一个患者并判断是否跳转到首页
	@pytest.mark.parametrize('data',CD.emergency_alert)
	@pytest.mark.results
	def test_index_alert(self,class_env,data):
		#点击不同的页面后再点击头部报警提示
		IndexPage(class_env).click_button(data['button'])
		#点击头部报警提示
		IndexPage(class_env).click_alert()
		#点击患者，并提取患者姓名
		patient_name =IndexPage(class_env).click_emergency_alert_patient()
		#判断跳转的页面姓名是否一致
		patient_name_all = IndexPage(class_env).get_alltable_fullname()
		assert patient_name==patient_name_all

if __name__ == '__main__':
	pytest.main(['test_1_emergency_alert.py'])
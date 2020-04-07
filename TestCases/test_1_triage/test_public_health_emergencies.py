# -*- coding: utf-8 -*-
'''
----------------------
file : test_public_health_emergencies.py
author : gaobo
time : /10:16
----------------------
'''
import pytest
from PageObjects.triage.public_health_emergencies_page import PublicHealthEmergencies
from TestData.patient_data import datas_event_draf
from PageObjects.triage.index_page import IndexPage
from TestData.patient_data import datas_event_save

@pytest.mark.usefixtures('function_env')
@pytest.mark.usefixtures('class_env')
class TestPublicHealthEmergencies:
	#返回功能
	def test_return_event(self,class_env):
		#点击突发公共事件-新增事件
		phe = PublicHealthEmergencies(class_env)
		phe.click_event()
		#点击返回
		phe.click_return_event()
		assert phe.assert_event_index()
	#添加患者
	@pytest.mark.test
	def test_add_patient(self,class_env):
		# 点击突发公共事件-新增事件
		phe = PublicHealthEmergencies(class_env)
		ip = IndexPage(class_env)
		phe.click_event()
		phe.click_generate_list()#生成清单
		ip.click_emergency_alert_x()
		phe.add_patient()#添加患者
		assert phe.get_patient_num() == 2

	#正常保存
	@pytest.mark.parametrize('data',datas_event_save)
	def test_event_save(self,class_env,data):
		# 点击突发公共事件-新增事件
		phe = PublicHealthEmergencies(class_env)
		phe.click_event()
		# 生成清单
		phe.click_generate_list()
		#输入数据
		phe.send_data(data['cardnum'],data['fullname'])
		phe.click_triage_to()
		#点击保存
		phe.click_save()
		assert phe.assert_event_index()

	#暂存
	@pytest.mark.parametrize('data', datas_event_draf)
	def test_event_def(self,class_env,data):
		# 点击突发公共事件-新增事件
		phe = PublicHealthEmergencies(class_env)
		phe.click_event()
		# 生成清单
		phe.click_generate_list()
		# 输入数据
		phe.send_data(data['cardnum'], data['fullname'])
		# 点击保存
		phe.click_save()
		assert phe.assert_event_index()
if __name__ == '__main__':
	pytest.main(['test_public_health_emergencies.py','-m','test'])

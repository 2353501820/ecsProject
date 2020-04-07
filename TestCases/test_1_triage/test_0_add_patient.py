#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File:test_0_add_patient.py
# Author：GaoBo
# Time:2019/03/01

from PageObjects.triage.index_page import IndexPage
from PageObjects.triage.new_patient_page import NewPatient
from TestData import patient_data as PD

from TestData import common_data as CD
import pytest
@pytest.mark.usefixtures('function_env')
@pytest.mark.usefixtures('class_env')
class TestNewPatient():
	'''
	测试新增患者暂存和保存以及统计的人数变化
	'''
	@pytest.mark.results
	@pytest.mark.adds
	@pytest.mark.parametrize("data",PD.datas_draf)
	def test_new_patient_def(self,data,class_env):
		'''
		新增患者暂存
		:param data: 患者数据
		:param class_env: driver
		:return:
		'''
		ip = IndexPage(class_env)
		# 查询新增前待分诊人数
		num = ip.pending_triage_patients_num()
		#点击新增患者
		ip.click_newPatient()
		#输入数据
		np = NewPatient(class_env)
		np.send_information(cardnum=data['cardnum'], fullname=data['fullname'], birthday=data['birthday'])
		#暂存患者
		np.new_patient_draf()
		assert np.save_suc()
		ip.return_homepage()
		new_num = ip.pending_triage_patients_num()
		assert  new_num -1==num

	@pytest.mark.parametrize("data",PD.datas_save)
	@pytest.mark.add
	@pytest.mark.results
	def test_new_patient_save(self,data,class_env):
		'''
		#新增患者保存
		:param data: 患者数据

		ip = IndexPage(class_env)
		num = ip.separated_patients_num()
		# 点击新增患者
		ip.click_newPatient()
		# 输入数据保存患者
		np = NewPatient(class_env)
		if CD.anonymous_person == 1:
			np.send_information(data['birthday'])#无名氏
		else:
			np.send_information(cardnum=data['cardnum'], fullname=data['fullname'], birthday=data['birthday'])
		#保存患者
		np.new_patient_save()
		:param class_env: driver
		:return:
		'''
		assert np.save_suc()
		ip.return_homepage()
		new_num = ip.separated_patients_num()
		assert new_num - 1 == num
if __name__ == '__main__':
	pytest.main(['test_0_add_patient.py','-m','add'])

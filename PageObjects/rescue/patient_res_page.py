#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: patient_res_page.py
# author:gaobo
# time:2019/03/11
from Common import basepage
from PageLocators.rescue.patient_res_page_loc import PatiengResPageLoc as loc
import time

class PatientResPage(basepage.BasePage):


	#选择离开抢救室
	def leave_rescue(self):
		name = '患者页-离开抢救室'
		try:
			time.sleep(0.5)
			self.wait_elemVisible(loc.leave_rescue, model_name=name)
			self.click_element(loc.leave_rescue, model_name=name)
			self.wait_elemVisible(loc.leave_rescue_win_determine, model_name=name)
			self.input_text(loc.leave_rescue_BP1,'1',model_name='BP1')
			self.input_text(loc.leave_rescue_BP2,'1',model_name='BP2')
			self.input_text(loc.leave_rescue_HR,'1',model_name='HR')
			self.input_text(loc.leave_rescue_SaO2,'1',model_name='SAO2')
			self.input_text(loc.leave_rescue_R,'1',model_name='R')
			self.click_element(loc.leave_rescue_win_determine, model_name=name)
		except Exception as e:
			raise e

	def go_obsroom(self):
		'''
		选择抢救结束的去向
		:return:
		'''
		name = '抢救结束'
		self.wait_elemVisible(loc.rescue_over,model_name=name)
		self.click_element(loc.rescue_over, model_name=name)

		if self.assert_patient_where() == True:
			name1 = '选择去向'
			self.click_element(loc.where, model_name=name1)
			self.wait_elemVisible(loc.determine_where, model_name=name1)
			self.click_element(loc.determine_where, model_name=name1)
			self.wait_elemVisible(loc.determine_where_next, model_name=name1)
			self.click_element(loc.determine_where_next, model_name=name1)
		else:
			self.wait_elemVisible(loc.close, model_name="去向X")
			self.click_element(loc.close, model_name="去向X")

	def assert_patient_where(self):
		'''
		判断选择去向弹窗是否出现
		:return:
		'''
		try:
			self.wait_elemVisible(loc.patient_where,timeout=2,model_name="选择去向去向")
			return True
		except :
			return False



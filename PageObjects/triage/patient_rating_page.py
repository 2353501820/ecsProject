# -*- coding: utf-8 -*-
'''
----------------------
file : patient_rating_page.py
author : gaobo
time : /09:36
----------------------
'''
from selenium.webdriver.common.by import By
from PageLocators.triage.patient_info_page_loc import PatientInfoPageLoc as loc
from Common.basepage import BasePage
import time
class PatientRating(BasePage):

	def chick_rating_mod(self):
		'''
		选择最后一个患者查看和修改按钮
		'''
		name = '已分诊-修改评级'
		self.wait_elemVisible(loc.index_divid_patients_table_edit,model_name=name)
		time.sleep(0.5)
		self.click_element(loc.index_divid_patients_table_edit,model_name=name)

	def click_grade(self):
		name = '评级'#患者页点击分级
		time.sleep(0.5)
		self.wait_elemVisible(loc.grade,model_name=name)
		self.click_element(loc.grade, model_name=name)
		# time.sleep(2)

	def mod_grade(self):
		name = '修改评级'#修改评级操作
		self.wait_elemVisible(loc.grade_1004, model_name=name)
		self.click_element(loc.grade_1004, model_name=name)
		self.select_by_value(loc.grade_changereason,value="病情减轻",model_name=name)
		self.click_element(loc.grade_ok, model_name=name)

	def assert_patient_mod(self): #验证是否有改字
		name = '评级'
		self.wait_elemVisible(loc.grade,model_name=name)
		try:
			self.wait_elemVisible(loc.grade_mod)
			return True
		except:
			return False
	def assert_index_mod(self):
		'''
		验证首页已分诊是否有改字
		:return:
		'''
		try:
			self.wait_elemVisible(loc.table_change_label,model_name='验证首页已分诊是否有改字')
			return True
		except:
			return False
	def again_rating(self):#再次评级操作
		name = '再次评级'
		time.sleep(1)
		self.wait_elemVisible(loc.again_rating,model_name=name)
		self.click_element(loc.again_rating,model_name=name)
		self.wait_elemVisible(loc.again_rating_button, model_name=name)
		self.click_element(loc.again_rating_button, model_name=name)
		self.wait_elemVisible(loc.again_rating_button_ok, model_name=name)
		self.click_element(loc.again_rating_button_ok, model_name=name)
	def get_rating_num(self):#获取评级次数的文本
		name='评级次数'
		self.wait_elemVisible(loc.reting_num,model_name=name)
		num_text = self.get_element_text(loc.reting_num,model_name=name)
		num = num_text[0]
		if num =='一':
			return 1
		elif num == '二':
			return 2
		elif num == '三':
			return 3
		else:
			return 4



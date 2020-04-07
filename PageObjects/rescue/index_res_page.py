#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: index_res_page.py
# author:gaobo
# time:2019/03/11
from Common import basepage
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from PageLocators.rescue.index_res_page_loc import IndexResPageLoc as loc
class IndexResPage(basepage.BasePage):


	def chooes_patient(self):
		'''
		选择患者
		:return:
		'''
		name = '首页-选择患者'
		self.wait_elemVisible(loc.patient_text, model_name=name)
		self.click_element(loc.patient_text,model_name=name)
	def assert_patient_null(self):
		'''
		判断床位上是否有患者
		:return: true 有患者  false 没有患者
		'''
		try:
			name = '首页-选择患者'
			self.wait_elemVisible(loc.patient_text, model_name=name)
			return True
		except:
			return False

	def get_patient_num_bed(self):
		'''
		获取床位上的患者人数
		:return: 床位上患者人数
		'''
		name = '首页-患者'
		time.sleep(1)
		self.wait_elemVisible(loc.patient_text,model_name=name)
		return len(self.get_elements(loc.patient_text,model_name=name))

	#点击返回首页
	def return_res_homepage(self):
		name = '返回首页'
		self.wait_elemVisible(loc.return_res_homepage,model_name=name)
		self.click_element(loc.return_res_homepage,model_name=name)
	#点击接诊分床，并获取分床的床号
	def click_reception_bed(self):
		name = '接诊分床按钮'
		self.wait_elemVisible(loc.reception_bed,model_name=name)
		card_num = self.get_element_text(loc.patient_num)
		self.click_element(loc.reception_bed,model_name=name)
		name_1 = '选择床位'
		self.wait_elemVisible(loc.choose_bed,model_name=name_1)
		self.click_element(loc.choose_bed,model_name=name_1)
		return card_num

	#根据卡号查找床位上患者
	def seek_cardnum(self,num):
		try:

			self.wait_elemVisible((By.XPATH,'//p[text()="{}"]'.format(num)))
			self.get_element((By.XPATH,'//p[text()="{}"]'.format(num)))
			return True
		except:
			return False
	#判断床位是否满
	def assert_nonebed(self):
		try:
			name = '空闲床位'
			self.wait_elemVisible(loc.none_bed,model_name=name)
			self.get_element(loc.none_bed,model_name=name)
			return True
		except:
			return False
	#点击切换
	def swtich_res(self):
		name = '切换'
		self.wait_elemVisible(loc.patient_switch,model_name=name)
		self.click_element(loc.patient_switch,model_name=name)
	#点击签退
	def exit_res(self):
		name = '签退'
		self.wait_elemVisible(loc.patient_exit, model_name=name)
		self.click_element(loc.patient_exit, model_name=name)
	#点击报特殊
	def click_special(self):
		name = '报特殊'
		self.wait_elemVisible(loc.menu,model_name=name)
		self.click_element(loc.menu,model_name=name)
		self.wait_elemVisible(loc.special, model_name=name)
		self.click_element(loc.special, model_name=name)
		self.wait_elemVisible(loc.win,model_name=name)
		self.click_element(loc.special_patient,model_name=name)
		self.click_element(loc.owe_patient, model_name=name)
		self.click_element(loc.determine,model_name=name)


	def get_special_img_num(self):
		'''
		获取特殊标识数量
		:return: 特殊标识数量
		'''
		name = '获取特殊标识数量'
		self.wait_elemVisible(loc.special_img,model_name=name)
		num =len(self.get_elements(loc.special_img,model_name=name))
		return num

	def get_num_count(self):
		'''
		获取待接诊人数
		:return: 待接诊人数
		'''
		name = '待接诊人数'
		self.wait_elemVisible(loc.num_count,model_name=name)
		time.sleep(0.5)
		num = int(self.get_element_text(loc.num_count,model_name=name))
		return num
	#获取首页病区
	def get_index_ward_text(self):
		name = '获取首页病区'
		time.sleep(1)
		text = self.get_element_text(loc.button_ward,model_name=name)
		return text

	def get_choose_ward_text(self):
		'''
		获取选择的病区
		:return:
		'''
		name = '获取选择的病区'
		self.wait_elemVisible(loc.choose_ward,model_name=name)
		text = self.get_element_text(loc.choose_ward,model_name=name)
		return text

	def choose_ward(self):
		'''
		选择病区
		:return:
		'''
		name = '选择病区'
		self.wait_elemVisible(loc.button_ward,model_name=name)
		self.click_element(loc.button_ward,model_name=name)
		self.wait_elemVisible(loc.all_ward,model_name=name)
		text= self.get_choose_ward_text()
		self.click_element(loc.choose_ward,model_name=name)
		return text


	def click_ward_button(self):
		'''
		点击病区按钮
		:return:
		'''
		name = '选择病区'
		self.wait_elemVisible(loc.button_ward, model_name=name)
		self.click_element(loc.button_ward, model_name=name)

	def choose_ward_all(self):
		'''
		循环选择所有的病区
		:return:list_id 列表
		'''
		name = '获取病区列表'
		self.wait_elemVisible(loc.choose_ward, model_name=name)
		list_ele = self.get_elements(loc.choose_ward,model_name=name)
		list_id = []
		for i in list_ele:
			id =self.get_attribute(ele=i,attribute='id',model_name=name)
			list_id.append(id)
		return  list_id
	def click_ward(self,text):
		'''
		根据传的病区名称选择病区
		:param text: 每个病区的text
		:return:
		'''
		name = '点击病区'
		time.sleep(1)
		self.wait_elemVisible((By.XPATH,'//div[@id="wardbuttons"]//button[text()="{}"]'.format(text)),model_name=name)
		self.click_element((By.XPATH,'//div[@id="wardbuttons"]//button[text()="{}"]'.format(text)),model_name=name)

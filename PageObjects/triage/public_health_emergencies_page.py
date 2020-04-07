# -*- coding: utf-8 -*-
'''
----------------------
file : public_health_emergencies_page.py.py
author : gaobo
time : /16:25
----------------------
'''
from Common import basepage
from PageLocators.triage.public_health_emergencies_page_loc import PublicHealthEmergenciesPageLoc as loc
import time
class PublicHealthEmergencies(basepage.BasePage):
	#点击突发公共事件-新增事件
	def click_event(self):
		name ='突然公共卫生事件'
		self.wait_elemVisible(loc.public_health_emergencies,model_name=name)
		self.click_element(loc.public_health_emergencies,model_name=name)
		name1 = '新增事件'
		self.wait_elemVisible(loc.add_event, model_name=name1)
		self.click_element(loc.add_event, model_name=name1)
	#返回操作
	def click_return_event(self):
		name = '返回'
		self.wait_elemVisible(loc.return_event, model_name=name)
		self.click_element(loc.return_event, model_name=name)
	#是否在突发公共卫生事件首页
	def assert_event_index(self):
		try:
			self.wait_elemVisible(loc.add_event)
			return True
		except:
			return False
	#生成清单
	def click_generate_list(self):
		name = '事件名称'
		self.wait_elemVisible(loc.send_eventname,model_name=name)
		self.input_text(loc.send_eventname,value='火灾', model_name=name)
		name1 = '人数'
		self.wait_elemVisible(loc.send_eventnum, model_name=name1)
		self.input_text(loc.send_eventnum,'1',model_name=name1)
		name2 = '生成清单'
		self.wait_elemVisible(loc.eventchat, model_name=name2)
		self.click_element(loc.eventchat, model_name=name2)
	#保存
	def click_save(self):
		name = '保存'
		self.wait_elemVisible(loc.save, model_name=name)
		self.click_element(loc.save, model_name=name)
	#输入数据信息
	def send_data(self,cardnum,fullname):
		name = '输入患者信息'
		self.wait_elemVisible(loc.cardnum, model_name=name)
		self.input_text(loc.cardnum,cardnum,model_name=name)
		self.input_text(loc.fullname,fullname,model_name=name)
		self.select_by_value(loc.gender,value='未说明',model_name=name)
		self.input_text(loc.age,value='19890228',model_name=name)
		self.select_by_value(loc.source,value='110',model_name=name)
		self.select_by_value(loc.hospital_visit,value='轮椅',model_name=name)
		self.select_by_value(loc.consciousness, value='谵妄', model_name=name)
		self.click_element(loc.pash_history,model_name=name)
		self.wait_elemVisible(loc.pash_history_list,model_name=name)
		self.click_element(loc.pash_history_list_high,model_name=name)
		self.input_text(loc.ssy,value='120',model_name=name)
		self.input_text(loc.szy, value='60', model_name=name)
		self.input_text(loc.heart_rate, value='62', model_name=name)
		self.input_text(loc.respiratory_rate, value='55', model_name=name)
		self.input_text(loc.temperature, value='42', model_name=name)
		self.click_element(loc.classification,model_name=name)
		self.wait_elemVisible(loc.classification_list,model_name=name)
		self.wait_elemVisible(loc.quick_sizing_1, model_name=name)
		self.click_element(loc.quick_sizing_1, model_name=name)
		self.wait_elemVisible(loc.quick_sizing_2, model_name=name)
		self.click_element(loc.quick_sizing_2, model_name=name)
		self.wait_elemVisible(loc.quick_sizing_3, model_name=name)
		self.click_element(loc.quick_sizing_3, model_name=name)
	#选择去向
	def click_triage_to(self):
		name = '去向'
		# self.click_element(loc.triage_to, model_name=name)
		# time.sleep(0.5)
		self.select_by_value(loc.triage_to,value='8',model_name=name)
	#添加患者
	def add_patient(self):
		name='添加患者'
		time.sleep(0.5)
		self.wait_elemVisible(loc.add_patient, model_name=name)
		self.click_element(loc.add_patient, model_name=name)
		self.wait_elemVisible(loc.add_patient_determine, model_name=name)
		self.click_element(loc.add_patient_determine, model_name=name)
	#获取患者人数
	def get_patient_num(self):
		name = '患者人数'
		self.wait_elemVisible(loc.numdiv,model_name=name)
		num = self.get_element_text(loc.numdiv)
		return int(num)
	#保存成功的弹窗
	def get_save_win(self):
		pass
		try:
			self.wait_elemVisible(loc.save_win)
			return True
		except:
			return False




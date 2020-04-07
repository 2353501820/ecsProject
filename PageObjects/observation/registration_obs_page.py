# -*- coding: utf-8 -*-
'''
----------------------
file : registration_obs_page.py
author : gaobo
time : /17:11
----------------------
'''
from Common.basepage import BasePage
from PageLocators.observation.index_obs_page_loc import IndexObsPageLoc as iloc
from PageLocators.observation.registration_obs_page_loc import RegistrationObsPageLoc as rloc
from TestData.patient_data import PatientData as PD
import time
class RegistrationObsPage(BasePage):
	'''
	登记过程类
	'''

	def click_new_patients(self):
		'''
		点击新增患者
		:return:
		'''
		name = '新增患者'
		self.wait_elemVisible(iloc.new_patients,model_name=name )
		self.click_element(iloc.new_patients,model_name=name)

	def input_data_newpatient(self,cardnum ,fullname):
		'''
		录入数据-新增患者
		:param cardnum: 患者卡号
		:param fullname: 患者姓名
		:return:
		'''
		name = '输入新增患者数据'
		self.wait_elemVisible(rloc.reg_save, model_name=name)
		self.input_text(rloc.cardnum,value=cardnum,model_name='就诊卡号')
		self.input_text(rloc.fullname,value=fullname,model_name='姓名')
		self.click_element(rloc.birthday,model_name='生日')
		self.input_text(rloc.birthday, value=PD.birthday, model_name='生日')
		self.input_text(rloc.idcard, value=PD.idcard, model_name='身份证号')
		self.input_text(rloc.phone, value=PD.phone, model_name='手机号')
		self.select_by_index(rloc.bed_num,1,model_name='床号')
		self.select_by_index(rloc.depart,1,model_name='留观科室')
		self.input_text(rloc.allergic_history, value=PD.allergic_history, model_name='过敏史')
		self.click_element(rloc.anamnesis,model_name='既往史')
		self.input_data_regpatient()

	def input_data_regpatient(self):
		'''
		录入数据-登记患者
		:return:
		'''
		name = '登记患者数据'
		self.wait_elemVisible(rloc.reg_save,model_name=name)
		self.input_text(rloc.diagnosis,value=PD.diagnosis,model_name='诊断')
		self.input_text(rloc.address,value=PD.address,model_name='通讯地址')
		self.input_text(rloc.doctor_name,value=PD.doctor_name,model_name='留观医生')
		self.click_element(rloc.admission,model_name='入室-步入')
		self.click_element(rloc.decubitus,model_name='卧位-平卧')
		self.click_element(rloc.consciousness, model_name='神志-嗜睡')
		self.click_element(rloc.bilateral_pupil, model_name='双侧瞳孔 等大')
		self.input_text(rloc.bilateral_pupil_text,value='12',model_name='双侧瞳孔 等大')
		self.click_element(rloc.light_response, model_name='对光反射 灵敏')
		self.click_element(rloc.skin, model_name='皮肤黏膜 湿冷')
		self.click_element(rloc.face, model_name='面色 正常')
		self.click_element(rloc.lips, model_name='口唇 苍白')
		self.click_element(rloc.edts_registration, model_name='EDTS按钮')
		self.wait_elemVisible(rloc.edts_registration_checkbox,model_name='EDTS选项')
		self.click_element(rloc.edts_registration_checkbox,model_name='EDTS选项')
		self.click_element(rloc.edts_registration_determine,model_name='EDTS确定')
		time.sleep(0.5)
		name1 ='跌倒 / 坠床风险'
		self.click_element(rloc.fallingscore, model_name=name1)
		self.wait_elemVisible(rloc.fallingscore_table, model_name=name1)
		self.click_element(rloc.fallingscore_checkbox, model_name=name1)
		self.click_element(rloc.fallingscore_table_determine, model_name=name1)
		time.sleep(0.5)
		name2 = '压疮危险因素—Branden'
		self.click_element(rloc.bardenscore, model_name=name2)
		self.wait_elemVisible(rloc.bardenscore_table, model_name=name2)
		self.click_element(rloc.bardenscore_b12, model_name=name2)
		self.click_element(rloc.bardenscore_b22, model_name=name2)
		self.click_element(rloc.bardenscore_b32, model_name=name2)
		self.click_element(rloc.bardenscore_b42, model_name=name2)
		self.click_element(rloc.bardenscore_b52, model_name=name2)
		self.click_element(rloc.bardenscore_b63, model_name=name2)
		self.click_element(rloc.bardenscore_determine, model_name=name2)
		time.sleep(0.5)
	def reg_save(self):
		'''
		点击登记保存
		:return:
		'''
		self.click_element(rloc.reg_save,model_name='登记保存')

	def save_suc(self):
		'''
		判断登记保存成功的弹窗是否出现
		:return: True出现，False不出现
		'''
		try:
			self.wait_elemVisible(rloc.save_suc,model_name='保存成功')
			time.sleep(0.5)
			return True
		except:
			return False






#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File:new_patient_page.py
# Author：GaoBo
# Time:2019/03/01
from PageLocators.triage.new_patient_page_loc import NewPatientPageLoc as loc
from Common import basepage
from TestData.patient_data import PatientData as pd
from TestData.common_data import anonymous_person
import time
class NewPatient(basepage.BasePage):

	def send_information(self,birthday,fullname=None,cardnum=None):
	#新增患者选择输入患者信息

		self.wait_elemVisible(loc.dosave,model_name="输入患者信息")
		if anonymous_person == 1:
			self.input_text(loc.fullname,'无名氏', model_name="输入姓名")  # 输入无名氏
		else:
			self.input_text(loc.cardnum,cardnum,model_name="输入卡号")# 输入卡号
			self.input_text(loc.fullname,fullname,model_name="输入姓名")# 输入姓名
		self.select_by_value(loc.gender,pd.gender,model_name='选择性别')# 选择性别
		self.click_element(loc.birthday,model_name='选择生日')# 生日先点击输入框，再输入日期
		self.input_text(loc.birthday,birthday, model_name='选择生日')
		self.select_by_index(loc.category,1,model_name='费别')
		self.input_text(loc.sg,pd.sg,model_name='身高')
		self.input_text(loc.tz,pd.tz,model_name='体重')
		self.input_text(loc.tel,pd.phone,model_name='输入手机号')# 输入手机号
		self.input_text(loc.idcard,pd.idcard,model_name='身份证号')
		self.input_text(loc.parenttel, pd.parenttel, model_name='家属电话')
		self.input_text(loc.memberstel, pd.memberstel, model_name='紧急联系人')
		self.input_text(loc.address, pd.address, model_name='地址')

		self.click_element(loc.source,model_name='选择来源')# 选择来源
		self.click_element(loc.source_method,model_name='选择来源方式')# 选择来源方式
		self.input_text(loc.reason, pd.reason, model_name='来院原因')
		self.click_element(loc.state_consciousnes,model_name='选择意识状态')# 选择意识状态
		self.click_element(loc.pash_history,model_name='选择既往史')# 选择既往史
		self.click_element(loc.allergic_history,model_name='药物过敏史')#药物过敏史

		self.input_text(loc.note, pd.note, model_name='备注')
		#输入生命体征
		self.input_text(loc.maibo,value=pd.maibo,model_name='心率')
		self.input_text(loc.spo2, value=pd.spo2, model_name='血氧饱和度')
		self.input_text(loc.shousuoya, value=pd.shousuoya, model_name='收缩压')
		self.input_text(loc.shuzhangya, value=pd.shuzhangya, model_name='舒张压')
		self.input_text(loc.tiwen, value=pd.tiwen, model_name='体温')
		# 选择快速分级
		self.click_element(loc.fast_grading, model_name='选择快速分级')
		time.sleep(0.2)
		self.wait_elemVisible(loc.fast_grading_1)
		self.click_element(loc.fast_grading_1, model_name='点击分类')
		self.wait_elemVisible(loc.fast_grading_2)
		self.click_element(loc.fast_grading_2, model_name='点击主诉')
		self.wait_elemVisible(loc.fast_grading_3)
		self.click_element(loc.fast_grading_3, model_name='点击判定依据')
		self.click_element(loc.fast_grading, model_name='选择快速分级')

		# 选择疼痛评分
		self.wait_elemVisible(loc.pain, model_name='疼痛评分')
		self.click_element(loc.pain, model_name='疼痛评分')
		self.wait_elemVisible(loc.pain_ten, model_name='疼痛评分')
		self.click_element(loc.pain_ten, model_name='疼痛评分')
		self.click_element(loc.pain_confirm, model_name='疼痛评分')
		time.sleep(0.5)
		#选择edts评级
		# self.click_element(loc.edts, model_name='EDTS')
		# time.sleep(0.1)
		# self.wait_elemVisible(loc.edts_1,model_name='EDTS选项1')
		# time.sleep(0.1)
		# self.click_element(loc.edts_1, model_name='EDTS选项1')
		# # self.click_element(loc.edts_2, model_name='EDTS选项2')
		# time.sleep(0.1)
		# self.click_element(loc.edts_win_confirm, model_name='评级弹窗确认') #评级弹窗上的确认
		# time.sleep(0.5)


		# 选择分诊去向
		self.click_element(loc.choose_depart, model_name='选择去向')
		self.wait_elemVisible(loc.department,model_name='去向弹窗')
		self.click_element(loc.department, model_name='去向点击')
		time.sleep(0.5)



	def new_patient_save(self):	#新增患者保存
		# 点击button
		self.wait_elemVisible(loc.dosave, model_name='保存按钮')
		time.sleep(0.5)
		self.click_element(loc.dosave, model_name='保存按钮')
		# 等待保存成功并点确定
		# self.wait_elemVisible(loc.determine_win,model_name='弹窗确定按钮')
		# self.click_element(loc.determine_win, model_name='弹窗确定按钮')
	def patient_save(self):	#患者保存
		# 点击button
		self.wait_elemVisible(loc.dosave, model_name='保存按钮')
		time.sleep(0.5)
		self.click_element(loc.dosave, model_name='保存按钮')
		# 等待保存成功并点确定
		self.wait_elemVisible(loc.determine_win,model_name='弹窗确定按钮')
		self.click_element(loc.determine_win, model_name='弹窗确定按钮')




	def new_patient_draf(self):		#新增患者暂存
		# 点击button
		self.wait_elemVisible(loc.dodraf, model_name='暂存按钮')
		self.click_element(loc.dodraf, model_name='暂存按钮')
		# 等待暂存成功并点确定
		# self.wait_elemVisible(loc.determine_win, model_name='弹窗确定按钮')
		# self.click_element(loc.determine_win, model_name='弹窗确定按钮')
	def save_suc(self):#获取保存成功
		name = '保存成功'
		try:
			self.wait_elemVisible(loc.save_suc,model_name=name)
			self.get_element(loc.save_suc, model_name=name)
			self.wait_elemVisible(loc.determine_win, model_name='弹窗确定按钮')
			self.click_element(loc.determine_win, model_name='弹窗确定按钮')
			return True
		except:
			return False



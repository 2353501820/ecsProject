#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: new_patient_page_loc.py
# author:gaobo
# time:2019/03/06

from selenium.webdriver.common.by import By
class NewPatientPageLoc:

	dosave = (By.XPATH,'//button[text()="保存"]')#保存按钮
	dodraf = (By.XPATH,'//button[text()="暂存"]')#暂存按钮
	cardnum = (By.ID,'cardnum')	#卡号输入框

	fullname = (By.ID,'fullname')	#姓名输入框

	gender = (By.ID,'gender')	#性别
	tz= (By.ID,'tz')#体重
	birthday = (By.ID,'bornday')	#生日
	sg =  (By.ID,'sg')#身高
	parenttel = (By.ID,'parenttel')#患者家属电话
	memberstel = (By.ID,'memberstel')#紧急联系人
	address = (By.ID,'address')#地址
	idcard = (By.ID,'idcard')  #身份证号
	category = (By.ID,'category')	#费别
	reason = (By.ID,'reason') #来院原因
	note = (By.ID,'hljl')  #备注
	tel = (By.ID,'tel')	#手机号
	source = (By.XPATH,'//span//input[@value="120"]')	# 选择来源：120
	source_method = (By.XPATH,'//span//input[@value="扶走"]')	#选择来源方式
	state_consciousnes = (By.XPATH,'//span//input[@value="清醒"]')	#意识状态：清醒
	pash_history = (By.XPATH,'//span//input[@value="糖尿病"]')	#既往史
	allergic_history = (By.XPATH,'//input[@name="allergic_history" and @value="头孢"]')	# 药物过敏史
	import_signs = (By.XPATH,'//button[text()="导入生命体征"]')	#导入生命体征按钮
	maibo = (By.ID,'maibo')	#脉搏
	spo2 = (By.ID,'spo2')	#SpO2 血氧饱和度
	shousuoya = (By.ID,'shousuoya')	#收缩压
	shuzhangya =  (By.ID,'shuzhangya')	#舒张压
	tiwen = (By.ID,'tiwen')	#体温
	#左下角快速分级按钮和选择分级
	fast_grading = (By.XPATH,'//div[contains(@class,"gradeMark")]')
	fast_grading_1 = (By.XPATH,'//li[@id="13885703552"]//a')
	fast_grading_2 = (By.XPATH,'//li[@id="17163349292"]//a')
	fast_grading_3 = (By.XPATH, '//li[@id="11073624790"]//a')


	edts =  (By.XPATH, '//div[@id="edts"]')	# edts评级按钮
	#edts评级弹窗
	edts_win = (By.XPATH, '//div[@id="quickpf"]')
	edts_1 =  (By.XPATH, '//li[@id="e-b-1-1"]')
	edts_2 = (By.XPATH, '//li[@id="e-c-1-1"]')
	#edts评级弹窗上的确认
	edts_win_confirm = (By.XPATH, '//div[@id="modalEdts"]//button[text()="确认"]')
	#分诊时间框
	dividtime = (By.ID, 'dividtime')
	dividtime_now = (By.XPATH, '//span[text()="此刻"]')
	#分诊去向按钮
	choose_depart = (By.ID, 'chooseDepart')
	#选择科室
	department = (By.XPATH, '//ul[@id="department"]//a[text()="急诊眼科"]')
	#弹窗的确定按钮
	determine_win = (By.XPATH, '//div[@id="delcfmModel2"]//a[text()="确定"]')
	#疼痛评分
	pain = (By.ID,'pain')
	#10级
	pain_ten = (By.XPATH, '//span[text()="10"]')
	pain_confirm = (By.XPATH, '//div[@id="modalScore"]//button[text()="确认"]')
	#保存成功
	save_suc = (By.ID, 'mes2')




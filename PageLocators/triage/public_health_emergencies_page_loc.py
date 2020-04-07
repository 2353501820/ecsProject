# -*- coding: utf-8 -*-
'''
----------------------
file : public_health_emergencies_page_loc.py
author : gaobo
time : /10:22
----------------------
'''
from selenium.webdriver.common.by import By
class PublicHealthEmergenciesPageLoc:
	#突发公共卫生事件按钮
	public_health_emergencies = (By.ID,'events')
	#新增事件
	add_event = (By.XPATH,'//button[text()="新增事件"]')
	#事件输入名字
	send_eventname = (By.ID,'name')
	# 事件输入人数
	send_eventnum = (By.ID, 'num')
	# 事件生成清单
	eventchat = (By.ID, 'btn-chat')
	# 卡号输入框
	cardnum = (By.NAME, 'cardnum')
	# 姓名输入框
	fullname = (By.NAME, 'fullname')
	#性别
	gender = (By.NAME, 'gender')
	# 年龄输入框
	age = (By.NAME, 'age')
	#来源
	source= (By.NAME, 'source')
	#来院方式
	hospital_visit = (By.NAME, 'lyfs')
	#意识状态
	consciousness = (By.NAME, 'consciousness')
	#既往病史
	pash_history =(By.ID, 'history_1')
	# 既往病史列表
	pash_history_list = (By.ID, '1')
	#选择高血压
	pash_history_list_high = (By.XPATH, '//div[@id="1"]//button[text()="高血压"]')
	#血压
	ssy = (By.NAME, 'ssy')
	szy = (By.NAME, 'szy')
	#心率
	heart_rate = (By.NAME, 'maibo')
	#体温
	temperature = (By.NAME, 'tiwen')
	#呼吸频率
	respiratory_rate = (By.NAME, 'huxi')
	# 分级
	classification = (By.XPATH, '//span[text()="分级"]')
	#完整评级
	classification_list = (By.ID, 'classify1')
	#快速评级三次选择
	quick_sizing_1 = (By.ID, '10714307018')
	quick_sizing_2= (By.ID, '10437537916')
	quick_sizing_3 = (By.ID, '10515367977')
	#分诊去向
	triage_to = (By.NAME, 'chooseDepart')
	#删除按钮
	delete = (By.XPATH, '//*[@class="fa fa-trash-o delete"]')
	#返回按钮
	return_event = (By.XPATH, '//button[text()="返回"]')
	#保存
	save = (By.ID, 'save')
	#添加患者
	add_patient = (By.XPATH, '//div[text()="添加患者"]')
	#添加患者确定按钮
	add_patient_determine =  (By.XPATH, '//div[@id="addList"]//button[text()="确定"]')
	#患者人数
	numdiv =  (By.ID, 'numdiv')
	#保存成功的弹窗
	save_win = (By.XPATH, '//p[text()="保存成功"]')





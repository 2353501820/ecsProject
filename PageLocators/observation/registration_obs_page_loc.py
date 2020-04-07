# -*- coding: utf-8 -*-
'''
----------------------
file : registration_obs_page_loc.py
author : gaobo
time : /19:30
----------------------
'''
from selenium.webdriver.common.by import By
class RegistrationObsPageLoc:
	#就诊卡号
	cardnum = (By.ID, 'cardnum1')
	#姓名
	fullname = (By.ID, 'fullname1')
	#出生日期
	birthday = (By.ID, 'bornday')
	#身份证号
	idcard = (By.ID, 'idcard')
	#手机号
	phone = (By.ID, 'phone')
	#床号
	bed_num = (By.ID, 'bed_num')
	#留观科室
	depart = (By.ID, 'depart')
	#既往史
	anamnesis = (By.ID, 'anamnesis4')
	#过敏史
	allergic_history = (By.ID, 'allergic_history')
	# 诊断
	diagnosis = (By.ID, 'diagnosis')
	# 通讯地址
	address = (By.ID, 'address')
	# 留观医生
	doctor_name = (By.ID, 'doctor_name')
	# 入室 步入
	admission = (By.ID, 'checkbox1')
	# 卧位 平卧
	decubitus = (By.ID, 'checkbox6')
	# 神志 嗜睡
	consciousness = (By.ID, 'checkbox13')
	# 双侧瞳孔 等大
	bilateral_pupil = (By.ID, 'checkbox19')
	bilateral_pupil_text = (By.ID, 'pupil')
	# 对光反射 灵敏
	light_response = (By.ID, 'checkbox24')
	# 皮肤黏膜 湿冷
	skin = (By.ID, 'checkbox29')
	# 面色 正常
	face = (By.ID, 'checkbox36')
	# 口唇 苍白
	lips = (By.ID, 'checkbox43')
	# EDTS评分
	edts_registration = (By.XPATH,'//*[@id ="edtsscore1"]//button')
	edts_registration_checkbox = (By.XPATH,'//td[text()="颅内出血"]')
	edts_registration_determine = (By.XPATH,'//button[@class="btn btn-success"]')
	#跌倒 / 坠床风险
	fallingscore = (By.XPATH,'//*[@id ="fallingscore1"]//button')
	fallingscore_table = (By.ID, 'ftable')
	fallingscore_checkbox = (By.ID, '9-2')
	fallingscore_table_determine = (By.XPATH,'//div[@id="modalFail"]//button[text()="确定"]')
	#压疮危险因素—Branden
	bardenscore = (By.ID, 'pf3')
	bardenscore_table = (By.ID,'table-braden')
	bardenscore_b12 = (By.ID,'b-1-2')
	bardenscore_b22 = (By.ID,'b-2-2')
	bardenscore_b32 = (By.ID,'b-3-2')
	bardenscore_b42 = (By.ID,'b-4-2')
	bardenscore_b52 = (By.ID,'b-5-2')
	bardenscore_b63 = (By.ID,'b-6-3')
	bardenscore_determine = (By.XPATH,'//button[text()="提交"]')
	#切换随诊
	suizhenbutton = (By.ID,'suizhenbutton')
	#保存
	reg_save = (By.XPATH,'//button[text()="保存"]')
	#保存成功
	save_suc = (By.XPATH,'//*[@id="mes1" and text()="保存成功!"]')


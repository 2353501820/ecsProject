#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: index_obs_page_loc.py
# author:gaobo
# time:2019/03/06
from selenium.webdriver.common.by import By
class IndexPageLoc:
	# 新增患者按钮
	addPatient = (By.ID, 'addPatient')
	# 已分诊按钮
	re_evaluated = (By.XPATH, '//a[text()="已分诊"]')
	#已接诊按钮
	re_recived= (By.XPATH, '//a[text()="已接诊"]')
	#待分诊列表人数
	pending_triage_num = (By.ID, 'wait')
	#已分诊列表人数
	re_evaluate_num =(By.ID, 'divid')
	#已接诊人数
	accepted_num = (By.ID, 'receive')
	#特殊人员人数
	special_personnel_num = (By.ID,'special')
	#返回首页按钮
	return_homepage = (By.ID, 'openIndex')
	#待分诊按钮
	pending_triage = (By.XPATH, '//a[text()="待分诊"]')
	# 历史记录按钮
	historyrecord = (By.ID, 'historyrecord')
	#历史记录查找数据-能找到删除按钮就好
	get_historyrecord=(By.XPATH, '//span[text()="删除"]')
	#报警消息
	alert_msg=(By.ID,'warnNum')
	#危急报警提示框
	emergency_alert = (By.ID,'toast-container-yling')
	#危急报警提示框x按钮
	emergency_alert_x = (By.XPATH, '//div[@id="toast-container-yling"]//*[text()="×"]')
	#危急报警提示框第一个患者
	emergency_alert_first = (By.XPATH, '//div[@id="toast-container-yling"]//td')
	#全部患者里的名字
	all_fullname = (By.XPATH, '//table[@id="all-patients"]//td[5]')
	#统计报表
	statistical_report = (By.ID, 'statisticalreport')
	#个人信息
	userinfo = (By.ID, 'nurse')
	#退出
	userexit = (By.XPATH, '//span[text()="退出"]')
	#切换
	userswitch = (By.XPATH, '//span[text()="切换"]')
	#欠费患者
	arrears = (By.XPATH, '//label[text()="欠费患者"]')
	#特殊患者
	special = (By.XPATH, '//label[text()="特殊患者"]')
	#特殊患者提示信息里确定按钮
	determine_win_special =  (By.XPATH, '//div[@id="promptModel"]//a[text()="确定"]')
	#接诊按钮
	accepted = (By.XPATH, '//span[@id="receive"]')
	#接诊确定
	determine_win_accepted = (By.XPATH, '//a[text()="确定" and @onclick="teurlSubmit()"]')
	#待分诊删除按钮
	pending_triage_delete = (By.XPATH, '//table[@id="wait-patients"]// span[@e_name="index_wait_patients_table_del"]')

	#messsage提示消息框
	prompt_message = (By.XPATH, '//div[@class="modal fade common-modal in"]')
	# messsage提示消息框X按钮
	prompt_message_x = (By.XPATH, '//div[@id="delcfmModel"]//span[text()="×"]')
	# messsage提示消息框取消
	prompt_message_cancel = (By.XPATH, '//div[@id="delcfmModel"]//button[text()="取消"]')
	# messsage提示消息框确定
	prompt_message_detemine = (By.XPATH, '//div[@id="delcfmModel"]//a[text()="确定"]')
	#向左箭头
	left = (By.XPATH,'//div[@id="about"]//a[text()="‹"]')
	#页签
	table_about= (By.XPATH,'//div[@id="about"]//span[@class="page-list" and@style="display: none;"]')
	#已分诊的最后一个患者的报特殊
	re_last_special = (By.XPATH,'//tr[last()]//span[@e_name="index_divid_patients_table_specail"]')

	#特殊患者已被勾选
	arrears_checked = (By.CSS_SELECTOR,'input[type="checkbox"]:checked')
	#特殊患者星标记显示
	special_mark = (By.XPATH,'//table[@id="divid-patients"]//tbody//tr[last()]//span[@class="red"]')


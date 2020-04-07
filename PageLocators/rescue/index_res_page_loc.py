#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: index_res_page_loc.py
# author:gaobo
# time:2019/03/11
from selenium.webdriver.common.by import By
class IndexResPageLoc:
	#点击抢救工作站
	return_res_homepage = (By.ID,'rescue-index-btn')
	# 找到床上的第一个患者名字
	patient_text = (By.XPATH, '//div[@class="wrapBox"]')
	#抢救床上最后一个患者
	patient_last = (By.XPATH, '//div[@class="wrapBox"]')
	#查找待接诊列表患者 找第一个接诊分床按钮
	reception_bed= (By.XPATH, '//tr[@id="datagrid-row-r1-2-0"]//button[text()="接诊分床"]')
	#查找待接诊列表患者 找第一个接诊的患者
	patient_num =(By.XPATH, '//tr[@id="datagrid-row-r1-2-0"]//td[@field="cardnum"]//div')
	#菜单按钮
	menu = (By.XPATH, '//tr[@id="datagrid-row-r1-2-0"]//i')
	#报特殊
	special = (By.ID,'baote')
	#弹窗
	win = (By.ID,'promptmassage')
	#特殊患者
	special_patient = (By.XPATH,'//input[@value="特殊患者"]')
	#确定
	determine = (By.XPATH,'//a[text()="确定"]')
	#欠费患者
	owe_patient= (By.XPATH,'//input[@value="欠费患者"]')
	#报特殊标识
	special_img = (By.XPATH,'//tr[@id="datagrid-row-r1-2-0"]//img')
	#x选择床位的确定按钮
	choose_bed = (By.ID, 'recive')
	#空闲床位
	none_bed = (By.XPATH, '//p[@class="cardDefault"]')

	#切换
	patient_switch = (By.XPATH, '//button[text()="切换"]')
	#签退
	patient_exit = (By.XPATH, '//button[text()="签退"]')
	#待接诊人数
	num_count = (By.ID, 'count')
	#退回分诊
	return_triage = (By.ID, 'tuihuifenzhen')
	#所有病区框
	all_ward = (By.ID,'wardbuttons')
	#病区按钮
	button_ward = (By.ID,'ward_name1')
	#选择病区
	choose_ward = (By.XPATH, '//div[@id="wardbuttons"]//button')





#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: patient_res_page_loc.py
# author:gaobo
# time:2019/03/11
from selenium.webdriver.common.by import By
class PatiengResPageLoc:
	#离开抢救室按钮
	leave_rescue = (By.XPATH,'//p[@onclick="dreliqiang();"]')
	# 离开抢救室弹窗确定按钮
	leave_rescue_win_determine = (By.XPATH, '//div[@id="grabsome"]//button[text()="确定"]')
	#离开抢救室生命体征
	leave_rescue_BP1 = (By.ID, 'leaveBP1')
	leave_rescue_BP2 = (By.ID, 'leaveBP2')
	leave_rescue_SaO2 = (By.ID, 'leaveSaO2')
	leave_rescue_HR = (By.ID, 'leaveHR')
	leave_rescue_R = (By.ID, 'leaveR')
	#抢救结束
	rescue_over = (By.XPATH, '//li[@onclick="rescueMethod()"]')
	#修改按钮
	updselectquxiang= (By.ID, 'updselectquxiang')
	#x按钮
	close = (By.XPATH, '//div[@id="direction"]//button[@class="close"]')
	#去向框
	patient_where = (By.XPATH, '//div[@id="Rescue"]//div[@class="modal-dialog"]')
	#去向的离院
	where = (By.ID, 'qxradio-1005')
	#去向下一步
	determine_where = (By.XPATH, '//div[@id="Rescue"]//button[text()="下一步"]')
	#去向确定
	determine_where_next = (By.XPATH, '//div[@id="next"]//button[text()="确定"]')


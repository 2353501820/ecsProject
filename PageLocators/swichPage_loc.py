#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: swichPage_loc.py
# author:gaobo
# time:2019/03/06
from selenium.webdriver.common.by import By
class SwichPageLoc:

	#身份图片
	img = (By.XPATH,'//img[@class="center-block"]')
	#预检分诊工作站
	triage = (By.XPATH, '//h4[text()="预检分诊工作站"]')

	#抢救工作站
	rescue = (By.XPATH, '//h4[text()="抢救工作站"]')
	#留观工作站
	observation = (By.XPATH, '//h4[text()="留观工作站"]')
	#系统工作站
	system = (By.XPATH, '//h4[text()="系统管理工作站"]')
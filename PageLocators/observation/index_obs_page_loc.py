#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: index_obs_page_loc.py
# author:gaobo
# time:2019/03/08
from selenium.webdriver.common.by import By

class IndexObsPageLoc:
	#找到床上的第一个患者名字
	patient_text = (By.XPATH, '//div[@class="cardContent"]//p[2]')

	#找到空床
	null_beb = (By.XPATH, '//p[@class="cardDefault"]')

	#返回首页
	return_home = (By.XPATH, '//span[text()="急诊观察室护士工作站"]')
	#接诊分床
	receive_separate_bed = (By.XPATH, '//button[text()="接诊分床"]')
	# 接诊分床-确定
	receive_separate_bed_determine = (By.ID,'recive')

	#新增患者
	new_patients = (By.XPATH, '//a[text()="新增患者"]')

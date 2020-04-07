#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: patient_obs_page_loc.py
# author:gaobo
# time:2019/03/08
from selenium.webdriver.common.by import By
class PatiengObsPageLoc:
	#离开留观按钮
	leave_obs = (By.XPATH, '//a[text()="离开留观" and @class="tab9"]')
	#离开留观弹窗确定按钮
	leave_obs_win_determine =  (By.XPATH, '//div[@id="promptModel"]//a[text()="确定"]')

	# 病情跟踪
	illness_tracking = (By.XPATH, '//a[text()="病情跟踪"]')

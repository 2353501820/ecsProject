#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: index_obs_page.py.py
# author:gaobo
# time:2019/03/08
from Common import basepage
from PageLocators.observation.index_obs_page_loc import IndexObsPageLoc as loc

class IndexObsPage(basepage.BasePage):
	#选择患者
	def chooes_patient(self):
		name = '首页-查找患者'
		self.wait_elemVisible(loc.patient_text, model_name=name)
		if self.get_element_text(loc.patient_text,model_name=name):
			self.click_element(loc.patient_text,model_name=name)


	def return_obs_home(self):
		name = "返回首页"
		self.wait_elemVisible(loc.return_home,model_name=name)
		self.click_element(loc.return_home,model_name=name)

	def separate_bed(self):
		pass
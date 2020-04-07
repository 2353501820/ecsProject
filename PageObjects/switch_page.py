#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File:main.py
# Author：GaoBo
# Time:2019/02/28
from PageLocators.swichPage_loc import SwichPageLoc as loc
from Common import basepage
class SwitchPage(basepage.BasePage):

	#判断切换页面有没有工作站存在--根据工作站的图标，看看图标存不存在
	def get_workstation_img(self):
		try:
			self.wait_elemVisible(loc.img,model_name='身份图片')
			return True
		except:
			return False

	#选择预检分诊工作站
	def choose_triage(self):
		self.wait_elemVisible(loc.triage)
		self.click_element(loc.triage)

	#选择抢救工作站
	def choose_rescue(self):
		self.wait_elemVisible(loc.rescue)
		self.click_element(loc.rescue)

	#选择留观工作站
	def choose_observation(self):
		self.wait_elemVisible(loc.observation)
		self.click_element(loc.observation)

	#选择系统管理工作站
	def choose_system(self):
		self.wait_elemVisible(loc.system)
		self.click_element(loc.system)




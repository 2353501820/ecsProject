#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: patient_obs_page.py
# author:gaobo
# time:2019/03/08
from Common import basepage
from PageLocators.observation.patient_obs_page_loc import PatiengObsPageLoc as loc
class PatientObsPage(basepage.BasePage):

	#离开留观室
	def leave_observation(self):
		name = '患者页-离开留观室'
		self.wait_elemVisible(loc.leave_obs,model_name=name)
		self.click_element(loc.leave_obs,model_name=name)
		self.wait_elemVisible(loc.leave_obs_win_determine, model_name=name)
		self.click_element(loc.leave_obs_win_determine, model_name=name)


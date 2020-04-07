#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File:index_obs_page.py
# Author：GaoBo
# Time:2019/03/01
from selenium.webdriver.common.by import By
import time
from PageLocators.triage.index_page_loc import IndexPageLoc as loc
from Common import basepage


class IndexPage(basepage.BasePage):



	def click_newPatient(self):
		name = '首页-新增患者'#点击新增患者
		self.wait_elemVisible(loc.addPatient,model_name = name)
		self.click_element(loc.addPatient,model_name = name)


	def click_historyrecord(self):
		name = '历史记录'#点击历史记录
		self.wait_elemVisible(loc.historyrecord,model_name= name)
		self.click_element(loc.historyrecord,model_name=name )

	def get_historyrecord(self):
		try:	#历史记录有数据就返回TRUE
			self.wait_elemVisible(loc.get_historyrecord)
			return True
		except:
			return False


	def separated_patients_num(self):
		name = '首页-查找已分诊的人数'#查找已分诊的人数
		self.wait_elemVisible(loc.re_evaluate_num,model_name=name)
		time.sleep(1)
		num = self.get_element_text(loc.re_evaluate_num,model_name=name)
		while num == '':
			num = self.get_element_text(loc.re_evaluate_num, model_name=name)
		return int(num)

	def accepted_num(self):
		name = '首页-查找已接诊的人数'#查找已接诊的人数
		self.wait_elemVisible(loc.accepted_num,model_name=name)
		time.sleep(1)
		num = self.get_element_text(loc.accepted_num,model_name=name)
		return int(num)

	def pending_triage_patients_num(self):
		name = '首页-待分诊列表的人数'# 查找待分诊的人数
		self.wait_elemVisible(loc.pending_triage_num,model_name=name)
		time.sleep(0.5)
		num = self.get_element_text(loc.pending_triage_num,model_name=name)
		return int(num)#待分诊的人数

	def special_personnel_num(self):
		name = '首页-查找特殊患者的人数'#查找特殊患者人数
		self.wait_elemVisible(loc.special_personnel_num, model_name=name)
		time.sleep(0.5)
		num = self.get_element_text(loc.special_personnel_num, model_name=name)
		return int(num)



	def return_homepage(self):
		name = '返回首页'#点击返回首页
		time.sleep(0.5)
		self.wait_elemVisible(loc.return_homepage,model_name=name)
		self.click_element(loc.return_homepage,model_name=name)


	def click_alert(self):
		name='报警提示'#点击报警消息提示
		self.wait_elemVisible(loc.alert_msg,model_name=name)
		self.click_element(loc.alert_msg,model_name=name)

	def click_emergency_alert_patient(self):#点击危急报警提示第一个患者
		name = '危急报警提示第一个患者'
		self.wait_elemVisible(loc.emergency_alert_first,model_name=name)
		fullname = self.get_element_text(loc.emergency_alert_first, model_name=name)
		self.click_element(loc.emergency_alert_first,model_name=name)
		return fullname


	def get_alltable_fullname(self):	#获取跳转后的名字
		name = '跳转后的全部table'

		self.wait_elemVisible(loc.all_fullname,model_name=name)
		return self.get_element_text(loc.all_fullname,model_name=name)

	def click_statistical_report(self):	#点击统计报表
		name = '统计报表'
		self.wait_elemVisible(loc.statistical_report, model_name=name)
		self.click_element(loc.statistical_report, model_name=name)

	def click_button(self,locator_id):	#点击带有ID的按钮
		self.wait_elemVisible((By.ID,'{}'.format(locator_id)))
		self.click_element((By.ID,'{}'.format(locator_id)))


	def click_userinfor(self):	#点击个人信息
		self.wait_elemVisible(loc.userinfo,model_name="用户信息")
		self.click_element(loc.userinfo)

	def click_exit(self):	#点击退出
		self.wait_elemVisible(loc.userexit,model_name="退出")
		self.click_element(loc.userexit)

	def click_switch(self):	#点击切换
		self.wait_elemVisible(loc.userswitch,model_name="切换")
		self.click_element(loc.userswitch)

	def click_re_evaluated(self):
		'''
		#点击已分诊
		:return: 
		'''
		self.wait_elemVisible(loc.re_evaluated, model_name="点击已分诊按钮")
		self.click_element(loc.re_evaluated, model_name="点击已分诊按钮")

	def click_emergency_alert_x(self):
		'''
		关掉危急报警弹窗
		:return:
		'''
		self.wait_elemVisible(loc.emergency_alert_x)
		self.click_element(loc.emergency_alert_x)
		time.sleep(1)

	def click_last_special_patient(self):
		'''
		点击最后一个患者的报特殊按钮
		:param num: 
		:return: 
		'''
		self.wait_elemVisible(loc.re_last_special)
		# time.sleep(1)
		self.click_element(loc.re_last_special)


	def click_arrears(self):
		'''
		#标记欠费患者
		:return:
		'''
		name = '欠费患者'
		self.wait_elemVisible(loc.arrears,model_name=name)
		self.click_element(loc.arrears,model_name=name)
		self.click_element(loc.determine_win_special,model_name=name)




	def click_special(self):
		'''
		标记特殊患者
		:return: 
		'''
		name = '特殊患者'
		self.wait_elemVisible(loc.special,model_name=name)
		self.click_element(loc.special,model_name=name)
		self.click_element(loc.determine_win_special,model_name=name)

	def click_arrears_special(self):
		'''
		#同时标记特殊和欠费
		:return:
		'''
		name = '特殊患者和欠费患者'
		self.wait_elemVisible(loc.arrears, model_name=name)
		self.click_element(loc.arrears, model_name=name)
		self.wait_elemVisible(loc.special, model_name=name)
		self.click_element(loc.special, model_name=name)
		self.click_element(loc.determine_win_special, model_name=name)

	def click_accepted(self):
		'''
		点击接诊
		:return: 
		'''
		name = '接诊'
		self.wait_elemVisible(loc.accepted,model_name=name)
		self.click_element(loc.accepted,model_name=name)
		self.wait_elemVisible(loc.determine_win_accepted,model_name=name)
		self.click_element(loc.determine_win_accepted,model_name=name)

	def click_pending_triage_delete(self):
		'''
		点击待接诊-删除
		:return: 
		'''
		name = '删除'
		time.sleep(0.5)
		self.wait_elemVisible(loc.pending_triage_delete,model_name=name)
		self.click_element(loc.pending_triage_delete,model_name=name)

	def click_prompt_message_x(self):
		'''
		点击待接诊-删除X号
		:return: 
		'''
		name = '待接诊-删除X号'
		self.wait_elemVisible(loc.prompt_message_x, model_name=name)
		self.click_element(loc.prompt_message_x, model_name=name)



	def click_prompt_message_cancel(self):
		'''
		点击待接诊-删除-取消按钮
		:return: 
		'''
		name = '待接诊-删除-取消按钮'
		self.wait_elemVisible(loc.prompt_message_cancel, model_name=name)
		self.click_element(loc.prompt_message_cancel, model_name=name)

	def click_prompt_message_detemine(self):	# 点击待接诊-删除-确定按钮
		name = '待接诊-删除-确定按钮'
		self.wait_elemVisible(loc.prompt_message_detemine, model_name=name)
		self.click_element(loc.prompt_message_detemine, model_name=name)



	def click_left(self):#点击向左按钮
		'''
		点击向左翻页按钮
		:return:
		'''
		name = "点击向左翻页按钮"
		time.sleep(1)
		self.wait_elemVisible(loc.left,model_name=name)
		self.click_element(loc.left,model_name=name)


#######断言###########

	def wait_table(self):
		'''
		等待页签
		:return:
		'''
		name ='等待待分诊页签出现'
		try:
			self.wait_elemVisible(loc.table_about,model_name=name)
			return True
		except:
			return False


	def prompt_message_cancel(self):	#
		'''
		待接诊删除按钮后的弹窗是否消失，消失返回TRUE
		:return: 
		'''
		name = '待接诊-删除提示消息框'
		try:
			self.wait_elemVisible(loc.prompt_message, model_name=name)

			return True
		except:
			return False

	def special_choose(self):
		'''
		特殊患者的欠费患者是否被选中
		:return:
		'''
		name ='欠费患者是否被选中'
		try:
			self.wait_elemVisible(loc.arrears, model_name=name)
			self.wait_elemVisible(loc.arrears_checked,model_name=name)
			return True
		except:
			return False


	def special_mark(self):
		'''
		特殊患者的标记是否显示
		:return:
		'''
		name ='特殊患者的标记显示'
		try:
			self.wait_elemVisible(loc.special_mark,model_name=name)
			return True
		except:
			return False






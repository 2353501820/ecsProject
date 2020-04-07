#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: basepage.py
# author:gaobo
# time:2019/03/07


from Common.myloging import Logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Common.path import screenshots_dir
import os

import time
from selenium.webdriver.support.select import Select
class BasePage:
	loging = Logging()
	def __init__(self,driver):
		self.driver = driver

	def wait_elemVisible(self,locator,timeout=10,model_name='model'):
		'''
		等待元素可见
		:param locator: 元素表达式
		:param timeout: 等待超时时间
		:param model_name:进行的模块
		:return:
		'''
		self.loging.info('等待元素：{}'.format(locator))
		try:
			WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
			self.loging.info('找到元素')
		except:
			#写日志
			self.loging.exception('等待元素超时!')
			#截图
			self.save_webImg(model_name)
			raise


	def get_element(self,locator,model_name='model'):
		'''
		查找一个元素
		:param locator: 元素表达式
		:param model_name:进行的模块
		:return:返回查到的元素
		'''
		self.loging.info('查找{}下的元素:{}'.format(model_name,locator))
		try:
			ele = self.driver.find_element(*locator)

			self.loging.info('查找成功')
			return ele
		except:
			self.loging.exception('查找元素失败！！')
			# 截图
			self.save_webImg(model_name)
			raise

	def get_elements(self,locator,model_name='model'):
		'''
		查找多个元素
		:param locator: 元素表达式
		:param model_name:进行的模块
		:return:
		'''
		self.loging.info('查找{}下的元素:{}'.format(model_name,locator))
		try:
			ele = self.driver.find_elements(*locator)
			self.loging.info('查找成功')
			return ele
		except:
			self.loging.exception('查找元素失败！！')
			# 截图
			self.save_webImg(model_name)
			raise

	def click_element(self,locator,model_name='model'):
		'''
		点击操作
		:param locator: 元素表达式
		:param model_name:进行的模块
		:return:
		'''
		#元素查找
		ele = self.get_element(locator,model_name)
		self.loging.info('点击操作：{}下的元素{}'.format(model_name,locator))
		#元素点击
		try:
			ele.click()
		except:
			self.loging.exception('点击元素失败！')
			# 截图
			self.save_webImg(model_name)
			raise

	def input_text(self,locator,value,model_name='model'):
		'''
		输入文本操作
		:param locator: 元素定位表达式
		:param model_name:进行的模块
		:return:
		'''
		ele = self.get_element(locator, model_name)
		self.loging.info('输入操作：{}下的元素{}输入{}'.format(model_name, locator,value))
		try:
			ele.send_keys(value)
		except:
			self.loging.exception('输入失败！')
			# 截图
			self.save_webImg(model_name)
			raise

	def get_element_attribute(self,locator,attribute,model_name='model'):
		'''
		获取单个元素的属性值
		:param locator: 元素定位表达式
		:param attribute: 元素属性
		:param model_name: 进行的模块
		:return: 元素属性值
		'''
		ele = self.get_element(locator,model_name)
		self.loging.info('操作：{}下的元素{}的属性{}'.format(model_name,locator,attribute))
		try:
			return ele.get_attribute(attribute)
		except:
			self.loging.exception('获取元素属性失败！')
			# 截图
			self.save_webImg(model_name)
			raise
	def get_attribute(self,ele,attribute,model_name='model'):
		'''
		获取元素的属性值
		:param locator: 元素定位表达式
		:param attribute: 元素属性
		:param model_name: 进行的模块
		:return: 元素属性值
		'''
		try:
			return ele.get_attribute(attribute)
		except:
			self.loging.exception('获取元素属性失败！')
			# 截图
			self.save_webImg(model_name)
			raise



	def get_element_text(self, locator, model_name='model'):
		'''
		获取元素文本
		:param locator: 元素定位表达式
		:param model_name: 进行的模块
		:return: 元素文本值
		'''
		# 元素查找
		ele = self.get_element(locator, model_name)
		self.loging.info('操作：{}下的元素{}的文本'.format(model_name, locator))
		# 属性获取
		try:
			return ele.text
		except:
			self.loging.exception('获取元素文本失败！')
			# 截图
			self.save_webImg(model_name)
			raise

	def select_by_value(self,locator,value,model_name='model'):
		'''
		select元素下拉框的选择，根据value值
		:param locator: 元素定位表达式
		:param value: 元素value值
		:param model_name: 进行的模块
		:return:
		'''
		ele = self.get_element(locator, model_name)
		self.loging.info('选择操作：{}下的元素{}选择{}'.format(model_name, locator,value))
		try:
			Select(ele).select_by_value(value)
		except:
			self.loging.exception('选择下拉框value值失败！')
			# 截图
			self.save_webImg(model_name)
			raise

	def select_by_index(self,locator,index,model_name='model'):
		'''
		select元素下拉框的选择，根据index索引值
		:param locator: 元素定位表达式
		:param index: 下拉框index值
		:param model_name: 进行的模块
		:return:
		'''
		ele = self.get_element(locator, model_name)
		self.loging.info('选择操作：{}下的元素{}的第一个option'.format(model_name, locator))
		try:
			Select(ele).select_by_index(index)
		except:
			self.loging.exception('选择下拉框value值失败！')
			# 截图
			self.save_webImg(model_name)
			raise

	def swtich_window(self,str='',index=None):
		'''
		浏览器窗口切换，根据传入的index数字，切换到第index窗口
		:param str:如果传new，就切换到新窗口
		:param index:写什么数字就切这个数字的窗口
		:return:
		'''
		if str == 'new':
			# 等待新窗口出现
			time.sleep(2)
			windows = self.driver.window_handles
			#再去切换
			self.driver.switch_to.window(windows[-1])
		else:
			#获取所有的窗口
			windows = self.driver.window_handles
			if index !=None and 0 <= int(index) < len(windows):
				self.driver.switch_to.window(windows[int(index)])
				#切换到index下标的窗口



	def swtich_alert(self,timeout=30,poll_frequency=0.5 ,action='accept', model_name='model'):
		'''
		alert弹窗切换
		:param timeout:等待弹窗认30秒
		:param poll_frequency: 轮寻0.5秒找弹窗
		:param action: 默认accept，传别的值就取消关闭
		:param model_name: 进行的模块
		:return: alert弹窗的文本
		'''
		self.loging.info('等待弹窗')
		try:
			WebDriverWait(self.driver,timeout,poll_frequency).until(EC.alert_is_present())
			self.loging.info('找到弹窗')
			# #关闭弹窗
			alert = self.driver.switch_to.alert
			text = alert.text
			self.loging.info('获取到文本')
			if action == 'accept':
				alert.accept()
				self.loging.info('点确定关闭弹窗')
			else:
				alert.dismiss()
				self.loging.info('点取消关闭弹窗')
			return text
		except:
			# 写日志
			self.loging.exception('切换失败超时!')
			# 截图
			self.save_webImg(model_name)
			raise

	def swtich_iframe(self,iframe_name,timeout=30,poll_frequency=0.5,model_name='model'):
		'''
		iframe弹窗切换，先等待iframe出现并切换过去
		:param iframe_name: iframe弹窗id
		:param timeout:等待弹窗认30秒
		:param poll_frequency:轮寻0.5秒找弹窗
		:param model_name:进行的模块
		:return:
		'''
		try:
			WebDriverWait(self.driver,timeout,poll_frequency).until(EC.frame_to_be_available_and_switch_to_it(iframe_name))
			time.sleep(0.5)
			self.loging.info('切换成功')
			#self.driver.switch_to.default_content()    #回到默认页面，看需求使用
		except:
			# 写日志
			self.loging.exception('切换失败')
			# 截图
			self.save_webImg(model_name)
			raise

	def save_webImg(self, model_name):
		'''
		截图类，让别的类调用可以截浏览器窗口图
		:param model_name:
		:return:
		'''
		file_path = screenshots_dir + '/{0}_{1}.png'.format(model_name, time.strftime("%Y-%m-%d_%H_%M_%S",
																  time.localtime(time.time())))
		try:
			sd = os.listdir(screenshots_dir)
			if len(sd)>10:#目录下文件超过10个就删掉
				for i in sd :
					c_path = os.path.join(screenshots_dir, i)
					os.remove(c_path)
			self.driver.save_screenshot(file_path)
			self.loging.info('截图成功，文件路径是：{}'.format(file_path))
		except:
			self.loging.exception('截图失败！')
			raise
	def assert_displayed(self,locator, model_name):
		'''
		判断元素是否可见
		:return:
		'''
		try:
			ele =self.get_element(locator,model_name=model_name)
			self.loging.info('开始判断元素是否可见')
			if ele.is_displayed():
				self.loging.info('元素可见')
				return True
			else:
				self.loging.info('元素不可见')
				return False
		except:
			# 写日志
			self.loging.exception('判断失败')
			# 截图
			self.save_webImg(model_name)
			raise



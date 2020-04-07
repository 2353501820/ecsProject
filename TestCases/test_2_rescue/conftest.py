#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: conftest.py
# author:gaobo
# time:2019/03/19
import pytest
from selenium import webdriver
from TestData import common_data as CD
from TestData import login_data as LD
from PageObjects.login_page import LoginPage
from PageObjects.switch_page import SwitchPage
from PageObjects.rescue.index_res_page import IndexResPage


@pytest.fixture
def common_env():
	print("-------这是测试函数级别的fixture-------")
	driver = webdriver.Chrome()
	driver.get(CD.login_url)
	# driver.maximize_window()
	driver.set_window_size(1440,900)
	# 登录系统
	LoginPage(driver).login(CD.uesname, CD.passward)
	# 选择分诊工作站
	SwitchPage(driver).choose_rescue()
	yield driver
	driver.quit()

driver = None
@pytest.fixture(scope='class')
def class_env():
	global driver
	driver = webdriver.Chrome()
	driver.get(CD.login_url)
	# driver.maximize_window()
	driver.set_window_size(1440, 900)
	# 登录系统
	LoginPage(driver).login(CD.uesname, CD.passward)
	# 选择分诊工作站
	SwitchPage(driver).choose_rescue()
	yield driver
	driver.quit()
@pytest.fixture
def fun_env():

	yield
	IndexResPage(driver).return_res_homepage()



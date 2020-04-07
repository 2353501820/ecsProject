#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: conftest.py
# author:gaobo
# time:2019/03/19
import pytest
from selenium import webdriver
from TestData import common_data as CD
import time
# driver = None
# @pytest.fixture(scope="class")
# def class_env_common():
# 	global driver
# 	driver = webdriver.Chrome()
# 	driver.get(CD.login_url)
# 	driver.maximize_window()
# 	yield  driver
# 	driver.quit()
# 	pass
#
# @pytest.fixture
# def function_env_common():
# 	print("-------这是测试函数级别的fixture-------")
# 	driver = webdriver.Chrome()
# 	driver.get(CD.login_url)
# 	driver.refresh()
# 	driver.maximize_window()
# 	yield driver
# 	driver.quit()

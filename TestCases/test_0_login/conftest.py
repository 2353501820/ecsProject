#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: conftest.py
# author:gaobo
# time:2019/03/19
import pytest
from selenium import webdriver
from TestData import common_data as CD
import time
driver = None
@pytest.fixture(scope="class")
def class_env():
	global driver
	# print("-------这是测试类级别的fixture--------")
	driver = webdriver.Chrome()
	driver.get(CD.login_url)

	driver.set_window_size(1440, 900)
	yield  driver
	driver.quit()


@pytest.fixture
def function_env():
	# print("-------这是测试函数级别的fixture--------")
	yield
	driver.refresh()
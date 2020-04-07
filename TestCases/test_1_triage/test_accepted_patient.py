#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: test_accepted_patient.py
# author:gaobo
# time:2019/03/20

from PageObjects.triage.index_page import IndexPage

import pytest
@pytest.mark.usefixtures('function_env')
@pytest.mark.usefixtures('class_env')
class TestAcceptedPatient:
	'''
	测试接诊功能，并测试统计已接诊的人数变化
	'''

	@pytest.mark.results
	def test_accepted(self,class_env):
		lp = IndexPage(class_env)
		# 点击已分诊
		lp.click_re_evaluated()
		# 获取已分诊人数
		num = lp.accepted_num()
		#点击接诊
		lp.click_accepted()
		#再次获取已分诊人数
		num_new = lp.accepted_num()
		#断言已分诊人数是否有-1
		assert num + 1 == num_new


if __name__ == '__main__':
	pytest.main(['test_accepted_patient.py'])
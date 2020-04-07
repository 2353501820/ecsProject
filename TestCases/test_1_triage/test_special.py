#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: test_special.py
# author:gaobo
# time:2020/03/27
import pytest
from PageObjects.triage.index_page import IndexPage


@pytest.mark.usefixtures('function_env')
@pytest.mark.usefixtures('class_env')
class TestSpecial:
	'''
	测试报特殊和修改
	'''
	def test_soecial(self,class_env):
		ip =IndexPage(class_env)
		ip.click_re_evaluated()
		ip.click_emergency_alert_x()
		ip.click_last_special_patient()
		ip.click_arrears()
		assert  ip.special_mark()
		# ip.click_last_special_patient()
		# assert ip.special_choose()



if __name__ == '__main__':
    pytest.main(['test_special.py'])



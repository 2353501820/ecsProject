#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: test_4_pending_triage_delete.py
# author:gaobo
# time:2019/03/21
'''
待分诊删除功能
1、点击X号
2、点击取消
3、、点击确定
'''
import pytest
from PageObjects.triage.index_page import IndexPage
@pytest.mark.usefixtures('class_env')
@pytest.mark.usefixtures('function_env')
class TestPendingTriageDelete:

	#待分诊删除-X功能
	def test_prompt_message_x(self, class_env):
		lp = IndexPage(class_env)
		# 点击待分诊删除
		lp.click_pending_triage_delete()
		# 点击弹窗X号
		lp.click_prompt_message_x()
		lp.click_pending_triage_delete()
		# 点击弹窗取消按钮
		lp.click_prompt_message_cancel()
		# assert lp.prompt_message_cancel()	# 判断弹窗是否取消
		num = lp.pending_triage_patients_num()
		# 点击待分诊删除
		lp.click_pending_triage_delete()
		# 点击弹窗确定按钮
		lp.click_prompt_message_detemine()
		# 查找下待分诊人数
		num_new = lp.pending_triage_patients_num()
		# 判断待分诊人数是否-1
		assert num - 1 == num_new



if __name__ == '__main__':
	pytest.main(['test_4_pending_triage_delete.py'])
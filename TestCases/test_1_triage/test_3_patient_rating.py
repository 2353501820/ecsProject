# -*- coding: utf-8 -*-
'''
----------------------
file : test_3_patient_rating.py
author : gaobo
time : /09:24
----------------------
'''
import pytest
from PageObjects.triage.index_page import IndexPage
from PageObjects.triage.patient_rating_page import PatientRating
from PageObjects.triage.new_patient_page import NewPatient
from PageObjects.triage.index_page import IndexPage

@pytest.mark.usefixtures('class_env')
@pytest.mark.usefixtures('function_env')
class TestPatientRating:
	"""
	评级相关
	"""


	def test_rating_patientpage_mod(self,class_env):
		'''
		测试修改评级是否修改成功，首页是否有改字，
		:param class_env:
		:return:
		'''
		ip = IndexPage(class_env)
		pr = PatientRating(class_env)
		ip.click_re_evaluated()  # 点击已分诊
		ip.click_emergency_alert_x()  # 关掉危急提示窗
		pr.chick_rating_mod()
		ip.click_emergency_alert_x()  # 关掉危急提示窗
		before_num = pr.get_rating_num()
		pr.again_rating()  # 再次评级操作

		pr.click_grade()  # 点击评级
		pr.mod_grade()# 击修成成2级，确定
		assert pr.assert_patient_mod() #验证患者页是否有改字
		NewPatient(class_env).patient_save()  # 点击保存
		ip.click_emergency_alert_x()  # 关掉危急提示窗
		ip.click_re_evaluated()  # 点击已分诊
		if ip.wait_table()==False:
			ip.click_left()
		assert pr.assert_index_mod(), '测试执行失败，首页未找到改字'  # 首页是否有改字
		# lp.click_re_evaluated()  # 点击已分诊
		pr.chick_rating_mod()  # 点击最新的患者的修改评级
		ip.click_emergency_alert_x()  # 关掉危急提示窗
		new_num = pr.get_rating_num()
		assert before_num +1 == new_num , '执行失败，患者再次分级测试失败'


if __name__ == '__main__':

	pytest.main(['test_3_patient_rating.py'])


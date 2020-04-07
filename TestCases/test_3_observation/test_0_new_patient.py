# -*- coding: utf-8 -*-
'''
----------------------
file : test_0_new_patient.py
author : gaobo
time : /19:32
----------------------
'''
from PageObjects.observation.registration_obs_page import RegistrationObsPage
import pytest
from TestData.patient_data import datas_save
@pytest.mark.usefixtures('function_env')
@pytest.mark.usefixtures('class_env')
class TestNewPatient:
	@pytest.mark.parametrize('data',datas_save)
	def test_new_patient(self,class_env,data):#新增患者
		reg_obs = RegistrationObsPage(class_env)
		#点击新增患者
		reg_obs.click_new_patients()
		#输入数据
		reg_obs.input_data_newpatient(data['cardnum'], data['fullname'])
		#保存
		reg_obs.reg_save()
		assert reg_obs.save_suc()


if __name__ == '__main__':
	pytest.main(['test_0_new_patient.py'])


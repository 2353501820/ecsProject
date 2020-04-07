# -*- coding: utf-8 -*-
'''
----------------------
file : patient_info_page_loc.py
author : gaobo
time : /10:06
----------------------
'''
from selenium.webdriver.common.by import By
class PatientInfoPageLoc:
	grade = (By.ID,'grade') #分级按钮
	grade_1004 =(By.ID,'1004')  #修改2级
	grade_changereason = (By.ID,'changereason')#修改原因
	grade_ok = (By.ID,'okbtn')
	grade_mod = (By.XPATH,'//p[text()="改"]')
	again_rating = (By.XPATH,'//p[text()=">"]')
	again_rating_button = (By.XPATH,'//button[text()="再次评级"]')
	again_rating_button_ok = (By.XPATH,'//*[@id="read"]//button[text()="确认"]')
	reting_num = (By.ID,'handle3')
	index_divid_patients_table_edit = (By.XPATH,'//table[@id="divid-patients"]//tr[last()]//td[last()]//span[@e_name="index_divid_patients_table_edit"]')#最后一个患者的查看和修改按钮
	table_change_label = (By.XPATH,'//*[@id="divid-patients"]//tr[last()]//span[text()="改"]')

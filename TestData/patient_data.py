#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: patient_data.py
# author:gaobo
# time:2019/03/05

from Common.mysql import MysqlQuery
from Common.tool import Tool
from  faker import Faker
fake =Faker("zh_CN")
sql =MysqlQuery()
#批量加患者的数据

datas_save = [
{"cardnum":sql.cardnum(),"fullname":fake.name(),"birthday":fake.date(pattern="%Y-%m-%d")},
]
#暂存患者的数据

datas_draf = [
	{"cardnum":sql.cardnum(),"fullname":fake.name(),"birthday":fake.date(pattern="%Y-%m-%d")}
]
#突发公共事件的数据
datas_event_draf = [
	{"cardnum":sql.cardnum(),"fullname":fake.name()}
]
datas_event_save = [
	{"cardnum":sql.cardnum(),"fullname":fake.name()}
]

#留观登记数据
class PatientData:
	gender = '男'
	diagnosis = fake.word()#诊断
	address = fake.address()#通讯地址
	doctor_name = fake.last_name()#留观医生
	birthday = fake.date(pattern="%Y-%m-%d")#生日
	idcard = '320723198002203025'#身份证号
	phone = fake.phone_number()#手机号
	allergic_history = fake.word()  #药物过敏史
	parenttel =fake.phone_number()#患者家属电话
	memberstel =fake.name()#紧急联系人
	tz = '200'#体重
	sg = '190'#身高
	reason= fake.sentence(nb_words=6,variable_nb_words=True)#来院原因
	note = fake.word() #备注
	maibo = '55'
	spo2 = '93'
	shousuoya ='150'
	shuzhangya ='80'
	tiwen = '37.5'


if __name__ == '__main__':
	print(datas_draf)




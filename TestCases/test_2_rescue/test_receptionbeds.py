#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: test_receptionbeds.py
# author:gaobo
# time:2019/03/15
from TestData import login_data as LD
from PageObjects.login_page import LoginPage
from PageObjects.switch_page import SwitchPage
from PageObjects.rescue.index_res_page import IndexResPage
from PageObjects.rescue.patient_res_page import PatientResPage
import pytest
@pytest.mark.usefixtures("class_env")
@pytest.mark.usefixtures("fun_env")
class TestReceptionBed:

	pass





if __name__ == '__main__':
	pytest.main(['-m','test_return_triage'])
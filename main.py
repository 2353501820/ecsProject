#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File:main.py
# Author：GaoBo
# Time:2019/02/28
import pytest

# pytest.main(["--html=OutPut/reports/report.html","--reruns","2","--alluredir=OutPut/allure/"])

pytest.main(["--html=OutPut/reports/report.html","--reruns","2"])
# pytest.main(['-m','results'])


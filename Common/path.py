#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: path.py
# author:gaobo
# time:2019/03/07
import os
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

log_dir = os.path.join(base_dir,'OutPut','log')

reports_dir = os.path.join(base_dir,'OutPut','reports')

screenshots_dir = os.path.join(base_dir,'OutPut','screenshots')




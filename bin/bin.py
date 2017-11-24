  # -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/23 0023

import sys,os
dirname=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dirname)
# print(dirname)

from module_m import main
main.main()
# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/24 0024

import json
acc_dic = {
    'id':1234,
    'password':'abc',
    'credit':15000,
    'balance':15000,
    'enroll_date':'2017-10-1',
    'expire_date':'2021-10-1',
    'pay_day':22,
    'status':0
}


print(json.dumps(acc_dic))
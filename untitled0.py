# -*- coding: utf-8 -*-
"""
Created on Sun May 16 10:47:14 2021

@author: user
"""

import csv
fn = "tbike.csv"
with open(fn,encoding = ('utf-8')) as fo:
    data = csv.DictReader(fo)
    for row in data:
        print('站名：',row['StationName'])
        print('可借：',row['AvaliableBikeCount'])
        print('可停：',row['AvaliableSpaceCount'])
    
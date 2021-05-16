# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:54:46 2021

@author: user
"""

import csv
fn = 'lcc4.csv'
with open(fn,'a',newline='',encoding=('utf-8')) as fo:
    fields = ['姓名','性別','電話','學校']
    csvobj = csv.DictWriter(fo,fieldnames=fields)
    csvobj.writeheader() #寫入標題
    csvobj.writerow({'姓名':'王大同','性別':'男','電話':'0912486256','學校':'台中科技大學'})
    csvobj.writerow({'姓名':'王美美','性別':'女','電話':'0952455242','學校':'中興大學'})
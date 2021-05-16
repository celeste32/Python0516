# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:23:29 2021

@author: user
"""

import csv
fn = 'lcc.csv'
with open(fn,'a',newline='',encoding=('utf-8')) as fo:
    csvobj = csv.writer(fo)
    csvobj.writerow(['姓名','性別','電話'])
    csvobj.writerow(['Nemo','Male','998462'])
    csvobj.writerow(['Molly','Female','456513'])
    csvobj.writerow(['Tom','Male','879231'])
    csvobj.writerow(['Tony','Male','754133'])
    
import csv
fn = 'lcc2.csv'
with open(fn,'a', encoding=('utf-8')) as fo:
    csvobj = csv.writer(fo)
    csvobj.writerow(['姓名','性別','電話'])
    csvobj.writerow(['Nemo','Male','998462'])
    csvobj.writerow(['Molly','Female','456513'])
    csvobj.writerow(['Tom','Male','879231'])
    csvobj.writerow(['Tony','Male','754133'])
    
import csv
fn = 'lcc3.csv'
with open(fn,'a', encoding=('utf-8')) as fo: #sig是加上BOM(編首)位元順序
    csvobj = csv.writer(fo)
    csvobj.writerow(['姓名','性別','電話'])
    csvobj.writerow(['Nemo','Male','998462'])
    csvobj.writerow(['Molly','Female','456513'])
    csvobj.writerow(['Tom','Male','879231'])
    csvobj.writerow(['Tony','Male','754133'])
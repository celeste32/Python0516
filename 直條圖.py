# -*- coding: utf-8 -*-
"""
Created on Sun May 16 15:44:02 2021

@author: user
"""

import openpyxl
from openpyxl.chart import BarChart,Reference
wb = openpyxl.Workbook()
ws = wb.active
data = [['地區','人次'],['美國',9800],['中國',8700],['臺灣',1200],['日本',7600]]
for row in data:
    ws.append(row)
chart = BarChart()
chart.title = '全球富豪人數'
item = Reference(ws,min_col=2,min_row=1,max_row=5)
chart.add_data(item,titles_from_data=True)
labels = Reference(ws,min_col=2,min_row=1,max_row=5)
chart.set_categories(labels)
ws.add_chart(chart,'E1')
wb.save('barchart.xlsx')
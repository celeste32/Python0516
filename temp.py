# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import datetime
import time
def writelog(Error):
    
    dirpath = "C://mylog" #dir=目錄縮寫
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    
    today = datetime.datetime.strftime(datetime.datetime.now(),'%Y/%m/%d %H:%M:%S')
    filename = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d')
    filename = dirpath + '//' + filename + ".log"
    with open(filename,'a',encoding = ('utf-8')) as fo:
        msg = today + '-原因：' + Error + '\n'
        fo.write(msg)
writelog("狀態顯示正常寫入")

data = [10,20,30,40]
try:
    print(data[1])
    print(data[10])
    print(data[3])
except Exception as ex:
    writelog(str(ex))
    

# -*- coding: utf-8 -*-
"""
Created on Sun May 16 15:51:08 2021

@author: user
"""
#圖表要到右邊的plot查看
import matplotlib.pyplot as plt #Python裡的圖表
score = [20,60,90,30,70,68]
plt.plot(score,color='red',linewidth=3)
plt.show()

score1 = [10,54,57,97,64,25]
plt.plot(score1,linewidth=3,marker='x')
plt.show()

score2 = [30,44,87,97,44,65]
plt.plot(score2,linewidth=3,linestyle='--',color='green')
plt.show()
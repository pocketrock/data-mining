#-*- coding: utf-8 -*-
#对数据进行基本的探索
#返回缺失值个数以及最大最小值


# -*- coding:UTF-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import sys                    #导入sys模块
sys.path.append('../code/')    #要用绝对路径
print(sys.path)
import norma


datafile= '../tmp/missing_data_processed.xls' #航空原始数据,第一行为属性标签

#基本信息
data = pd.read_excel(datafile,index_col=u'次数') #读取原始数据


explore = data.describe()
print(explore)




#箱型图
import matplotlib.pyplot as plt #导入图像库
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
#plt.ylim(ymin=-20000,ymax=150000)


plt.figure() #建立图像
p = data.boxplot() #画箱线图，直接使用DataFrame的方法
new_ticks = np.linspace(0, 100000, 10)
plt.yticks(new_ticks)
#plt.ylim([0,150000]);
#x = p['fliers'][0].get_xdata() # 'flies'即为异常值的标签
#y = p['fliers'][0].get_ydata()
#y.sort() #从小到大排序，该方法直接改变原对象
plt.show() #展示箱线图





#
# describe2=data['人大'].describe()
#
#
# IQR = describe2[6] - describe2[4]
#
# errorup = describe2[6] + 1.5 * IQR
#
# errordown = describe2[4] - 1.5 * IQR
#
# range = (errordown,errorup)
#
# print(range)
#
# norm=norma.check_normality(data['人大'])
#
# print (norm)
#
# describe2=data['人大'].describe()
#

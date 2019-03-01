#!/usr/bin/env python
#  -*- coding:utf-8 -*-
from xlrd import open_workbook as owb
import matplotlib.pyplot as plt
#import matplotlib.colors as colors
#from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FuncFormatter
import numpy as np
#!/usr/bin/python
# -*- coding: GBK -*-
import re
from numpy import *
import operator
from os import listdir
import xlrd
from xlwt import *
import xlutils.copy
from xlutils.copy import copy
import os
import numpy as np
import pandas as pd
import xlwt
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties



def main():
    datafile = '../tmp/data_processed.xls'
    wb = xlrd.open_workbook(filename=datafile)
    sheet1 = wb.sheet_by_index(0)


    list1=[]
    for i in range(1, sheet1.nrows):
         list1.append(sheet1.cell(i, 1).value)

    list2=[]
    for i in range(1, sheet1.nrows):
         list2.append(sheet1.cell(i, 2).value)


    list3=[]
    for i in range(1, sheet1.nrows):
         list3.append(sheet1.cell(i, 3).value)


    list4=[]
    for i in range(1, sheet1.nrows):
         list4.append(sheet1.cell(i, 4).value)


    list5=[]
    for i in range(1, sheet1.nrows):
         list5.append(sheet1.cell(i, 5).value)


    plt.bar([1, 2, 3, 4, 5, 6, 7],list1, label='RUC')
    plt.bar([8, 9, 10, 11, 12, 13, 14],list2, label='pku')
    plt.bar([15, 16, 17, 18, 19, 20, 21],list3, label='BNU')
    plt.bar([22, 23, 24, 25, 26, 27, 28],list4, label='BUAA')
    plt.bar([29, 30, 31, 32, 33, 34, 35],list5, label='TSING')

    plt.legend()

    plt.xlabel('year')
    plt.ylabel('number')



    plt.show()
def  mmm():
    datafile = '../tmp/data_processed.xls'
    wb = xlrd.open_workbook(filename=datafile)
    sheet1 = wb.sheet_by_index(0)
    number0 = 0
    number1 = 0
    number2 = 0
    number3 = 0
    number4 = 0

    list1 = []
    for i in range(1, sheet1.nrows):
        list1.append(sheet1.cell(i, 1).value)
        number0 += sheet1.cell(i, 1).value

    list2 = []
    for i in range(1, sheet1.nrows):
        list2.append(sheet1.cell(i, 2).value)
        number1 += sheet1.cell(i, 2).value

    list3 = []
    for i in range(1, sheet1.nrows):
        list3.append(sheet1.cell(i, 3).value)
        number2 += sheet1.cell(i, 3).value

    list4 = []
    for i in range(1, sheet1.nrows):
        list4.append(sheet1.cell(i, 4).value)
        number3 += sheet1.cell(i, 4).value

    list5 = []
    for i in range(1, sheet1.nrows):
        list5.append(sheet1.cell(i, 5).value)
        number4 += sheet1.cell(i, 5).value
    SD=[108156.5412,	182032.7497,	114650.7263,	81003.13884,	250248.5565]

    plt.bar([1, 2,3, 4,5], [number0,number1,number2,number3,number4], yerr= SD, error_kw={'ecolor': '0.2', 'capsize': 6}, alpha=0.7,label = 'First')


    plt.legend()

    plt.xlabel('year')
    plt.ylabel('number')



    plt.show()
if __name__ == '__main__':
    main()
    mmm()
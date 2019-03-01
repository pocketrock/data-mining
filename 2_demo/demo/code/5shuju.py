
import xlrd
from datetime import date,datetime
import xlrd
from datetime import date,datetime
import pandas as pd
import types
import string
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


def main(ww):
    datafile= '../tmp/missing_data_processed.xls'
    wb = xlrd.open_workbook(filename=datafile)
    sheet1 = wb.sheet_by_index(0)

    #date_value = xlrd.xldate_as_tuple(sheet1.cell_value(2,1),wb.datemode)
    #print(date_value)
    #print(date_value[0])
    #print(date_value[1])
    #print(date_value[2])
    #print(date(*date_value[0:3]))
    #print(date(*date_value[:3]).strftime('%Y/%m/%d'))

    xlist=[

    [2011, 0],
    [2012, 0],
    [2013, 0],
    [2014, 0],
    [2015, 0],
    [2016, 0],
    [2017, 0],
    ]

    print(xlist[1][0])
    print(len(xlist))
    for i in range  (1,sheet1.nrows):
       # for j in range (sheet1.ncols) :

               date_value = xlrd.xldate_as_tuple(sheet1.cell(i, ww).value, 0)
              # xlist.append(date_value[0:3])
               for j in range (0,len(xlist)):
                  if(date_value[0]==xlist[j][0]):
                      xlist[j][1]= xlist[j][1]+ sheet1.cell(i, ww+1).value;

    for jhh in range(0, len(xlist)):

        rb = xlrd.open_workbook('../tmp/data_processed.xls', formatting_info=True)

        wb = xlutils.copy.copy(rb)
        ws = wb.get_sheet(0)

        ws.write(jhh,ww+1,xlist[jhh][1])
       # ws.write()
        wb.save("../tmp/data_processed.xls")

        print(xlist)
    #for i in xlist:
       # print(i )
if __name__ == '__main__':
  main(1)
  main(3)
  main(5)
  main(7)
  main(9)
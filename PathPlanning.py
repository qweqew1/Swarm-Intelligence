import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import random
import copy
from matplotlib import colors


9

'''
# --------------------------------PATHPLANNING函数包------------------------------------
# =====Tips1:输入参数矩阵尺寸为[0-->rows]的所有个数，非rows的最大下标
# =====Tips2:区别行列矩阵，行列坐标，和XY坐标
# =====Tips3:在不同表示系，sz均为行列尺寸，即sz=[rows,cols],在XY坐标坐标系中sz=[leny,lenx]
#
# # sub2coord(possub)函数，输入单个行列位置，输出单个行列坐标位置(数组)
# # coord2sub(posxy)函数，输入单个行列坐标位置，输出单个行列位置(数组)
# # xy2sub(sz,x,y)函数，输入尺寸、x坐标和y坐标，输出行列位置(数组)
# # sub2xy(sz,r,c)函数，输入尺寸、XY坐标行位置和列位置，输出xy位置(数组)
# # sub2ind(sz,r,c)函数，输入尺寸，行位置和列位置，输出对应的线性索引值(从0开始)
# # ind2sub(sz,ind)函数，输入尺寸和线性索引值，输出矩阵位置(数组)
# ----------------------------------------------------------------------------------------
'''




'''
# sub2coord和coord2sub函数，行列坐标系内，行列位置和坐标位置相互转换
# 其中的【行列坐标系】形式如图所示，从0开始，因为Python数组下标从0开始，Y方向沿下递增
#
#                   0 1 2 3 4
#                0+---------->X(X=cols)
#                1|
#                2|
#                3|
#               Y(Y=rows)
'''
def sub2coord(possub):
    posx = possub[1]
    posy = possub[0]
    return [posx, posy]


def coord2sub(posxy):
    posr = posxy[1]
    posc = posxy[0]
    return [posr, posc]


'''
# xy2sub和sub2xy函数，坐标系XY位置转换为矩阵格式的转换函数
# ++++sz为坐标尺寸，即元素个数，非最大坐标值
# 其中的XY形式如图所示，从0开始，到[sz]-1为止
#
#                Y/
#                3|
#                2|
#                1|
#                0+---------->X
#                   0 1 2 3 4
'''
def xy2sub(sz, x, y):
    r = sz[0]-1-y
    c = x
    return [r, c]


def sub2xy(sz, r, c):
    x = c
    y = sz[0]-1-r
    return [x, y]


'''
# sub2ind和ind2sub函数，将行列位置转换为索引位置
# 行列位置和索引关系，对应如图所示
#
#                   0 1 2 3 4
#                0+---------->cols
#                1| 0 3 6 ...
#                2| 1 4 7 ...
#                3| 2 5 8 ...
#               rows
'''

def sub2ind(sz,r,c):
    ind = c*sz[0]+r
    return ind


def ind2sub(sz,ind):
    c = int(ind/sz[0])
    r = ind-c*sz[0]
    return [r,c]


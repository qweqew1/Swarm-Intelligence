import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors
from matplotlib import animation
import matplotlib.patches as pc
import copy
import random

import PathPlanning


'''
# ----------------------------------------------------------------------------------------------
# 绘制动态地图方法提供两种参考：
# 1、使用imshow(field)联合plt.pause()显示栅格地图
# 2、利用plt.plot()联合plt.pause()和plt.cla()进行刷新显示
# tips：import PathPlanning是必须的
# -----------------------------------------------------------------------------------------------
'''

'''
# ------------------------声明地图信息和某些固定信息，地图样式如图所示
# [[1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 2. 1. 1. 1.]
#  [1. 4. 1. 2. 1. 5. 1.]
#  [1. 1. 1. 2. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1.]]
#
'''
rows = 6
cols = 7
startSub = [2,1]
goalSub = [2,5]
obsSub = [[1,3],[2,3],[3,3]]


# 栅格地图属性
field = np.ones((rows, cols))

field[startSub[0], startSub[1]] = 4
field[goalSub[0], goalSub[1]] = 5

for i in range(len(obsSub)):
    field[obsSub[i][0], obsSub[i][1]] = 2

# 新建画布指定大小
fig = plt.figure(figsize=(9,6))
# 新建子图
ax = fig.add_subplot(111)

# 没有用的变量，主要是区分绘制方法是第一种还是第二种
draw = False



'''
# 方法一利用imshow绘制动态地图
# 利用随机函数，随机选择地图位置改变数值
'''
cmap = colors.ListedColormap(['none', 'white', 'black', 'red', 'yellow', 'magenta', 'green', 'cyan', 'blue'])

# 动态刷新地图次数
if draw:
    for i in range(10):
        # 随机选择修改地图信息的位置
        temp_r = random.randint(0,rows-1)
        temp_c = random.randint(0,cols-1)

        # 修改地图信息
        field[temp_r][temp_c] = 3

        # 显示图像并设置图像属性
        ax.imshow(field, cmap=cmap, vmin=0, vmax=8)
        ax.set_ylabel('rows')
        ax.set_xlabel('cols')
        ax.xaxis.tick_top()
        ax.xaxis.set_label_position('top')
        ax.set_xticks(np.arange(cols))
        ax.set_yticks(np.arange(rows))
        plt.pause(0.05)

        # 重置回白色
        field[temp_r][temp_c] = 1


'''
# 方法二：采用plt.plot联合plt.pause()和plt.cla()
# 利用随机函数，随机选择地图位置改变数值
'''
if not draw:
    # plt.plot都是建立在xy坐标系上的内容可以利用pathplanning的sub2xy函数转换
    # 将行列转成xy坐标系的xy值
    startXY = PathPlanning.sub2xy([rows,cols],startSub[0],startSub[1])
    goalXY = PathPlanning.sub2xy([rows,cols],goalSub[0],goalSub[1])
    obsX = []
    obsY = []

    for i in range(len(obsSub)):
        obsxy = PathPlanning.sub2xy([rows,cols],obsSub[i][0],obsSub[i][1])
        obsX.append(obsxy[0])
        obsY.append(obsxy[1])

    for i in range(100):
        # 随机选择修改地图信息的位置
        temp_r = random.randint(0,rows-1)
        temp_c = random.randint(0,cols-1)
        temp_xy = PathPlanning.sub2xy([rows,cols],temp_r,temp_c)

        # 修改地图信息
        field[temp_r][temp_c] = 3

        # 显示图像并设置图像属性
        plt.plot(startXY[0],startXY[1],'r+')
        plt.plot(goalXY[0],goalXY[1],'b+')
        plt.plot(obsX,obsY,'sk')
        plt.plot(temp_xy[0],temp_xy[1],'sr')
        ax.set_xlim([-1,cols])
        ax.set_ylim([-1,rows])
        ax.set_xticks(np.arange(cols))
        ax.set_yticks(np.arange(rows))
        plt.pause(1)
        plt.cla()

        # 重置回白色
        field[temp_r][temp_c] = 1













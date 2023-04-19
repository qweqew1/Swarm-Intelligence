import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors

'''
# # -------------------------------------这里定义绘图函数-------------------------------------------------
'''
def drawmap(rows,cols,startSub,goalSub,obsSub):
    # 创建全部为空地的地图栅格，其中空地以数字1表征
    field = np.ones((rows+1,cols+1))

    # 修改栅格地图中起始点和终点的数值，其中起点以数值4表征，终点以数值5表示
    field[startSub[0],startSub[1]] = 4
    field[goalSub[0],goalSub[1]] = 5

    # 修改栅格地图中障碍物的数值，其中以数值5表示
    for i in range(len(obsSub)):
        field[obsSub[i][0],obsSub[i][1]] = 2

    # 绘制图像，利用matplotlib的热力图进行绘制
    # 设置色条的范围，从0~8
    cmap = colors.ListedColormap(['none','white','black','red','yellow','magenta','green','cyan','blue'])

    # 绘图函数
    # 其实默认为fig,ax = plt.figure(),后续发现fig没有用上
    # 但是ax需要频繁使用，因此直接ax = plt.gca()替代掉
    plt.figure(figsize=(cols,rows))
    ax = plt.gca()


    # 绘制热力图
    # 其中vmin和vmax对应栅格地图数值的颜色与cmap一一对应
    # cbar设置false将色条设置为不可见
    sns.heatmap(field, cmap = cmap,vmin = 0,vmax = 8, linewidths = 0.25, linecolor= 'black', ax = ax, cbar = False)

    # 设置图标题
    ax.set_ylabel('rows')
    ax.set_xlabel('cols')

    # 将列标签移动到图像上方
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')


    # 设置图标的数字个数文字，放在plt.show下面能居中
    ax.set_xticks(np.arange(0,cols+1,1))
    ax.set_yticks(np.arange(0,rows+1,1))

    # 直接显示图像，如要类似于MATLAB的hold on建议在主函数最后使用plt.show()
    # plt.show()

    return field


'''
# # -------------------------------------这是是行列转以该行列方向为坐标系的函数------------------------------
# 其中的XY形式如图所示，从0开始，因为Python数组下标从0开始，Y方向沿下递增
#                   0 1 2 3 4
#                0+---------->X(X=cols)
#                1|
#                2|
#                3|
#               Y(Y=rows)
#     
'''
def sub2coord(possub):
    posx = possub[1]
    posy = possub[0]
    return [posx,posy]


def coord2sub(posxy):
    posr = posxy[1]
    posc = posxy[0]
    return [posr,posc]



'''
# # -------------------------------------这是是测试的主函数-------------------------------------------------
'''
# rows = 4
# cols = 5

# startSub = [2,0]
# goalSub = [2,4]
# obsSub = [[1,2],[2,2],[3,2]]

# drawmap(rows,cols,startSub,goalSub,obsSub)
# # 采用热力图这种，坐标系简历和MATLAB是一致的，X=col，Y=rows，且递增方向都是一致的，因此绘制XY时候比较难理解
# pointxy = [2,3]
# plt.scatter(pointxy[0],pointxy[1],s = 200,c = 'r')
# pointsub = coord2sub(pointxy)
# plt.scatter(pointsub[0],pointsub[1],s = 200,c = 'y')
# plt.show()

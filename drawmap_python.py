import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors

#绘图函数
def drawmap(rows,cols,start,end,obspos):
    startIndex = start
    goalIndex = end
    obsIndex = obspos
    # 创建全部为空地的地图栅格，空地以数字1表示
    filed = np.ones((rows,cols))

    # 起点以数值3表示，终点以数值10表示
    filed[startIndex[0],startIndex[1]] = 3
    filed[goalIndex[0],goalIndex[1]] = 10

    # 栅格地图中障碍物的数值以数值2表示
    for index in range(len(obsIndex)):
        filed[obsIndex[index][0],obsIndex[index][1]] = 2

    # 设置色条
    cmap = colors.ListedColormap(['none','white','black','red','yellow','magenta','green','cyan','blue'])

    # 绘图函数
    fig, ax = plt.subplots(figsize=(10,4.8))
    9
    # 绘制热力图
    # 其中vmin和vmax对应栅格地图数值的颜色与cmap一一对应
    # cbar设置false将色条设置为不可见00
    sns.heatmap(filed, cmap = cmap,vmin = 0,vmax = 8, linewidths = 1.5, linecolor= 'black', ax = ax,cbar = False)#True)

    # 设置图标题
    ax.set_title('Simulated robot path planning')
    ax.set_ylabel('')
    ax.set_xlabel('')

    # 将列标签移动到图像上方
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')

    # 显示图像
    plt.show()


    # 设置图标的数字个数文字，放在plt.show下面能居中
    ax.set_xticks(np.arange(cols))
    ax.set_xticklabels(np.arange(cols))
    ax.set_yticks(np.arange(rows))
    ax.set_yticklabels(np.arange(rows))

    return filed


#主函数
rows = 10
cols = 20

start = [0,0]
end = [9,19]
obspos = [[1,2],[1,3],[1,4],[1,5],[3,1],[3,2],[4,2],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[0,5],
          [1,12],[2,12],[3,12],[4,12],[5,12],[6,12],[7,12],[8,12],[9,12]]

filed = drawmap(rows,cols,start,end,obspos)
print(filed)



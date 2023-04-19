import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pc


'''
# 其中的XY形式如图所示，从0开始，因为Python数组下标从0开始，在
#                Y/
#                3|
#                2|
#                1|
#                0+---------->X
#                   0 1 2 3 4
'''
def xy2sub(len,x,y):
    r = len - y
    c = x
    return [r,c]

def sub2xy(len,r,c):
    x = c
    y = len - r
    return [x,y]




def drawmap_xy(Xs,Ys,startxy,goalxy,obsxy):
    # 其中X和矩阵地图的cols对应
    rows = Ys
    cols = Xs
    # 创建全部为空地的地图栅格，其中空地以数字1表征
    # ！！！注意ones(行列个数，因此rows需要+1)
    field = np.ones([rows+1,cols+1])

    # 修改栅格地图中起始点和终点的数值，其中起点以数值4表征，终点以数值5表示
    startsub = xy2sub(rows,startxy[0],startxy[1])
    goalsub = xy2sub(rows,goalxy[0],goalxy[1])
    field[startsub[0],startsub[1]] = 4
    field[goalsub[0],goalsub[1]] = 5

    # 修改栅格地图中障碍物的数值，其中以数值5表示
    for i in range(len(obsxy)):
        obssub = xy2sub(rows,obsxy[i][0],obsxy[i][1])
        field[obssub[0],obssub[1]] = 2


    # 设置画布属性
    plt.figure(figsize=(cols,rows))
    plt.xlim(-1, cols+1)
    plt.ylim(-1, rows+1)
    plt.xticks(np.arange(Xs+1))
    plt.yticks(np.arange(Ys+1))

    # 绘制障碍物XY位置
    for i in range(len(obsxy)):
        plt.gca().add_patch(pc.Rectangle((obsxy[i][0] - 0.5, obsxy[i][1] - 0.5), 1,1,color='k'))

    # 绘制起点，终点
    plt.gca().add_patch(pc.Rectangle((startxy[0] - 0.5, startxy[1] - 0.5), 1,1,color='yellow'))
    plt.gca().add_patch(pc.Rectangle((goalxy[0] - 0.5, goalxy[1] - 0.5), 1,1,color='m'))

    return field




'''
这里是主函数，将下列地图，用以为坐标XY形式绘制出
# Y/|1. 1. 1. 1. 1.
#   |1. 1. 2. 1. 1.
#   |4. 1. 2. 1. 5.
#   |1. 1. 2. 1. 1.---->X
'''

startxy = [0,1]
goalxy = [4,1]
obsxy = [[2,0],[2,1],[2,2]]

Ys = 3
Xs = 4

drawmap_xy(Xs,Ys,startxy,goalxy,obsxy)

# 采用XY坐标的优势在于绘制其他参数时候，如在X=2，Y=3 绘制一个大圆点，但是地图矩阵和XY又需要相互转变一下
plt.scatter(2,3,s = 200,c = 'r')
plt.show()

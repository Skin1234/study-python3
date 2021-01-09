#做个迷宫吧!可通过为0，墙体为1，当前所在位置为2.起始位置为迷宫左上角，上下左右移动直到走到迷宫右下角的终点。
import random
import numpy as np

#建立迷宫结构，初始化墙体，初始位置
def init_walls(wall_size):
    maze_list = [[0 for col in range(wall_size[0])] for row in range(wall_size[1])]
    maze = build_walls(maze_list)
    #print(np.array(maze).shape)#输出list形状
    # print(len(maze),len(maze[0]))#获取list长度
    maze[0][0] = 2
    return maze

def build_walls(maze):
    row = 0
    col = 0
    walls = 200
    row = np.random.randint(0, 19, size=walls)
    col = np.random.randint(0, 19, size=walls)

    for k in range(0, walls):
        maze[row[k]][col[k]] = 1
    return maze

#输出迷宫
def print_walls(maze):
    for i in range(0,len(maze)):
        print(maze[i])

#更新当前位置
def operate_maze(maze,last_position,current_position):
    maze[last_position[0]][last_position[1]] = 0
    maze[current_position[0]][current_position[1]] = 2
    return maze

#对迷宫进行操作
def operate(maze,operation,last_position):
    rows = len(maze)
    cols = len(maze[0])

    row = last_position[0]
    col = last_position[1]

    if(operation == '4'):
        col = col - 1
        if(col < 0):
            print("移动越界！")
            return last_position,[-1,-1]
    elif(operation == '6'):
        col = col + 1
        if (col > cols):
            print("移动越界！")
            return last_position,[-1,-1]
    elif(operation == '2'):
        row = row + 1
        if (row > rows):
            print("移动越界！")
            return last_position,[-1,-1]
    elif(operation == '8'):
        row = row - 1
        if (row < 0):
            print("移动越界！")
            return last_position,[-1,-1]
    else:
        print("输入不符合规范！")
        return last_position,[-1,-1]

    next_position = [row,col]
    #判断是否有墙
    if (maze[next_position[0]][next_position[1]] == 1 ):
        print("哎呀是墙，不能过去呢!")
        return last_position, [-1, -1]
    return last_position,next_position


wall_size = [25,20]
maze = init_walls(wall_size)
current_position = [0,0]
print("通道为0，阻挡墙为1，目前所在位置为2，初始点在迷宫左上角,终止点在迷宫右下角。")
print_walls(maze)

while(current_position != wall_size):
    operation = input("上8下2左4右6退出q，请输入您的移动方向：")
    if(operation == 'q'):
        print("游戏结束，再来玩哦！")
        break
    else:
        last_position, result_position = operate(maze, operation, current_position)
        if (result_position[0] == -1):
            continue
        else:
            current_position = result_position
        maze = operate_maze(maze, last_position, current_position)
        print_walls(maze)

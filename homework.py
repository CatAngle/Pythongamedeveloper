import pgzrun

# 设置窗口的宽度和高度
WIDTH = 400
HEIGHT = 400

def draw():
    # 清除屏幕，并设置背景颜色为白色 (RGB: 255, 255, 255)
    screen.clear()
    screen.fill((255, 255, 255))

    # 1. 画脸 (使用圆形)
    # 参数: (圆心的X坐标, 圆心的Y坐标), 半径, 颜色(黄色), 线条宽度(0表示实心填充)
    screen.draw.filled_circle((200, 200), 150, (255, 255, 0))
    
    # 给脸画一个黑色的边框，让它更好看
    screen.draw.circle((200, 200), 150, (0, 0, 0))

    # 2. 画眼睛 (使用圆形)
    # 左眼
    screen.draw.filled_circle((140, 150), 20, (0, 0, 0))
    # 右眼
    screen.draw.filled_circle((260, 150), 20, (0, 0, 0))

    # 3. 画微笑的嘴巴 (使用线条和弧线)
    # 为了让微笑更生动，我们可以画一条弧线
    # 参数: 矩形边界 (左, 上, 右, 下), 起始角度, 结束角度
    # 角度 0 是向右，180 是向左。从 0 到 180 就是下半圆（微笑的形状
    screen.draw.line((130, 240), (160, 270), "black")
    screen.draw.line((160, 270), (200, 280), "black")
    screen.draw.line((200, 280), (240, 270), "black")
    screen.draw.line((240, 270), (270, 240), "black")

pgzrun.go()
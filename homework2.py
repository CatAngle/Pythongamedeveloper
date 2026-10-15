import pgzrun

# 设置游戏窗口的宽度和高度
WIDTH = 800
HEIGHT = 600

def draw():
    # 1. 绘制天空背景 (浅蓝色)
    screen.fill((135, 206, 235))

    # 2. 绘制太阳 (题目要求：circles for the sun)
    # 参数：圆心坐标(x, y), 半径, 颜色
    screen.draw.filled_circle((650, 100), 60, "yellow")
    
    # 给太阳加一点外围光晕效果（可选）
    screen.draw.circle((650, 100), 65, "orange")

    # 3. 绘制山脉 (题目要求：lines for mountains)
    # 使用粗线或多条线来形成山峰的形状
    # 第一座山 (左边)
    screen.draw.line((0, 500), (200, 200), "gray")
    screen.draw.line((200, 200), (400, 500), "gray")
    
    # 第二座山 (中间最高)
    screen.draw.line((250, 500), (450, 100), "dimgray")
    screen.draw.line((450, 100), (650, 500), "dimgray")

    # 第三座山 (右边)
    screen.draw.line((550, 500), (700, 250), "gray")
    screen.draw.line((700, 250), (800, 500), "gray")

    # 4. 绘制河流 (题目要求：Add a river)
    # 使用蓝色多边形或粗线来表示河流，从山脚蜿蜒流向底部
    river_points = [
        (300, 500),  # 起点（山脚）
        (600, 550),  # 中间点
        (800, 600),  # 右下角出画面
        (0, 600),    # 左下角出画面
        (100, 550)   # 左侧山脚
    ]
    screen.draw.filled_polygon(river_points, "blue")

    # 加上草地/地基，让山和河有落脚点
    screen.draw.filled_rect(Rect((0, 500), (800, 100)), "green")

def update():
    pas
pgzrun.go()
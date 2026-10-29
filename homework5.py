import pygame
import sys
import math

# 初始化 pygame
pygame.init()

# 屏幕设置
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basketball Shooter")
clock = pygame.time.Clock()

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)

# 物理参数
GRAVITY = 0.5
HOOP_X = 650
HOOP_Y = 300
HOOP_WIDTH = 80
HOOP_HEIGHT = 15

# 篮球初始状态
ball_pos = [100, 450]  # 使用列表存储坐标 [x, y]
ball_vel = [0, 0]      # 速度 [vx, vy]
ball_radius = 20
is_shooting = False
score = 0
scored_in_hoop = False # 防止一次进球多次计分

def reset_ball():
    """重置篮球到初始位置"""
    global ball_pos, ball_vel, is_shooting, scored_in_hoop
    ball_pos = [100, 450]
    ball_vel = [0, 0]
    is_shooting = False
    scored_in_hoop = False

def draw_hoop():
    """绘制篮筐"""
    # 篮板
    pygame.draw.rect(screen, WHITE, (HOOP_X + HOOP_WIDTH, HOOP_Y - 60, 10, 80))
    # 篮筐 (椭圆形表示)
    pygame.draw.ellipse(screen, RED, (HOOP_X, HOOP_Y, HOOP_WIDTH, HOOP_HEIGHT), 3)

def draw_ball():
    """绘制篮球"""
    pygame.draw.circle(screen, ORANGE, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
    # 画几条线模拟篮球纹理
    pygame.draw.line(screen, BLACK, (int(ball_pos[0]-15), int(ball_pos[1])), 
                     (int(ball_pos[0]+15), int(ball_pos[1])), 2)
    pygame.draw.line(screen, BLACK, (int(ball_pos[0]), int(ball_pos[1]-15)), 
                     (int(ball_pos[0]), int(ball_pos[1]+15)), 2)

# 主循环
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 鼠标点击投篮
        if event.type == pygame.MOUSEBUTTONDOWN and not is_shooting:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # 计算投篮方向和初速度 (根据鼠标位置与球的连线)
            dx = mouse_x - ball_pos[0]
            dy = mouse_y - ball_pos[1]
            dist = math.sqrt(dx**2 + dy**2)
            
            # 归一化并赋予初速度倍数
            if dist > 0:
                power = 0.6
                ball_vel[0] = (dx / dist) * power * 15
                ball_vel[1] = (dy / dist) * power * 15 - 5 # 额外给一点向上的力
                is_shooting = True
                scored_in_hoop = False

    # 物理更新 (重力与运动)
    if is_shooting:
        ball_vel[1] += GRAVITY  # 施加重力
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]
        
        # 进球检测：球穿过篮筐区域 (简单矩形碰撞)
        # 当球下落经过篮筐高度，且在篮筐宽度内
        if (HOOP_X < ball_pos[0] < HOOP_X + HOOP_WIDTH and 
            HOOP_Y < ball_pos[1] < HOOP_Y + HOOP_HEIGHT and 
            ball_vel[1] > 0 and not scored_in_hoop):
            score += 1
            scored_in_hoop = True
            
        # 重置条件：出界 (地面或屏幕外)
        if ball_pos[1] > HEIGHT - ball_radius or ball_pos[0] > WIDTH + 50 or ball_pos[0] < -50:
            reset_ball()

    # 绘制元素
    draw_hoop()
    draw_ball()
    
    # 显示得分
    font = pygame.font.SysFont("Arial", 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (20, 20))
    
    if not is_shooting:
        hint = font.render("Click to Shoot!", True, WHITE)
        screen.blit(hint, (WIDTH//2 - 80, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
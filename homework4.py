import pygame
import math
import random

# 初始化 Pygame
pygame.init()

# 屏幕设置
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click Trail - List and Problems")

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)

# ==========================================
# 1. 定义“小角色 (Actor)”类：星星/圆点痕迹
# ==========================================
class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(3, 8)  # 随机大小
        self.color = (random.randint(200, 255), random.randint(200, 255), 0) # 偏黄/白

    def draw(self, surface):
        # 画一个简易的星形或圆点（这里用圆点，也可扩展为五角星）
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

# ==========================================
# 2. 主角色 (Main Actor)
# ==========================================
main_actor_x = WIDTH // 2
main_actor_y = HEIGHT // 2
main_actor_radius = 20

# 【核心】用列表存储所有点击生成的痕迹 (Actors List)
trail_list = []

# 游戏主循环
clock = pygame.time.Clock()
running = True

while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 监听鼠标点击
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左键点击
                mx, my = event.pos
                # 【核心】在点击位置创建一个新的 Star(Actor)，并加入列表
                new_star = Star(mx, my)
                trail_list.append(new_star)

    # 主角色跟随鼠标移动 (The main actor moves between clicks)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    main_actor_x += (mouse_x - main_actor_x) * 0.2  # 平滑跟随
    main_actor_y += (mouse_y - main_actor_y) * 0.2

    # 绘制背景
    screen.fill(BLACK)

    # 【核心】遍历列表，绘制所有保留在屏幕上的痕迹
    for star in trail_list:
        star.draw(screen)

    # 绘制主角色 (例如一个蓝色圆圈)
    pygame.draw.circle(screen, (0, 150, 255), (int(main_actor_x), int(main_actor_y)), main_actor_radius)
    
    # 可选：显示当前列表长度，体现 List 概念
    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Trail Actors in List: {len(trail_list)}", True, WHITE)
    screen.blit(text, (10, 10))

    # 刷新屏幕
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
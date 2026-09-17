import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    ctypes.windll.user32.SetProcessDOLAware()

import pgzrun

WINTH = 800
HEIGHT = 550

SCALE_X = WIDTH/ 1000

def X(value):
    return int (value*SCALE_X)

MAGENTA = (255,0,255)
CYAN = (0,255,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

def draw_rectanglr
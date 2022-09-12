from definitions import DataStructures
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

dt = DataStructures(500, 500, [])
dt.init_frame_buffer()

_r = 255
_g = 255
_b = 255
_a = 255


def init_window():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(dt.img_w, dt.img_h)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("My OpenGL")


def find_pixel(pos_x: int, pos_y: int):
    return pos_x * 4 + pos_y * dt.img_w * 4


def draw_pixel(pos_x: int, pos_y: int):
    mem_pos = find_pixel(pos_x, pos_y)
    
    dt.fb_ret[mem_pos] = _r
    dt.fb_ret[mem_pos + 1] = _g
    dt.fb_ret[mem_pos + 2] = _b
    dt.fb_ret[mem_pos + 3] = _a


def bresenham(x1: int, y1: int, x2: int, y2: int):
    slope = 0

    if x1 > x2:
        bresenham(x2, y2, x1, y1)
        return

    dx = x2 - x1
    dy = y2 - y1

    if dy < 0:
        slope = -1
        dy = -dy
    else:
        slope = 1

    inc_e = 2 * dy
    inc_ne = 2 * dy -2 * dx
    d = 2 * dy - dx
    y = y1

    x = x1
    while x < x2:
        draw_pixel(x, y)
        
        if d <= 0:
            d += inc_e
        else:
            d += inc_ne
            y += slope
            
        x += 1

import atexit

from definitions import *

dt = DataStructures(500, 500, [], [])
#dt.init_frame_buffer()

_r = 255
_g = 255
_b = 255
_a = 255


def draw_func(func):
    func()


def my_gl_draw(ponto1 = None, ponto2 = None, ponto3 = None):

    try:
        ponto1 == ()
    except TypeError:
        raise "First parameter cannot be None. Need at least one point to work!"

    pontos = [ponto1]

    if ponto2:
        pontos.append(ponto2)
        bresenham(pontos[0], pontos[1])
    else:
        draw_pixel(pontos[0])

    if ponto3:
        pontos.append(ponto3)
    else:



def display():
    pass


def init_call_backs():
    glutDisplayFunc(display)


def init_window():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(dt.image_width, dt.image_height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("My OpenGL")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def find_pixel(pos_x: int, pos_y: int):
    return pos_x * 4 + pos_y * dt.image_width * 4


def draw_pixel(ponto: tuple):
    pos_x, pos_y = ponto
    mem_pos = find_pixel(pos_x, pos_y)
    
    dt.fb[mem_pos] = _r
    dt.fb[mem_pos + 1] = _g
    dt.fb[mem_pos + 2] = _b
    dt.fb[mem_pos + 3] = _a


def bresenham(ponto1: tuple, ponto2: tuple):
    slope = 0
    x1, y1 = ponto1
    x2, y2 = ponto2

    if x1 > x2:
        bresenham(ponto2, ponto1)
        return

    dx = x2 - x1
    dy = y2 - y1

    if dy < 0:
        slope = -1
        dy = -dy
    else:
        slope = 1

    inc_e = 2 * dy
    inc_ne = 2 * dy - 2 * dx
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

import atexit
from typing import List

import numpy as np

from definitions import *


dt = DataStructures(600, 600, [], [])
_r = 255
_g = 255
_b = 255
_a = 255


def my_gl_draw(point1=None, point2=None, point3=None):
    """
    Draw a point, line, or triangle.

    :param point1: first point
    :param point2: second point
    :param point3: third point
    :return: None
    """
    try:
        point1 is not None
    except TypeError:
        raise "First parameter cannot be None. Need at least one point to work!"

    if point2 and not point3:
        bresenham(point1, point2)
    else:
        draw_pixel(point1)

    if point3:
        points = [point1, point2, point3]
        try:
            verify_triangle(points)
        except ValueError:
            raise "These coordinates does not draw a triangle, but a line."
        triangle(point1, point2, point3)


def verify_triangle(points: []) -> bool:
    """
    Verify if the coordinates list parameter do draw a triangle.

    :param points: (list) A list of coordinate tuples.
    :return: True if triangle, else returns false.
    """
    if len(points) != 3:
        return False

    testTriangle = np.array([[points[0]], points[1], points[2]])
    if np.linalg.det(testTriangle):
        return True
    else:
        return False


def triangle(point1: tuple, point2: tuple, point3: tuple):
    """
    Draws a triangle with 3 points
    :param point1: first point
    :param point2: second point
    :param point3: third point
    :return: None
    """
    bresenham(point1, point2)
    bresenham(point2, point3)
    bresenham(point3, point1)


def init_opengl():

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    screen_width = glutGet(GLUT_SCREEN_WIDTH)
    screen_height = glutGet(GLUT_SCREEN_HEIGHT)

    glutInitWindowPosition((screen_width - dt.image_width) // 2,
                           (screen_height - dt.image_width) // 2)

    glutInitWindowSize(dt.image_width, dt.image_height)

    glutCreateWindow("Meu primeiro app com OpenGL em Python")


def initialize():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, dt.image_width, 0, dt.image_height)


def draws():
    # Limpa a janela de visualização com a cor
    # de fundo definida previamente
    glClear(GL_COLOR_BUFFER_BIT)

    # Altera a cor do desenho para vermelho
    glColor3f(0.0, 0.0, 0.0)

    glPointSize(5.0)

    glBegin(GL_POINTS)
    glVertex2f(200, 200)
    glVertex2f(400, 200)
    glVertex2f(400, 300)
    glVertex2f(200, 300)
    glVertex2f(200, 400)
    glVertex2f(400, 400)
    glEnd()

    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(3.0)  # aumenta a espessura das linhas
    glBegin(GL_LINES)
    # glBegin(GL_LINE_STRIP)
    # glBegin(GL_LINE_LOOP)
    glVertex2f(200, 200)
    glVertex2f(400, 200)
    glVertex2f(400, 300)
    glVertex2f(200, 300)
    glVertex2f(200, 400)
    glVertex2f(400, 400)
    glEnd()

    # Executa os comandos OpenGL
    glFlush()


def find_pixel(point: tuple):
    """
    Returns the memory position of a given point
    :param point: point
    :return: memory position in the window
    """
    pos_x, pos_y = point
    return pos_x * 4 + pos_y * dt.image_width * 4


def draw_pixel(point: tuple):
    """
    draws a pixel in a given position
    :param point: point that will be painted
    :return: None
    """
    mem_pos = find_pixel(point)

    dt.fb[mem_pos] = _r
    dt.fb[mem_pos + 1] = _g
    dt.fb[mem_pos + 2] = _b
    dt.fb[mem_pos + 3] = _a


def bresenham(point1: tuple, point2: tuple):
    """
    Uses the Bresenham algorithm to draw a line
    :param point1: first point of the line
    :param point2: last point of the line
    :return: None
    """
    slope = 0
    x1, y1 = point1
    x2, y2 = point2

    if x1 > x2:
        bresenham(point2, point1)
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
        draw_pixel((x, y))

        if d <= 0:
            d += inc_e
        else:
            d += inc_ne
            y += slope

        x += 1

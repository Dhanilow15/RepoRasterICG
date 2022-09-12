import atexit
import numpy as np

from definitions import *

dt = DataStructures(500, 500, [], [])
# dt.init_frame_buffer()

_r = 255
_g = 255
_b = 255
_a = 255


def draw_func(func):
    func()


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
        except TypeError:
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


def display():
    draw_func(my_gl_draw())
    glBindTexture(GL_TEXTURE_2D, dt.tex)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, dt.image_width, dt.image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, dt.fb)

    glEnable(GL_TEXTURE_2D)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glViewport(0, 0, dt.image_width, dt.image_height)

    glBegin(GL_TRIANGLES)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0, -1.0, 0.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, 1.0, 0.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0, 1.0, 0.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0, -1.0, 0.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0, -1.0, 0.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, 1.0, 0.0)

def init_call_backs():
    glutDisplayFunc(display)


def init_window():
    """
    initializes a Opengl window
    :return: None
    """
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

import atexit

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
    Draw a point, line, or triangle
    :param point1: first point
    :param point2: second point
    :param point3: third point
    :return: None
    """
    try:
        point1 == ()
    except TypeError:
        raise "First parameter cannot be None. Need at least one point to work!"

    if point2 and not point3:
        bresenham(point1, point2)
    else:
        draw_pixel(point1)

    if point3:
        triangle(point1, point2, point3)


def verify_multiple(*args: int) -> bool:
    """
    Verify if the bigger number is multiple of the others
    :param args: numbers
    :return: True if they are, False if not
    """
    numbers = sorted(args, reverse=True)
    if len(numbers) == 1:
        return True
    multiples = 0

    for x in numbers:
        assert type(x) == int
        if numbers[-1] % x == 0:
            multiples += 1

    if multiples == len(numbers):
        return True

    return False


def triangle(point1: tuple, point2: tuple, point3: tuple):
    """
    Verifies if the points are not all in the same line and then draws a triangle with 3 points
    :param point1: first point
    :param point2: second point
    :param point3: third point
    :return: None
    """
    assert not (verify_multiple(point1[0], point2[0], point3[0]) * verify_multiple(point1[1], point2[1], point3[1]))

    bresenham(point1, point2)
    bresenham(point2, point3)
    bresenham(point3, point1)


def display():
    pass


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

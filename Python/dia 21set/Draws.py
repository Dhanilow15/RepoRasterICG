import glfw
from glfw.GLFW import *
from OpenGL.GL import *


def draw_line(vertices):
    glBegin(GL_LINE_STRIP)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()


line_vertices = []


def onMouseButton(win, button, action, mods):
    global line_vertices

    if button == glfw.MOUSE_BUTTON_LEFT:
        if action == glfw.PRESS:
            line_vertices.append(glfw.get_cursor_pos(win))


glfw.init()
display_size = (640, 480)
window = glfw.create_window(*display_size, "OpenGL window", None, None)

glfw.make_context_current(window)
glfw.set_mouse_button_callback(window, onMouseButton)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, display_size[0], display_size[1], 0, -1, 1)

glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

while not glfwWindowShouldClose(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_line(line_vertices + [glfw.get_cursor_pos(window)])

    glfwSwapBuffers(window)
    glfwPollEvents()

glfw.terminate()
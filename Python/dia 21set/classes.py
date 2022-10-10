import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import compileProgram, compileShader

import numpy as np
import ctypes


def create_shader(vertexFilepath, fragmentFilepath):
    """
    Compiles and creates a OpenGL shader from vertex and fragment file path
    :param vertexFilepath:
    :param fragmentFilepath:
    :return: Shader
    """
    with open(vertexFilepath, 'r') as f:
        vertex_src = f.readlines()
    with open(fragmentFilepath, 'r') as f:
        fragment_src = f.readlines()

    shader = compileProgram(
        compileShader(vertex_src, GL_VERTEX_SHADER),
        compileShader(fragment_src, GL_FRAGMENT_SHADER)
    )

    return shader


class App:

    def __init__(self):
        """
        Initializing Python and OpenGL
        """
        # initializing python
        self.RGBA = [0, 0, 0, 1]
        pg.init()
        display = (512, 512)
        pg.display.set_mode(display, DOUBLEBUF | OPENGL)
        #   pg.display._set_caption("Sample OpenGL")
        self.clock = pg.time.Clock()
        # initializing OpenGL
        self.shader = create_shader("shaders/vertex.txt", "shaders/fragment.txt")
        glUseProgram(self.shader)
        self.triangle = Triangle((-0.4, 0.2, 0.0, 1.0, 0.4, 0.2,
                                  0.4, 0.2, 0.0, 1.0, 0.4, 0.2,
                                  0.0, 0.5, 0.0, 1.0, 0.4, 0.2))

        self.wall1 = Triangle((-0.4, 0.2, 0.0, 0.0, 0.5, 0.3,
                               0.4, 0.2, 0.0, 0.0, 0.5, 0.3,
                               -0.4, -0.4, 0.0, 0.0, 0.5, 0.3,))
        self.wall2 = Triangle((0.4, 0.2, 0.0, 0.0, 0.5, 0.3,
                               -0.4, -0.4, 0.0, 0.0, 0.5, 0.3,
                               0.4, -0.4, 0.0, 0.0, 0.5, 0.3))

        self.door1 = Triangle((-0.25, 0.0, 0.0, 0.5, 0.2, 0.0,
                               -0.25, -0.4, 0.0, 0.5, 0.2, 0.0,
                               -0.05, -0.4, 0.0, 0.5, 0.2, 0.0))
        self.door2 = Triangle((-0.25, 0.0, 0.0, 0.5, 0.2, 0.0,
                               -0.05, 0.0, 0.0, 0.5, 0.2, 0.0,
                               -0.05, -0.4, 0.0, 0.5, 0.2, 0.0))

        self.window1 = Triangle((0.1, 0.0, 0.0, 0.0, 0.0, 0.4,
                                 0.3, 0.0, 0.0, 0.0, 0.0, 0.4,
                                 0.1, -0.2, 0.0, 0.0, 0.0, 0.4))
        self.window2 = Triangle((0.1, -0.2, 0.0, 0.0, 0.0, 0.3,
                                 0.3, -0.2, 0.0, 0.0, 0.0, 0.3,
                                 0.3, 0.0, 0.0, 0.0, 0.0, 0.3))

        self.main_loop()

    def main_loop(self):
        """
        Display APP loop function
        :return: None
        """
        running = True
        # getting display events
        while running:
            for event in pg.event.get():
                # exit event
                if event.type == pg.QUIT:
                    running = False
                # background color change event
                if event.type == pg.KEYDOWN:
                    # space = black
                    if event.key == pg.K_SPACE:
                        self.RGBA[0] = 0
                        self.RGBA[1] = 0
                        self.RGBA[2] = 0
                        self.RGBA[3] = 1
                    # special keys = gray
                    elif event.key <= 47 or event.key in range(59,65) and event.key != pg.K_SPACE or \
                            event.key in range(92,97) \
                            or event.key >= 123:
                        self.RGBA[0] = 0.5
                        self.RGBA[1] = 0.5
                        self.RGBA[2] = 0.5
                        self.RGBA[3] = 1
                    # others = white
                    else:
                        self.RGBA[0] = 1
                        self.RGBA[1] = 1
                        self.RGBA[2] = 1
                        self.RGBA[3] = 1

            # refresh screen
            glClearColor(self.RGBA[0], self.RGBA[1], self.RGBA[2], self.RGBA[3])
            glClear(GL_COLOR_BUFFER_BIT)

            # drawing house
            glUseProgram(self.shader)
            glBindVertexArray(self.triangle.vao)
            glDrawArrays(GL_TRIANGLES, 0, self.triangle.vertices_count)
            glBindVertexArray(self.wall1.vao)
            glDrawArrays(GL_TRIANGLES, 0, self.wall1.vertices_count)
            glBindVertexArray(self.wall2.vao)
            glDrawArrays(GL_TRIANGLES, 0, self.wall2.vertices_count)
            glBindVertexArray(self.door1.vao)
            glDrawArrays(GL_TRIANGLES, 0, self.door1.vertices_count)
            glBindVertexArray(self.door2.vao)
            glDrawArrays(GL_TRIANGLES, 0, self.door2.vertices_count)
            glBindVertexArray(self.window1.vao)
            glDrawArrays(GL_TRIANGLES, 0, self.window1.vertices_count)
            glBindVertexArray(self.window2.vao)
            glDrawArrays(GL_TRIANGLES, 0, self.window2.vertices_count)

            pg.display.flip()

            # timing
            self.clock.tick(60)

        self.quit()

    def quit(self):

        self.triangle.destroy()
        glDeleteProgram(self.shader)
        pg.quit()


class Triangle:

    def __init__(self, vertices):
        """x, y, z, r, g, b"""
        self.vertices = vertices
        self.vertices = np.array(self.vertices, dtype=np.float32)
        self.vertices_count = 3

        # vao -> vertex array object
        # vbo -> vertex buffer object
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        # position attribute
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        # color attribute
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    def destroy(self):
        """
        Function to release allocated memory
        :return: None
        """
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))


class Rectangle:
    pass


if __name__ == "__main__":
    myApp = App()

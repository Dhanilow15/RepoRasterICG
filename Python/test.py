import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import compileProgram, compileShader

import numpy as np
import ctypes


class App:

    def __init__(self):
        """
        Initializing Python and OpenGL
        """
        # initializing python
        pg.init()
        display = (520, 520)
        pg.display.set_mode(display, DOUBLEBUF | OPENGL)
        #   pg.display._set_caption("Sample OpenGL")
        self.clock = pg.time.Clock()
        # initializing OpenGL
        glClearColor(0, 0, 0, 1)
        self.shader = self.create_shader("shaders/vertex.txt", "shaders/fragment.txt")
        glUseProgram(self.shader)
        self.triangle = Triangle()
        self.main_loop()

    def create_shader(self, vertexFilepath, fragmentFilepath):
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

    def main_loop(self):
        """
        Display APP loop function
        :return: None
        """
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            # refresh screen
            glClear(GL_COLOR_BUFFER_BIT)

            glUseProgram(self.shader)
            glBindVertexArray(self.triangle.vao)
            glDrawArrays(GL_TRIANGLES, 0, self.triangle.vertices_count)

            pg.display.flip()

            # timing
            self.clock.tick(60)

        self.quit()

    def quit(self):

        self.triangle.destroy()
        glDeleteProgram(self.shader)
        pg.quit()


class Triangle:
    def __init__(self):
        """x, y, z, r, g, b"""
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            0.0, -1.0, 0.0, 0.0, 0.0, 1.0
        )
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
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_TRUE, 24, ctypes.c_void_p(0))
        # color attribute
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_TRUE, 24, ctypes.c_void_p(12))

    def destroy(self):
        """
        Function to release allocated memory
        :return: None
        """
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))


if __name__ == "__main__":
    myApp = App()

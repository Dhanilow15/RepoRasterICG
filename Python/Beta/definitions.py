from dataclasses import dataclass
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import atexit


@dataclass
class DataStructures():
    image_width: int
    image_height: int
    fb: []
    tex: []

    def __str__(self):
        return "the image is" + str(self.image_width) + "x" + str(self.image_height)

    def init_frame_buffer(self):
        self.fb = [None] * self.image_width * self.image_height * 5
        
        for i in range(self.image_height * self.image_width):
            self.fb[i * 4 + 0] = 0
            self.fb[i * 4 + 1] = 0
            self.fb[i * 4 + 2] = 0
            self.fb[i * 4 + 3] = 255

        glGenTextures(1, self.tex)
        glBindTexture(GL_TEXTURE_2D, self.tex)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glBindTexture(GL_TEXTURE_2D, 0)

from dataclasses import dataclass


@dataclass
class DataStructures:
    image_width: int
    image_height: int
    fb: []

    def __str__(self):
        return "the image is" + str(self.image_width) + "x" + str(self.image_height)

    @property
    def img_w(self):
        return self.image_width

    @property
    def img_h(self):
        return self.image_height

    @property
    def fb_ret(self):
        return self.fb

    def init_frame_buffer(self):
        fb = [None] * self.image_width * self.image_height
        
        for i in range(self.image_height * self.image_width):
            fb[i * 4 + 0] = 0
            fb[i * 4 + 1] = 0
            fb[i * 4 + 2] = 0
            fb[i * 4 + 3] = 255

import numpy as np
from NeuralPainter.test_model import TestModel

class Painter:
    def __init__(self):
        self.k = 0
        self.frames = []

    def _random_generated_pixel(self, frame):
        frame_size = frame.shape

        random_red = np.random.rand()
        random_green = np.random.rand()
        random_blue = np.random.rand()

        random_h = np.random.randint(0, frame_size[0])
        random_w = np.random.randint(0, frame_size[1])

        frame[random_h, random_w] = [random_red, random_green, random_blue]

        return frame

    def generate_n_frames(self,
            n,
            start_frame=np.ones((100,100,3)),
            pixel_generator=""
            ):

        self.k = self.k + 1

        #Select function for generating next pixel in frame here
        new_frame = self._random_generated_pixel(start_frame)
        self.frames.append(new_frame.copy())

        if self.k < n:
            return self.generate_n_frames(n, new_frame)

    def generate_n_unsexy_frames(self,
            n,
            start_frame=np.ones((100,100,3))
            ):

        for k in range(0, n):
            new_frame = self._random_generated_pixel(start_frame)
            self.frames.append(new_frame.copy())
        return

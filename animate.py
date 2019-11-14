import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Animate:
    def __init__(self, sequence):
        self.fig = plt.figure()
        self.init_sequence = []
        self.im = plt.imshow(np.zeros((100, 100,3)), cmap='viridis', animated=True)
        self.ani = animation.FuncAnimation(self.fig, func=self._next_frame, frames=sequence)
        plt.show()

    def _next_frame(self, frame):
        im = self.im.set_data(frame)
        time.sleep(0)
        return im,

    def gen_test_seq():
        sequence = []
        sequence.append(np.random.random((100, 100,3)))
        return sequence

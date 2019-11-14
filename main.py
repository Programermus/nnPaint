from animate import Animate
from painter import Painter
import numpy as np

#Paint a random painting
painting = Painter()
painting.generate_n_frames(300)
Animate(painting.frames)

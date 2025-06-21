import numpy as np

def Signal():
    def __init__(
            self,
            bitstream: np.ndarray,
            samples: np.ndarray,
    ):
        self.bitstream = bitstream
        self.samples = samples
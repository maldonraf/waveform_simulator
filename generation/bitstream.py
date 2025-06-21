import numpy as np

def gen(pattern_type, bit_count):
    bitstream = []

    if pattern_type == "random":
        bitstream = np.random.randint(2, size=bit_count)

    return bitstream
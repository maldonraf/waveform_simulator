import scipy

import numpy as np

# def fir(num, denom, data):
#     filtered_data = scipy.signal.lfilter(num, denom, data)
#     return filtered_data

def root_raised_cosine():
    pass

def raised_cosine(beta, samples_per_symbol, symbol_cnt):
    samples = symbol_cnt * samples_per_symbol
    t = np.arange(-(samples//2), (samples//2) + 1) / samples_per_symbol

    h = np.zeros_like(t)
    for i, val in enumerate(t):
        if val == 0.0:
            h[i] = 1.0
        elif beta != 0 and np.isclose(abs(val), 1/(2 * beta)):
            h[i] = (np.pi / 4) * np.sinc(1 / (2 * beta))
        else:
            h[i] = (np.sinc(val) * np.cos(np.pi * beta * val)) / (1 - (2 * beta * val) ** 2)

    h = h / np.sqrt(np.sum(h ** 2))
    return h

def gaussian():
    pass
import scipy
import filters.fir

import numpy as np

def shape(sig, shaping):
    if shaping == "raised_cosine":
        h = filters.fir.raised_cosine(
            beta = sig.params.shaping_rc_beta,
            samples_per_symbol = sig.params.shaping_rc_sps,
            symbol_cnt = 10
        )
        shaped_signal = np.convolve(h, sig.signal_modulated, mode='same')

    return h, shaped_signal
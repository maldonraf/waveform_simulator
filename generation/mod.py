import math

import numpy as np

def modulator(
        bitstream,
        modulation_type,
        modulation_levels,
        oversampling_ratio,
        oversampling_type,
        ):
    if modulation_type == "PAM":
        symbol_bitlength = int(math.log(modulation_levels, 2))

        # trim bitstream length to a multiple of symbol_bitlength
        if len(bitstream) % symbol_bitlength != 0:
            bitstream_length = (len(bitstream) // symbol_bitlength) * symbol_bitlength
            bitstream = bitstream[:bitstream_length]

        # group bits into symbols, scale symbols, and center them about 0
        symbol_bitgroups    = np.reshape(bitstream, (-1, symbol_bitlength))
        powers              = 2 ** np.arange(symbol_bitlength - 1, -1, -1)
        symbol_indices      = np.dot(symbol_bitgroups, powers)
        pam_levels          = np.linspace(-(modulation_levels - 1), (modulation_levels - 1), modulation_levels)
        symbol_stream       = pam_levels[symbol_indices]

        if oversampling_type == "ZOH":
            oversampled_symbol_stream = np.repeat(symbol_stream, oversampling_ratio)
        elif oversampling_type == "zero-stuff":
            oversampled_symbol_stream = zero_stuffing(symbol_stream, oversampling_ratio)

        return oversampled_symbol_stream
    
def zero_stuffing(signal, oversampling_ratio):
    oversampled_signal = np.zeros(len(signal) * oversampling_ratio, dtype=signal.dtype)
    oversampled_signal[::oversampling_ratio] = signal

    return oversampled_signal
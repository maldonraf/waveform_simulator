import numpy as np
import matplotlib.pyplot as plt
import stream_gen as stream_gen
import scipy
import filters

# ===== User Params =====
bit_rate        = (53.125e9 * 2)
sample_rate     = bit_rate * 50
signal_length   = 1000
plot_symbol_cnt = 2
# =====

figure, axis = plt.subplots(2, 1)

samples_per_symbol  = int(sample_rate / bit_rate)
samples             = signal_length * samples_per_symbol
symbol_stream       = stream_gen.stream_gen(length=signal_length, levels=4) - 1.5
signal = []
for symbol in symbol_stream:
    pulse = np.zeros(samples_per_symbol)
    pulse[0] = symbol
    signal = np.concatenate((signal, pulse))

h = filters.raised_cosine(0.8, samples_per_symbol, 100)

axis[0].set_title('Filter Impulse Responses')
axis[0].plot(h)

tx_signal   = np.convolve(signal, h, mode='same')

axis[1].set_title('Eye Capture')
plot_cnt = len(signal)//(plot_symbol_cnt * samples_per_symbol)
for i in range(plot_cnt-1):
    plot_range = plot_symbol_cnt * samples_per_symbol
    subrange_start = i * plot_range
    subrange_end = subrange_start + plot_range
    axis[1].plot(tx_signal[subrange_start:subrange_end])

figure.show()
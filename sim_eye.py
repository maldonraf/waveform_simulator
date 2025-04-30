import numpy as np
import matplotlib.pyplot as plt
import stream_gen as stream_gen
import scipy

# ===== User Params =====
bit_rate        = 1e3
sample_rate     = 1e5
signal_length   = 10000
# =====

samples_per_symbol  = int(sample_rate / bit_rate)
samples             = signal_length * samples_per_symbol
t                   = np.linspace(0, signal_length/bit_rate, samples, endpoint=False)
bit_stream          = stream_gen.stream_gen(length=signal_length, levels=4)
symbol_stream       = 2 * bit_stream - 1
signal              = np.repeat(symbol_stream, samples_per_symbol)

wn      = 2 * np.pi * 1e2
zeta    = 0.7
system  = scipy.signal.lti([wn**2], [1, 2 * zeta * wn, wn**2])
tout, h = scipy.signal.impulse(system)

tx_signal   = np.convolve(signal, h, mode='same')
t           = np.arange(len(tx_signal)) / sample_rate

plt.figure(figsize=(10,4))

for i in range(len(tx_signal)//5000):
    plot_range = (len(tx_signal)//5000)
    subrange_start = i * plot_range
    subrange_end = subrange_start + plot_range
    plt.plot(tx_signal[subrange_start:subrange_end])

plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
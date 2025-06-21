import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

import signal
import analysis.plots
import analysis.ana_metrics
import analysis.dig_metrics
import generation.bitstream
import generation.mod
import generation.shaping
import filters.fir
import filters.iir
import filters.jitter
import filters.noise
import filters.nonlinear
import recovery.cru
import recovery.demod
import recovery.ffe

# === SIGNAL PARAMS ===
bit_count           = 100
baudrate            = 53.125e9
modulation_type     = "PAM"
modulation_levels   = 4
pattern_type        = "random"
pulse_shape         = "raised_cosine"
oversampling_ratio  = 10
oversampling_type   = "zero-stuff" # "ZOH"

# === SIGNAL GEN ===
sig_bits = generation.bitstream.gen(pattern_type, bit_count)
sig_modulated = generation.mod.modulator(bitstream=sig_bits,
                               modulation_type=modulation_type,
                               modulation_levels=modulation_levels,
                               oversampling_ratio=oversampling_ratio,
                               oversampling_type=oversampling_type)
sig_tx = generation.shaping.shape(signal=sig_modulated,
                                  shaping=pulse_shape)

#sig = signal.Signal(bitstream=sig_bits, samples=sig_tx)

# === IMPAIRMENT CHAINING ===

# === SIGNAL RECOVERY ===

# === SIGNAL ANALYSIS ===
analysis.plots.plot_basic(sig_tx)
#analysis.plots.plot_constellation(sig)
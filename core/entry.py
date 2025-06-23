import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

import waveform
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
parameters = waveform.SignalConfig(
    bit_count=10000,
    baudrate=53.125e9,
    modulation_type="PAM",
    modulation_levels=4,
    pulse_shape="raised_cosine",
    shaping_rc_beta=0.7,
    shaping_rc_sps=10,
    oversampling_ratio=10,
    oversampling_type="zero-stuff"
)

# === SIGNAL GEN ===
sig = waveform.Signal(parameters=parameters)

sig.bitstream = generation.bitstream.gen(
    sig.params.pattern_type,
    sig.params.bit_count
)
sig.signal_modulated = generation.mod.modulator(
    bitstream=sig.bitstream,
    modulation_type=sig.params.modulation_type,
    modulation_levels=sig.params.modulation_levels,
    oversampling_ratio=sig.params.oversampling_ratio,
    oversampling_type=sig.params.oversampling_type
)
h, sig.signal_shaped = generation.shaping.shape(
    sig=sig,
    shaping=sig.params.pulse_shape
)
sig.h_shaping = h

# === IMPAIRMENT CHAINING ===

# === SIGNAL RECOVERY ===

# === SIGNAL ANALYSIS ===
analysis.plots.plot_basic(sig.h_shaping)
analysis.plots.plot_basic(sig.bitstream)
analysis.plots.plot_basic(sig.signal_modulated)
analysis.plots.plot_basic(sig.signal_shaped)
#analysis.plots.plot_constellation(sig)
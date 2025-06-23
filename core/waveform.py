import numpy as np

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class SignalConfig:
    bit_count: int
    baudrate: float
    modulation_type: str
    modulation_levels: int
    pattern_type: str = "random"
    pulse_shape: Optional[str] = None
    oversampling_ratio: int = 1
    oversampling_type: str = "zero-stuff"

    # Raised cosine specific (used only if pulse_shape == "raised_cosine")
    shaping_rc_beta: Optional[float] = None
    shaping_rc_sps: Optional[int] = None

class Signal:
    def __init__(self, parameters):
        self.params = parameters
"""KalmanEmergence — thin wrapper, delegates to eon-core unified_emergence.

The original standalone implementation (kalman_emergence.py v1.0) has been 
consolidated into eon-core's unified_emergence module.

Usage (backward compatible):
    from fish_ecology.kalman_emergence import KalmanEmergence
    kf = KalmanEmergence()
    kf.update("species_id", 0.7)
    if kf.is_emerging():
        print("Emergence detected!")

For advanced usage, use eon-core directly:
    from eon_core.unified_emergence import KalmanEmergence, EmergenceMonitor
"""

import sys, os, json, time, math
from dataclasses import dataclass
from typing import List, Optional

# Try eon-core import first
try:
    from eon_core.unified_emergence import KalmanEmergence as _KalmanEmergence
    _USE_EON_CORE = True
except ImportError:
    _USE_EON_CORE = False


if _USE_EON_CORE:
    KalmanEmergence = _KalmanEmergence  # direct re-export

else:
    # Fallback: embedded Kalman filter (for standalone use)
    @dataclass
    class KalmanState:
        x: float = 0.5
        P: float = 1.0
        Q: float = 0.01
        R: float = 0.1
        F: float = 1.0
        H: float = 1.0
        history: List[float] = None
        def __post_init__(self):
            self.history = self.history or []

    class KalmanEmergence:
        """Kalman Filter for emergence signal detection (fallback mode)."""
        def __init__(self, state_file: str = None):
            self._states: dict = {}
            self._divergences: dict = {}
            self._state_file = state_file

        def update(self, species_id: str, observation: float,
                   process_noise: float = 0.01, measurement_noise: float = 0.1) -> float:
            state = self._states.get(species_id, KalmanState())
            state.Q = process_noise; state.R = measurement_noise
            x_pred = state.F * state.x
            P_pred = state.F * state.P * state.F + state.Q
            y = observation - state.H * x_pred
            S = state.H * P_pred * state.H + state.R
            K = P_pred * state.H / S if S > 0 else 0
            state.x = x_pred + K * y
            state.P = (1 - K * state.H) * P_pred
            state.history.append(observation)
            self._states[species_id] = state
            self._divergences[species_id] = abs(y) / math.sqrt(S) if S > 0 else 0
            return state.x

        def is_emerging(self, species_id: str = None, threshold: float = 3.0) -> bool:
            if species_id:
                return self._divergences.get(species_id, 0) > threshold
            return any(d > threshold for d in self._divergences.values())

        @property
        def divergence(self, species_id: str = None) -> float:
            if species_id:
                return self._divergences.get(species_id, 0)
            return max(self._divergences.values()) if self._divergences else 0

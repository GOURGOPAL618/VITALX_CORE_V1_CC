# ============================================
# AstroVital CC V1 — Sensor Mocks
# Developer: Gouragopal Mohapatra
# © 2026 Gouragopal Mohapatra
# ============================================

import numpy as np


def get_vitals():
    """Simulate realistic astronaut vitals."""
    np.random.seed(int(__import__('time').time()) % 1000)
    return {
        'hr':    np.random.normal(75, 8),
        'sbp':   np.random.normal(118, 10),
        'dbp':   np.random.normal(75, 6),
        'spo2':  np.clip(np.random.normal(97, 1.5),
                         88, 100),
        'sleep': np.clip(np.random.normal(6.0, 0.8),
                         2, 8),
        'muscle':np.clip(np.random.normal(3.0, 1.5),
                         0, 16),
        'bone':  np.clip(np.random.normal(0.8, 0.3),
                         0, 2),
        'rad':   np.clip(np.random.normal(30, 10),
                         0, 100),
        'immune':np.clip(np.random.normal(72, 10),
                         20, 100),
    }
"""Simple plot digitization helper
Inspired by old dormant plot digitizer tools
"""
import numpy as np

def simple_digitize(image, num_points=10):
    """Placeholder for future graph digitization.
    Currently returns sample points."""
    # In future versions this will use the logic from the dormant repos
    height, width = image.shape[:2]
    x = np.linspace(0, width, num_points)
    y = np.random.randint(50, height-50, num_points)  # placeholder
    return list(zip(x.astype(int), y.astype(int)))}
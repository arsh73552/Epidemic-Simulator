import numpy as np
class helperClass:
    def custom_uv_func(self, x, y, height, width, desiredRadius):

        θ = 2 * np.pi * (x / width)  # Adjusting the range of θ to [-π, π]
        φ = np.pi * (y / height) - np.pi/2
        xr = desiredRadius * np.sin(φ) * np.cos(θ)
        yr = desiredRadius * np.sin(φ) * np.sin(θ)
        zr = desiredRadius * np.cos(φ)
        return (xr, yr, zr)

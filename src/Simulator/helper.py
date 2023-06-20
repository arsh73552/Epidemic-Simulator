import math
import numpy as np


class helperClass:

    def custom_uv_func(self, x, y, height, width, desiredRadius):
        θ = 2 * np.pi * (x / width)  # Adjusting the range of θ to [-π, π]
        φ = np.pi * (y / height) - np.pi/2
        xr = desiredRadius * np.sin(φ) * np.cos(θ)
        yr = desiredRadius * np.sin(φ) * np.sin(θ)
        zr = desiredRadius * np.cos(φ)
        return (xr, yr, zr)

    def distance_manhattan(self, firstCoord, secondCoord):
        dist = 0
        for i in range(len(firstCoord)):
            dist += abs(firstCoord[i] - secondCoord[i])
        return dist

    def distance_euler(self, firstCoord, secondCoord):
        dist = 0
        for i in range(len(firstCoord)):
            dist += (firstCoord[i] - secondCoord[i])**2
        return math.sqrt(dist)

    def patient_zero_exists(self):
        if 'self.patient_zero' in locals():
            return True
        return False
 
import math
import numpy as np


class helperClass:

    def custom_uv_func(self, x, y, height, width, desiredRadius):
        '''
        This function is used to map the x and y coordinates of the screen to the x, y and z coordinates of the sphere.
        Input Params:
            x: x coordinate of the screen
            y: y coordinate of the screen
            height: height of the screen in manim units
            width: width of the screen in manim units
            desiredRadius: radius of the sphere in manim units
        Output Params:
            Tuple containing the x, y and z coordinates of the input point on the sphere
        '''
        θ = 2 * np.pi * (x / width)  # Adjusting the range of θ to [-π, π]
        φ = np.pi * (y / height) - np.pi/2
        xr = desiredRadius * np.sin(φ) * np.cos(θ)
        yr = desiredRadius * np.sin(φ) * np.sin(θ)
        zr = desiredRadius * np.cos(φ)
        return (xr, yr, zr)

    def distance_manhattan(self, firstCoord, secondCoord):
        '''
        This function calculates the manhattan distance between two points in n-dimensional space.
        Input Params:
            firstCoord: coordinates of the first point
            secondCoord: coordinates of the second point
        Output Params:
            Manhattan distance between the two points
        '''
        dist = 0
        for i in range(len(firstCoord)):
            dist += abs(firstCoord[i] - secondCoord[i])
        return dist

    def distance_euler(self, firstCoord, secondCoord):
        '''
        This function calculates the euclidean distance between two points in n-dimensional space.
        Input Params:
            firstCoord: coordinates of the first point
            secondCoord: coordinates of the second point
        Output Params:
            Euclidean distance between the two points
        '''
        dist = 0
        for i in range(len(firstCoord)):
            dist += (firstCoord[i] - secondCoord[i])**2
        return math.sqrt(dist)

    def patient_zero_exists(self):
        '''
        This function checks if the patient zero has been initialized or not.
        Input Params:
            None
        Output Params:
            True if patient zero has been initialized, False otherwise
        '''
        if 'self.patient_zero' in locals():
            return True
        return False

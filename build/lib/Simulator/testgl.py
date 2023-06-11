from manimlib import *
import json
import numpy as np


class SquareAnimation(Scene):
    def construct(self):
        background = ImageMobject("map1.jpg").set_height(8)
        self.play(FadeIn(background))
        continentLocations = [[0, 0, 0],[1, 1, 0],[-2, -1, 0]]
        INFECTION_RATE = 0.5
        pixel_array = background.image
        x_coordinates, y_coordinates = [], []
        max_attempts = 100000  # Maximum number of attempts to find a white pixel
        attempts = 0
        
        while len(x_coordinates) < 100 and attempts < max_attempts:
            x = random.randint(0, 1920 - 1) # 0-1920
            y = random.randint(0, 1080 - 1) # 0-1080
            r, g, b = pixel_array.getpixel((x, y))
            if r > 200 and g > 200 and b > 200:  # Check if the pixel is white (adjust threshold as needed)
                x_coordinates.append(-7.11 + (14.22*x/1920))
                y_coordinates.append(4 - (8*y/1080))

                
            attempts += 1
        dots = VGroup()
        for i in range(len(x_coordinates)):
            print(x_coordinates[i], y_coordinates[i])
            dot = Dot(radius=0.03, color=GREEN)
            dot.move_to([x_coordinates[i], y_coordinates[i], 0])  # Adjust the Z-coordinate as needed
            dots.add(dot)
        img = background.image
        self.play(ShowCreation(dots), run_time = 10)

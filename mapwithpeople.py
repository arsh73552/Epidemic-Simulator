import math
import numpy as np
from manimlib import *

from matplotlib import pyplot as plt
from PIL import Image
import random
import time
class WorldMap(Scene):
    def construct(self):
        continentLocations = [[0, 0, 0],[1, 1, 0],[-2, -1, 0]]
        INFECTION_RATE = 0.5
        map = ImageMobject("map1.jpg")
        pixel_array = map.pixel_array
        pixel_to_vector_map = {}
        pixel_x_increment = 14.22/1920
        pixel_y_decrement = 8/1080
        initial_vector_x = -7.11
        initial_vector_y = 4
        for y in range(pixel_array.shape[0]):
            initial_vector_x = -7.11
            for x in range(pixel_array.shape[1]):
                pixel_to_vector_map[(x, y)] = [initial_vector_x, initial_vector_y]
                initial_vector_x += pixel_x_increment
            initial_vector_y -= pixel_y_decrement
        map.move_to(ORIGIN)
        self.play(FadeIn(map))
        grayscale_map = map.get_pixel_array()
        # Generate random coordinates for the dots on white areas
        np.random.seed(0)  # Set a seed for reproducibility
        x_coordinates = []
        y_coordinates = []
        max_attempts = 100000  # Maximum number of attempts to find a white pixel
        attempts = 0
        while len(x_coordinates) < 1000 and attempts < max_attempts:
            x = np.random.randint(0, grayscale_map.shape[1]) # 0-1920
            y = np.random.randint(0, grayscale_map.shape[0]) # 0-1080
            if grayscale_map[y, x, 0] > 200:  # Check if the pixel is white (adjust threshold as needed)
                x_coordinates.append(pixel_to_vector_map[(x, y)][0])
                y_coordinates.append(pixel_to_vector_map[(x, y)][1])
            attempts += 1

        # Add dots to the scene
        dots = VGroup()
        for x, y in zip(x_coordinates, y_coordinates):
            dot = Dot(radius=0.03, color=GREEN)
            dot.move_to([x, y, 0])  # Adjust the Z-coordinate as needed
            dots.add(dot)
        self.play(Create(dots), run_time = 10)

        yellow_dots = VGroup()
        dot = Dot(radius=0.1, color=RED)
        dot.move_to([x, y, 0])
        yellow_dots.add(dot)
        self.add(yellow_dots)

        start = time.time()
        while len(dots) > 0:
            selected = not_selected = 0
            InternationlTravelDots = []
            converted_dots = VGroup()  # Group to store converted yellow dots
            to_be_removed_dots = VGroup()
            converted_dots_animate = VGroup()
            print(len(converted_dots))
            for yd in yellow_dots:

                if random.uniform(0, 1) < 0.01:
                        InternationlTravelDots.append(yd.animate.move_to(continentLocations[random.randint(0, 2)]))

                for dot in dots:
                    # Check proximity with all existing yellow dots
                    x1, y1 = dot.get_center()[0], dot.get_center()[1]
                    x2, y2 = yd.get_center()[0], yd.get_center()[1]

                    if random.uniform(0, 1 < 0.1):
                        InternationlTravelDots.append(dot.animate.move_to(continentLocations[random.randint(0, 2)]))


                    if math.sqrt((x2 - x1)**2 + (y2 - y1)**2) < 0.5 and INFECTION_RATE > random.uniform(0, 1):
                        # Create a yellow dot at the current position of the red dot
                        yellow_dot = Dot(radius=0.03, color=RED)
                        yellow_dot.move_to(dot.get_center())
                        to_be_removed_dots.add(dot)
                        converted_dots_animate.add(yellow_dot)
                        # Animate the transition from red to yellow
                        selected+= 1
                        dots.remove(dot)
                        # Add the converted yellow dot to the list
                        converted_dots.add(dot)
                    else:
                        not_selected+=1
            print(type(dot.animate.move_to(continentLocations[random.randint(0, 2)])))
            print('hehe')
            print(selected/(selected+not_selected))
            print('pass')
            self.play(Transform(to_be_removed_dots, converted_dots_animate), AnimationGroup(*InternationlTravelDots), run_time=0.02*len(to_be_removed_dots))
            # Remove converted red dots from the list
            for converted_dot in converted_dots:
                yellow_dots.add(converted_dot)
            print(len(dots), len(converted_dots), len(yellow_dots))
            # Update the scene
            self.wait(0.1)
            if len(converted_dots) == 0:
                break




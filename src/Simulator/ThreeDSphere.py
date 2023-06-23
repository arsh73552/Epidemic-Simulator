from manimlib import ImageMobject, Sphere, SGroup, TexturedSurface, PI
from manimlib import ShowCreation, Rotate
from manimlib import RED, BLACK, IN, GREEN
import random
import time
from helper import helperClass
from init import Initialization
import typing


class surfaceExample(helperClass, Initialization):

    def __init__(self, **kwargs):
        Initialization.__init__(self)
        helperClass.__init__(self)

    def construct_animation_initialization(self, coords):
        '''
            This function constructs the animation for the initialization of the earth
            :param coords: The coordinates of the patient zero
            :return: A list of tuples, where each tuple contains the animation and the time it takes to run
        '''
        finalAnimations = []
        self.patient_zero = Sphere(radius=0.1)
        self.patient_zero.set_color(RED).move_to(self.custom_uv_func(coords[0], coords[1], self.canvas_height, self.canvas_width, self.radius))
        random.seed(time.time())
        background = ImageMobject(self.image_path).set_height(8)
        pixel_array = background.image
        x_coordinates: typing.List[float] = []
        y_coordinates: typing.List[float] = []
        attempts = 0
        while len(x_coordinates) < self.num_points and attempts < self.max_attempts:
            x = random.randint(0, 1920 - 1)  # 0-1920 960
            y = y = random.randint(0, 1080 - 1)  # 0-1080 540
            r, g, b = pixel_array.getpixel((x, y))
            if not (b > r + g):  # Check if the pixel is blue
                x_coordinates.append((self.canvas_width*x/self.pixel_width) - self.canvas_width/2)
                y_coordinates.append(self.canvas_height/2 - (self.canvas_height*y/self.pixel_height))
            attempts += 1

        earth = Sphere(radius=self.radius, fill_opacity=1).shift([0, 0, 1])

        self.healthyDots = []
        for i in range(len(x_coordinates)):
            x, y, z = self.custom_uv_func(x_coordinates[i], y_coordinates[i], self.canvas_height, self.canvas_width, self.radius)
            sphr = Sphere(radius=0.03).set_color(GREEN, opacity=1).move_to([x, y, z])
            self.healthyDots.append(sphr)

        earth.set_color(color=BLACK, opacity=1)

        surfaces = [
            TexturedSurface(surface, self.image_path)
            for surface in [earth]
        ]

        for mob in surfaces:
            mob.shift(IN)

        surface = surfaces[0]
        finalAnimations.append((ShowCreation(surface), 1))
        finalAnimations.append((Rotate(surface, 2*PI), 5))
        finalAnimations.append((ShowCreation(SGroup(*self.healthyDots)), 5))
        finalAnimations.append((ShowCreation(self.patient_zero), 1))
        return finalAnimations

    def construct_animation_BFS(self, coords):
        '''
            This function constructs the animation for the BFS algorithm
            :param coords: The coordinates of the patient zero
            :return: A list of tuples, where each tuple contains the animation and the time it takes to run
        '''
        dotsConvertingInOrer = []  # This is used to keep track of the dots that are converting
        unhealthyDots = []
        unhealthyDots.append(self.patient_zero)
        lastIterationConversionDots = [self.patient_zero]
        removedDots: typing.List[Sphere] = []
        interationCouner = 0
        while True:
            convertedDots = []
            interationCouner += 1
            for i, unhealthyDot in enumerate(lastIterationConversionDots):
                for healthyDot in self.healthyDots:
                    if self.distance_manhattan(unhealthyDot.get_center(), healthyDot.get_center()) < self.distance_threshold:
                        if random.uniform(0, 1) < self.INFECTION_RATE and healthyDot not in convertedDots:
                            convertedDots.append(healthyDot)
                            self.healthyDots.remove(healthyDot)
                            unhealthyDots.append(healthyDot)
                            dotsConvertingInOrer.append((healthyDot, len(self.healthyDots), len(unhealthyDots), 0, len(removedDots)))
                if (random.uniform(0, 1) < (0.85 ** i)):
                    removedDots.append(unhealthyDot)
                    unhealthyDots.remove(unhealthyDot)
                    dotsConvertingInOrer.append((unhealthyDot, len(self.healthyDots), len(unhealthyDots), -1, len(removedDots)))

            lastIterationConversionDots = convertedDots

            if len(convertedDots) == 0:
                break
        return dotsConvertingInOrer

from manimlib import ThreeDScene, ThreeDCamera, ImageMobject, Sphere, SGroup, TexturedSurface
from manimlib import ShowCreation, SurfaceMesh, ThreeDAxes
from manimlib import RED, BLUE, BLACK, DEGREES, IN, GREEN
import random
import time
from helper import helperClass
from init import Initialization
import math
import typing


class surfaceExample(ThreeDScene, helperClass, Initialization):
    CONFIG = {
        "camera_class": ThreeDCamera,
        "full_screen": True,
    }

    def __init__(self, **kwargs):
        Initialization.__init__(self)
        helperClass.__init__(self)
        ThreeDScene.__init__(self)

    def construct(self):
        random.seed(time.time())
        background = ImageMobject(self.image_path).set_height(8)
        pixel_array = background.image
        x_coordinates: typing.List[float] = []
        y_coordinates: typing.List[float] = []
        attempts = 0
        while len(x_coordinates) < 1 and attempts < self.max_attempts:
            x = random.randint(0, 1920 - 1)  # 0-1920 960
            y = random.randint(0, 1080 - 1)  # 0-1080 540
            r, g, b = pixel_array.getpixel((x, y))
            if r > 200 and g > 200 and b > 200:  # Check if the pixel is white (adjust threshold as needed)
                x_coordinates.append((self.canvas_width*x/self.pixel_width) - self.canvas_width/2)
                y_coordinates.append(self.canvas_height/2 - (self.canvas_height*y/self.pixel_height))
            attempts += 1

        sphere = Sphere(radius=self.radius, fill_opacity=1).shift([0, 0, 1])

        dots = SGroup()
        for i in range(len(x_coordinates)):
            x, y, z = self.custom_uv_func(x_coordinates[i], y_coordinates[i], self.canvas_height, self.canvas_width, self.radius)
            sphr = Sphere(radius=0.03).set_color(GREEN, opacity=1).move_to([x, y, z])
            dots.add(sphr)

        sphere.set_color(color=BLACK, opacity=1)

        surfaces = [
            TexturedSurface(surface, self.image_path)
            for surface in [sphere]
        ]

        for mob in surfaces:
            mob.shift(IN)
            mob.mesh = SurfaceMesh(mob)
            mob.mesh.set_stroke(BLUE, 1, opacity=0.5)

        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        surface = surfaces[0]
        self.play(*[ShowCreation(surface), ShowCreation(surface.mesh)])
        self.play(ShowCreation(dots))
        self.add(Sphere(radius=0.1).move_to([-0.022222222222222143, 2.988888888888889, 0.0]))
        self.play(ShowCreation(ThreeDAxes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            z_range=[-5, 5]
        )))

    def on_key_press(self, symbol: int, modifiers: int):
        from pyglet.window import key as pyglet_key
        if symbol == pyglet_key.G:
            self.patient_zero = Sphere(radius=0.1).set_color(RED)
            self.patient_one = Sphere(radius=0.1).set_color(RED)
            self.play(ShowCreation(self.patient_zero))
            x, y, z = self.mouse_point.get_center()
            print(x, y, z)
            print(self.camera.frame.uniforms["orientation"])
            z = math.sqrt(self.radius**2 - x**2 - y**2)
            self.play(self.patient_one.animate.move_to([x, y, z]))
        return super().on_key_press(symbol, modifiers)


class Main():
    def __init__(self) -> None:
        SE = surfaceExample()
        SE.run()


A = Main()

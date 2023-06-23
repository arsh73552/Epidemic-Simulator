from manimlib import ThreeDScene, ImageMobject, Sphere, RED, LEFT, UP
from manimlib import ShowCreation,  FadeIn, FadeOut, DEGREES, GREY
from init import Initialization
from introduction import intro
from ThreeDSphere import surfaceExample


class Main(ThreeDScene, Initialization):
    def gotKeyPress(self):
        '''
            Check if the user has pressed a key (G).
            :return: True if the user has pressed a key, False otherwise
        '''
        return self.waitOver

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Initialization.__init__(self)
        self.patient_zero = Sphere(radius=0.1).set_color(RED).move_to([4, 1, 0] + LEFT + UP)

    def construct(self):

        # Begin Intro Animation
        it = intro()
        frame = self.camera.frame
        anim1 = it.construct_animation()
        for animation in anim1:
            if animation[1] != -1:
                self.play(animation[0], run_time=animation[1])
            else:
                self.play(animation[0])
        # End Intro Animation

        # Begin Main Animation
        self.waitOver = False
        background = ImageMobject("test.jpg").set_height(8)
        self.play(FadeIn(background))
        self.wait_until(self.gotKeyPress, max_time=20)
        self.play(FadeOut(background), FadeOut(self.patient_zero))
        EarthAnimation = surfaceExample()
        anim2 = EarthAnimation.construct_animation_initialization(self.patient_zero.get_center())

        # Add Ambient Rotation to the camera.
        frame.add_updater(lambda m, dt: m.increment_theta(-0.3 * dt))

        # anim2 => List of animations, each animation is a tuple of (animation, run_time)
        for animation in anim2:
            if animation[1] != -1:
                self.play(animation[0], run_time=animation[1])
            else:
                self.play(animation[0])
        dots = EarthAnimation.construct_animation_BFS(self.patient_zero.get_center())

        # HealthyCounter = Tex("Healthy: " + str(self.num_points)).set_color(GREEN).to_corner(UL).scale(0.5)
        # UnhealthyCounter = Tex("Unhealthy: " + str(0)).set_color(RED).next_to(HealthyCounter, DOWN).scale(0.5)
        # THANOSCounter = Tex("Removed: " + str(0)).set_color(GREY).next_to(UnhealthyCounter, DOWN).scale(0.5)

        self.play(
            frame.animate.increment_phi(45 * DEGREES),
            run_time=3
        )
        for i, dotTuple in enumerate(dots):
            # newCounterHealthy = Tex("Healthy: " + str(dotTuple[1])).set_color(GREEN).to_corner(UL).scale(0.5)
            # newCounterUnhealthy = Tex("Unhealthy: " + str(dotTuple[2])).set_color(RED).next_to(newCounterHealthy, DOWN).scale(0.5)
            # newTHANOSCounter = Tex("Removed: " + str(dotTuple[4])).set_color(GREY).next_to(newCounterUnhealthy, DOWN).scale(0.5)
            if dotTuple[3] == 0:
                self.play(dotTuple[0].animate.set_color(RED), run_time=0.01)
            else:
                self.play(dotTuple[0].animate.set_color(GREY), run_time=0.01)
            if i % 10 == 0:
                self.wait(2)
            # self.play(*[
            # Transform(HealthyCounter, newCounterHealthy),
            # Transform(UnhealthyCounter, newCounterUnhealthy),
            # Transform(THANOSCounter, newTHANOSCounter)],
            # run_time=0.01
            # )

    def on_key_press(self, symbol: int, modifiers: int):
        '''
            Check if the user has pressed a key (G). If so get mouse position and create a sphere at that position.
            :param symbol: The key that was pressed
            :param modifiers: The modifiers that were pressed
            :return: None
        '''
        from pyglet.window import key as pyglet_key
        if symbol == pyglet_key.G:
            self.patient_zero = Sphere(radius=0.1).set_color(RED)
            self.play(ShowCreation(self.patient_zero))
            self.play(self.patient_zero.animate.move_to(self.mouse_point.get_center()))
            self.waitOver = True


A = Main()
A.run()

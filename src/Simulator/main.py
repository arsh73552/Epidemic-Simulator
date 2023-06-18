from manimlib import ThreeDScene, ImageMobject, Sphere
from manimlib import ShowCreation,  FadeIn, FadeOut
from manimlib import RED
from introduction import intro
from ThreeDSphere import surfaceExample


class Main(ThreeDScene):
    def gotKeyPress(self):
        return self.waitOver

    def construct(self):
        it = intro()
        anim1 = it.construct_animation()
        for animation in anim1:
            if animation[1] != -1:
                self.play(animation[0], run_time=animation[1])
            else:
                self.play(animation[0])
        self.waitOver = False
        background = ImageMobject("test.jpg").set_height(8)
        self.play(FadeIn(background))
        self.wait_until(self.gotKeyPress)
        self.play(FadeOut(background), FadeOut(self.patient_zero))
        EarthAnimation = surfaceExample()
        anim2 = EarthAnimation.construct_animation_initialization(self.patient_zero.get_center())
        for animation in anim2:
            if animation[1] != -1:
                self.play(animation[0], run_time=animation[1])
            else:
                self.play(animation[0])
        dots = EarthAnimation.construct_animation_BFS(self.patient_zero.get_center())
        print(len(dots))
        for dot in dots:
            self.play(dot.animate.set_color(RED), run_time=0.3)

    def on_key_press(self, symbol: int, modifiers: int):
        from pyglet.window import key as pyglet_key
        if symbol == pyglet_key.G:
            self.patient_zero = Sphere(radius=0.1).set_color(RED)
            self.play(ShowCreation(self.patient_zero))
            self.play(self.patient_zero.animate.move_to(self.mouse_point.get_center()))
            self.waitOver = True


A = Main()
A.run()

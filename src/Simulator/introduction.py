from manimlib import Text, RED, GREEN
from manimlib import VGroup, Square, Dot, Write, FadeOut, ShowCreation
import random


class intro():
    def construct_animation(self):
        '''
            This function is used to create the introduction animation.
            This includes the title, description and the information about the dots.
            The function returns the list of animations.

            Output: List of animations
        '''
        finalAnimations = []
        name = Text("Epidemic Simulator").scale(2)
        finalAnimations.append((Write(name), 2.0))
        finalAnimations.append((FadeOut(name), -1.0))
        description = VGroup()
        line1 = Text("An interactive model that uses the").move_to([0, 1, 0])
        line2 = Text("specified infection rate to mimic the spread").move_to([0, 0, 0])
        line3 = Text("of illness over the planet.").move_to([0, -1, 0])
        description.add(line1)
        description.add(line2)
        description.add(line3)

        finalAnimations.append((Write(description), 5.0))
        finalAnimations.append((FadeOut(description), -1.0))

        info = VGroup()
        title = Text("Infection spread in a confined setting").move_to([0, 3.5, 0]).scale(0.75)
        info.add(title)
        info1 = Text("Red = Infected").move_to([0, 3, 0]).scale(0.5)
        info.add(info1)
        info2 = Text("Green = Healthy").move_to([0, 2.5, 0]).scale(0.5)
        info.add(info2)

        finalAnimations.append((Write(info), 2.0))

        sq = Square().scale(2.2)
        finalAnimations.append((ShowCreation(sq), -1.0))
        x_coordinates = []
        y_coordinates = []

        people = VGroup()
        for i in range(0, 150):
            x = random.randint(-2, 1) + random.random()
            y = random.randint(-2, 1) + random.random()
            x_coordinates.append(x)
            y_coordinates.append(y)
            dot = Dot(radius=0.05, color=GREEN).move_to([x, y, 0])
            people.add(dot)
            finalAnimations.append((ShowCreation(dot), 0.01))

        infection_point = [x_coordinates[0], y_coordinates[0]]
        queue = []
        queue.append(infection_point)
        visited = {}

        dots = VGroup()

        while len(queue) > 0:

            temp = queue.pop(0)
            temp_x = temp[0]
            temp_y = temp[1]

            for i in range(0, len(x_coordinates)):
                if (x_coordinates[i], y_coordinates[i]) in visited:
                    continue
                if ((abs(temp_x - x_coordinates[i]) + abs(temp_y - y_coordinates[i])) < 1.25):
                    dot = Dot(color=RED).move_to([x_coordinates[i], y_coordinates[i], 0])
                    dots.add(dot)
                    visited[(x_coordinates[i], y_coordinates[i])] = True
                    queue.append([x_coordinates[i], y_coordinates[i]])
                    finalAnimations.append((ShowCreation(dot), 0.01))
        self.dots = dots
        self.sq = sq
        finalAnimations.append((FadeOut(info), -1))
        finalAnimations.append((FadeOut(sq), -1))
        finalAnimations.append((FadeOut(dots), -1))
        finalAnimations.append((FadeOut(people), -1))
        return finalAnimations
        # self.remove(name, people, dots, sq, info)

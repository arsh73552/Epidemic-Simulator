from manimlib import Scene, RED, GREEN, GREY, Rectangle, Brace, RIGHT
from manimlib import VGroup, Square, Dot, always_redraw, Text
import random
from typing import List

class SirGraph(Scene):
    def construct(self):
        sq = Square().scale(2.2)
        sq.move_to([3, 0, 0])
        self.add(sq)
        x_coordinates = []
        y_coordinates = []

        people = VGroup()
        population = 150
        for i in range(0, population):
            x = random.randint(-2, 1) + random.random() + 3
            y = random.randint(-2, 1) + random.random()
            x_coordinates.append(x)
            y_coordinates.append(y)
            dot = Dot(radius=0.05, color=GREEN).move_to([x, y, 0])
            people.add(dot)
            self.add(dot)
        values: List[float] = [1.0, 0.0, 0.0]
        custom_width = 5

        infected = always_redraw(
            lambda: Rectangle(
                color=RED,
                fill_color=RED,
                fill_opacity=0.7,
                width=custom_width,
                height=values[1]*4
            ).move_to([-4, -2 + (values[1] * 2), 0])
        )
        removed = always_redraw(
            lambda: Rectangle(
                color=GREY,
                fill_color=GREY,
                fill_opacity=0.7,
                width=custom_width,
                height=values[2]*4
            ).move_to(infected.get_top() + [0, values[2]*2, 0])
        )
        susceptible = always_redraw(
            lambda: Rectangle(
                color=GREEN,
                fill_color=GREEN,
                fill_opacity=0.7,
                width=custom_width,
                height=values[0]*4
            ).move_to(removed.get_top() + [0, values[0] * 2, 0])
        )

        sus_brace = always_redraw(
            lambda: Brace(susceptible, [1, 0, 0])
        )
        infected_brace = always_redraw(
            lambda: Brace(infected, [1, 0, 0])
        )
        removed_brace = always_redraw(
            lambda: Brace(removed, [1, 0, 0])
        )

        sus_text = always_redraw(
            lambda: Text(
                "Susceptable " + str(int(values[0]*100)) + "%",
                font_size=16
            ).next_to(sus_brace, RIGHT)
        )
        infected_text = always_redraw(
            lambda: Text(
                "Infected " + str(int(values[1]*100)) + "%",
                font_size=16).next_to(infected_brace, RIGHT)
        )
        removed_text = always_redraw(
            lambda: Text(
                "Removed " + str(int(values[2]*100)) + "%",
                font_size=16).next_to(removed_brace, RIGHT)
        )

        self.add(susceptible, infected, removed)
        self.add(sus_brace, infected_brace, removed_brace)
        self.add(sus_text, infected_text, removed_text)

        infection_point = [x_coordinates[0], y_coordinates[0]]
        queue = []
        queue.append(infection_point)
        visited = {}

        dots = VGroup()

        ptr = 0
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
                    self.add(dot)
                    if (len(dots) > (ptr+50)):
                        self.remove(dots[ptr])
                        new_dot = Dot(color=GREY)
                        new_dot.move_to(dots[ptr].get_center())
                        self.add(new_dot)
                        ptr += 1
                    values[0] = (population - len(dots))/population
                    values[1] = (len(dots) - ptr)/population
                    values[2] = ptr/population
                    self.wait(0.0001)
        for i in range(ptr, population):
            self.remove(dots[ptr])
            new_dot = Dot(color=GREY)
            new_dot.move_to(dots[ptr].get_center())
            self.add(new_dot)
            ptr += 1
            values[0] = (population - len(dots))/population
            values[1] = (len(dots) - ptr)/population
            values[2] = ptr/population
            self.wait(0.0001)

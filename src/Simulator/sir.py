from manimlib import Scene, RED, GREEN, GREY, BarChart
from manimlib import VGroup, Square, Dot

import random


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
        values = [1, 0, 0]

        chart = BarChart(
            values,
            bar_colors=[GREEN, RED, GREY],
            bar_names=["Susuptable", "Infected", "Removed"],
            x_length=10,
            y_axis_config={"font_size": 24},
        )

        chart.scale(0.75)
        chart.move_to([-3, 0, 0])
        self.add(chart)

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
                    self.remove(chart)
                    values[0] = (population - len(dots))/population
                    values[1] = (len(dots) - ptr)/population
                    values[2] = ptr/population
                    chart = BarChart(
                        values,
                        bar_colors=[GREEN, RED, GREY],
                        bar_names=["Susuptable", "Infected", "Removed"],
                        x_length=10,
                        y_axis_config={"font_size": 24},
                    )
                    chart.scale(0.75)
                    chart.move_to([-3, 0, 0])
                    self.add(chart)
                    self.wait(0.0001)
        for i in range(ptr, population):
            self.remove(dots[ptr])
            new_dot = Dot(color=GREY)
            new_dot.move_to(dots[ptr].get_center())
            self.add(new_dot)
            ptr += 1
            self.remove(chart)
            values[0] = (population - len(dots))/population
            values[1] = (len(dots) - ptr)/population
            values[2] = ptr/population
            chart = BarChart(
                values,
                bar_colors=[GREEN, RED, GREY],
                bar_names=["Susuptable", "Infected", "Removed"],
                x_length=10,
                y_axis_config={"font_size": 24},
            )
            chart.scale(0.75)
            chart.move_to([-3, 0, 0])
            self.add(chart)
            self.wait(0.0001)

from manimlib import Scene, RED, GREEN, GREY, Axes
from manimlib import VGroup, Square, Dot
import random


class SirGraph(Scene):
    def construct(self):
        sq = Square().scale(2.2)
        sq.move_to([3, 0, 0])
        self.add(sq)
        x_coordinates = []
        y_coordinates = []

        population = 70

        people = VGroup()

        for i in range(0, population):
            x = random.randint(-2, 1) + random.random() + 3
            y = random.randint(-2, 1) + random.random()
            x_coordinates.append(x)
            y_coordinates.append(y)

            dot = Dot(radius=0.05, color=GREEN).move_to([x, y, 0])
            people.add(dot)
            self.add(dot)

        plot_infected = [0, 0]
        plot_suseptible = [len(people), len(people)]
        plot_removed = [0, 0]

        axes = Axes(
            x_range=[0, len(plot_suseptible), 1],
            y_range=[0, len(people), 10],
            width=7
        ).scale(0.6)
        axes.move_to([-4, 0, 0])

        def suseptible(x):
            if x < len(plot_suseptible):
                return plot_suseptible[int(x)]
            else:
                return 0

        def infected(x):
            if x < len(plot_infected):
                return plot_infected[int(x)]
            else:
                return 0

        def removed(x):
            if x < len(plot_removed):
                return plot_removed[int(x)]
            else:
                return 0

        graph_suseptible = axes.get_graph(suseptible, x_min=0, x_max=len(plot_suseptible)-1)
        graph_infected = axes.get_graph(infected, x_min=0, x_max=len(plot_suseptible)-1)
        graph_removed = axes.get_graph(removed, x_min=0, x_max=len(plot_suseptible)-1)

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
            counter = 0
            for i in range(0, len(x_coordinates)):

                if (x_coordinates[i], y_coordinates[i]) in visited:
                    continue
                if ((abs(temp_x - x_coordinates[i]) + abs(temp_y - y_coordinates[i])) < 1.25):
                    counter += 1
                    dot = Dot(color=RED).move_to([x_coordinates[i], y_coordinates[i], 0])
                    dots.add(dot)
                    visited[(x_coordinates[i], y_coordinates[i])] = True
                    queue.append([x_coordinates[i], y_coordinates[i]])
                    self.add(dot)
                    plot_suseptible.append(plot_suseptible[len(plot_suseptible) - 1] - 1)
                    plot_infected.append(plot_infected[len(plot_infected) - 1] + 1)
                    plot_removed.append(plot_removed[len(plot_removed) - 1])
                    if (len(dots) > (ptr+50)):
                        counter += 1
                        self.remove(dots[ptr])
                        new_dot = Dot(color=GREY)
                        new_dot.move_to(dots[ptr].get_center())
                        self.add(new_dot)
                        plot_infected.append(plot_infected[len(plot_infected) - 1] - 1)
                        plot_removed.append(plot_removed[len(plot_removed) - 1] + 1)
                        plot_suseptible.append(plot_suseptible[len(plot_suseptible)-1])
                        self.wait(0.001)
                        ptr += 1
            if(counter):
                self.remove(axes, graph_infected, graph_removed, graph_suseptible)
                axes = Axes(
                    x_range=[0, len(plot_suseptible), 1],
                    y_range=[0, len(people), 10],
                    width=7
                ).scale(0.6)
                axes.move_to([-4, 0, 0])
                graph_suseptible = axes.get_graph(suseptible, x_min=0, x_max=len(plot_suseptible)-2, color=GREEN)
                graph_infected = axes.get_graph(infected, x_min=0, x_max=len(plot_suseptible)-2, color=RED)
                graph_removed = axes.get_graph(removed, x_min=0, x_max=len(plot_suseptible)-2, color=GREY)
                self.add(axes)
                self.add(graph_infected, graph_removed, graph_suseptible)
                self.wait(0.001)

        for i in range(ptr, population):
            self.remove(dots[ptr])
            new_dot = Dot(color=GREY)
            new_dot.move_to(dots[ptr].get_center())
            self.add(new_dot)
            ptr += 1
            plot_infected.append(plot_infected[len(plot_infected) - 1] - 1)
            plot_removed.append(plot_removed[len(plot_removed) - 1] + 1)
            plot_suseptible.append(plot_suseptible[len(plot_suseptible) - 1])
            if(i % 10 == 0 or ptr == population+1):
                self.remove(axes, graph_infected, graph_removed, graph_suseptible)
                axes = Axes(
                    x_range=[0, len(plot_suseptible), 1],
                    y_range=[0, len(people), 10],
                    width=7
                ).scale(0.6)
                axes.move_to([-4, 0, 0])
                graph_suseptible = axes.get_graph(suseptible, x_min=0, x_max=len(plot_suseptible)-2, color=GREEN)
                graph_infected = axes.get_graph(infected, x_min=0, x_max=len(plot_suseptible)-2, color=RED)
                graph_removed = axes.get_graph(removed, x_min=0, x_max=len(plot_suseptible)-2, color=GREY)
                self.add(axes)
                self.add(graph_infected, graph_removed, graph_suseptible)
                self.wait(0.001)

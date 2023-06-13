from manimlib import Scene, Text, VGroup, Square, Dot, RED
import random


class intro(Scene):
    def construct(self):
        name = Text("Epidemic Simulator").scale(2)
        self.add(name)
        self.wait(3)
        self.remove(name)

        description = VGroup()
        line1 = Text("An interactive model that uses the").move_to([0, 1, 0])
        line2 = Text("specified infection rate to mimic the spread").move_to([0, 0, 0])
        line3 = Text("of illness over the planet.").move_to([0, -1, 0])
        description.add(line1)
        description.add(line2)
        description.add(line3)

        self.add(description)
        self.wait(4)
        self.remove(description)

        info = VGroup()
        title = Text("Infection spread in a confined setting").move_to([0, 3.5, 0]).scale(0.75)
        info.add(title)
        info1 = Text("Red = Infected").move_to([0, 3, 0]).scale(0.5)
        info.add(info1)
        info2 = Text("white = Healthy").move_to([0, 2.5, 0]).scale(0.5)
        info.add(info2)

        self.add(info)

        sq = Square().scale(2.2)
        self.add(sq)
        x_coordinates = []
        y_coordinates = []

        people = VGroup()
        for i in range(0, 150):
            x = random.randint(-2, 1) + random.random()
            y = random.randint(-2, 1) + random.random()
            x_coordinates.append(x)
            y_coordinates.append(y)
            dot = Dot(radius=0.05).move_to([x, y, 0])
            people.add(dot)
            self.add(dot)

        infection_point = [x_coordinates[0], y_coordinates[0]]
        queue = []
        queue.append(infection_point)
        visited = {}

        dots = VGroup()

        while(len(queue) > 0):

            temp = queue.pop(0)
            temp_x = temp[0]
            temp_y = temp[1]

            for i in range(0, len(x_coordinates)):
                if (x_coordinates[i], y_coordinates[i]) in visited:
                    continue
                if((abs(temp_x - x_coordinates[i]) + abs(temp_y - y_coordinates[i])) < 1.25):
                    dot = Dot(color=RED).move_to([x_coordinates[i], y_coordinates[i], 0])
                    dots.add(dot)
                    visited[(x_coordinates[i], y_coordinates[i])] = True
                    queue.append([x_coordinates[i], y_coordinates[i]])
                    self.add(dot)
                    self.wait(0.0001)

        self.wait(2)
        self.remove(name, people, dots, sq, info)

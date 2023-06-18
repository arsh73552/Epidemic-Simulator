class Initialization:
    def __init__(self):
        self.image_path = "test.jpg"
        self.radius = 3
        self.pixel_height = 1080
        self.pixel_width = 1920
        self.canvas_height = 8
        self.canvas_width = 14.22
        self.num_points = 100
        self.initial_vector_x = -7.11
        self.initial_vector_y = 4
        self.continentLocations = [[0, 0, 0], [1, 1, 0], [-2, -1, 0]]  # Europe, Asia, NA
        self.INFECTION_RATE = 0.5
        self.max_attempts = 10000

import configparser


class Initialization:
    def __init__(self):
        # Load config values
        config = configparser.ConfigParser()
        config.read('config.ini')
        virusUsed = config.get('Simulation', 'virusName')
        # Set default values
        self.image_path = config.get('Simulation', 'image_path')
        self.radius = config.getfloat('Simulation', 'radius')
        self.pixel_height = config.getint('Simulation', 'pixel_height')
        self.pixel_width = config.getint('Simulation', 'pixel_width')
        self.canvas_height = config.getfloat('Simulation', 'canvas_height')
        self.canvas_width = config.getfloat('Simulation', 'canvas_width')
        self.num_points = config.getint('Simulation', 'num_points')
        self.initial_vector_x = config.getfloat('Simulation', 'initial_vector_x')
        self.initial_vector_y = config.getfloat('Simulation', 'initial_vector_y')
        self.continentLocations = self._parse_continent_locations(config)
        self.INFECTION_RATE = config.getfloat(virusUsed, 'INFECTION_RATE')
        self.distance_threshold = config.getfloat(virusUsed, 'distance_threshold')
        self.max_attempts = config.getint('Simulation', 'max_attempts')
        # self.print_everything()

    def _parse_continent_locations(self, config):
        # Parse continent locations from config
        continents = []
        continent_values = config.get('Simulation', 'continentLocations', fallback='').split('\n')
        for value in continent_values:
            if value:
                coords = list(map(float, value.split(',')))
                continents.append(coords)
        return continents

    def print_everything(self):
        print("Self.image_path: ", self.image_path)
        print("Self.radius: ", self.radius)
        print("Self.pixel_height: ", self.pixel_height)
        print("Self.pixel_width: ", self.pixel_width)
        print("Self.canvas_height: ", self.canvas_height)
        print("Self.canvas_width: ", self.canvas_width)
        print("Self.num_points: ", self.num_points)
        print("Self.initial_vector_x: ", self.initial_vector_x)
        print("Self.initial_vector_y: ", self.initial_vector_y)
        print("Self.continentLocations: ", self.continentLocations)
        print("Self.INFECTION_RATE: ", self.INFECTION_RATE)
        print("Self.distance_threshold: ", self.distance_threshold)

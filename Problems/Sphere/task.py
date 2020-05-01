class Sphere:
    # finish class Sphere here
    PI = 3.1415
    def __init__(self, radius):
        self.radius = round(radius, 2)
        self.volume = round((4 / 3) * self.PI * (self.radius ** 3), 2)

import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)

    def __str__(self):
        return f'''
Projectile details:
speed: {self.speed} m/s
height: {self.height} m
angle: {self.angle}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''
    def __calculate_displacement(self):
        """
        Calculate the displacement of a projectile.
        This function computes the horizontal displacement of a projectile
        based on its initial speed, launch angle, and height from which it is launched.
        It uses the equations of motion under constant gravitational acceleration.
        Returns:
            float: The horizontal displacement of the projectile.
        """
        horizontal_component = self.__speed * math.cos(self.__angle)
        vertical_component = self.__speed * math.sin(self.__angle)
        squared_component = vertical_component**2
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height
        sqrt_component = math.sqrt(squared_component + gh_component)

        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION

    def __calculate_y_coordinate(self, x):
        """
        Calculate the y-coordinate of a projectile at a given x-coordinate.
        This method uses the initial height, launch angle, speed, and gravitational acceleration
        to compute the y-coordinate of a projectile in motion.
        Args:
            x (float): The x-coordinate at which to calculate the y-coordinate.
        Returns:
            float: The y-coordinate of the projectile at the given x-coordinate.
        """
        height_component = self.__height
        angle_component = math.tan(self.__angle) * x
        acceleration_component = GRAVITATIONAL_ACCELERATION * x ** 2 / (
                2 * self.__speed ** 2 * math.cos(self.__angle) ** 2)
        y_coordinate = height_component + angle_component - acceleration_component

        return y_coordinate

    def calculate_all_coordinates(self):
        return [
            (x, self.__calculate_y_coordinate(x))
            for x in range(math.ceil(self.__calculate_displacement()))
        ]

    # Getters and setters
    @property
    def height(self):
        return self.__height

    @property
    def angle(self):
        return round(math.degrees(self.__angle))

    @property
    def speed(self):
        return self.__speed

    @height.setter
    def height(self, n):
        self.__height = n

    @angle.setter
    def angle(self, n):
        self.__angle = math.radians(n)

    @speed.setter
    def speed(self, s):
       self.__speed = s

    # Representation
    def __repr__(self):
        return f'{self.__class__}({self.speed}, {self.height}, {self.angle})'

class Graph:
    __slots__ = ('__coordinates')

    def __init__(self, coord):
        self.__coordinates = coord

    def __repr__(self):
        return f"Graph({self.__coordinates})"

    def create_coordinates_table(self):
        table = '\n  x      y\n'
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'

        return table

    def create_trajectory(self):
        """
        Generates a graphical representation of the trajectory based on the object's coordinates.

        The function rounds the coordinates to the nearest integer, determines the maximum x and y values,
        and creates a matrix to represent the trajectory. The trajectory is then plotted on the matrix
        using a predefined projectile symbol. The matrix is converted to a string format with axes labels
        and returned as a graph.

        Returns:
            str: A string representation of the trajectory graph.
        """
        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]

        x_max = max(rounded_coords, key=lambda i: i[0])[0]
        y_max = max(rounded_coords, key=lambda j: j[1])[1]

        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        for x, y in rounded_coords:
            matrix_list[-1 - y][x] = PROJECTILE

        matrix = ["".join(line) for line in matrix_list]

        matrix_axes = [y_axis_tick + row for row in matrix]
        matrix_axes.append(" " + x_axis_tick * (len(matrix[0])))

        graph = "\n" + "\n".join(matrix_axes) + "\n"

        return graph

def projectile_helper(speed, height, angle):

    ball = Projectile(speed, height, angle)
    coordinates = ball.calculate_all_coordinates()

    print(ball)
    graph = Graph(coordinates)
    print(graph.create_coordinates_table())
    print(graph.create_trajectory())

projectile_helper(10, 3, 45)

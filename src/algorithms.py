import numpy as np

def calculate_distance(point1, point2):
    """
    Calculates the Euclidean distance between two points in 3D space.

    Parameters:
    point1 (tuple): A tuple containing the x, y, and z coordinates of the first point.
    point2 (tuple): A tuple containing the x, y, and z coordinates of the second point.

    Returns:
    float: The Euclidean distance between the two points.
    """
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def calculate_angle(vector1, vector2):
    """
    Calculates the angle between two vectors in 3D space.

    Parameters:
    vector1 (tuple): A tuple containing the x, y, and z components of the first vector.
    vector2 (tuple): A tuple containing the x, y, and z components of the second vector.

    Returns:
    float: The angle between the two vectors in radians.
    """
    dot_product = np.dot(vector1, vector2)
    magnitude_product = np.linalg.norm(vector1) * np.linalg.norm(vector2)
    return np.arccos(dot_product / magnitude_product)

def calculate_force(mass1, mass2, distance):
    """
    Calculates the gravitational force between two masses.

    Parameters:
    mass1 (float): The mass of the first object in kilograms.
    mass2 (float): The mass of the second object in kilograms.
    distance (float): The distance between the two objects in meters.

    Returns:
    float: The gravitational force between the two objects in newtons.
    """
    G = 6.67430e-11  # gravitational constant
    return G * mass1 * mass2 / distance**2

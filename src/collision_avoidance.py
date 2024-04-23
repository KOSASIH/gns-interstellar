import math

def calculate_distance(pos1, pos2):
    """
    Calculates the distance between two positions.
    
    Parameters:
    pos1 (tuple): A tuple (x1, y1) representing the first position.
    pos2 (tuple): A tuple (x2, y2) representing the second position.
    
    Returns:
    float: The distance between the two positions.
    """
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def check_collision(pos1, pos2, radius1, radius2):
    """
    Checks if two positions are colliding.
    
    Parameters:
    pos1 (tuple): A tuple (x1, y1) representing the first position.
    pos2 (tuple): A tuple (x2, y2) representing the second position.
    radius1 (float): The radius of the first object.
    radius2 (float): The radius of the second object.
    
    Returns:
    bool: True if the positions are colliding, False otherwise.
    """
    distance = calculate_distance(pos1, pos2)
    return distance <= radius1 + radius2

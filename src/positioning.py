import numpy as np

def estimate_position(observations):
    """
    Estimates the position of a spacecraft based on multiple observations.
    
    Parameters:
    observations (list): A list of observations, where each observation is a tuple (time, distance, angle).
    
    Returns:
    tuple: A tuple (x, y) representing the estimated position of the spacecraft.
    """
    # Calculate the mean distance and angle
    distance = np.mean([obs[1] for obs in observations])
    angle = np.mean([obs[2] for obs in observations])

    # Convert polar coordinates to Cartesian coordinates
    x = distance * np.cos(angle)
    y = distance * np.sin(angle)

    return (x, y)

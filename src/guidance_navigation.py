import numpy as np

def calculate_course_correction(current_position, desired_position):
    """
    Calculates the course correction required to reach the desired position.

    Parameters:
    current_position (numpy array): A 3x1 array representing the current position of the spacecraft.
    desired_position (numpy array): A 3x1 array representing the desired position of the spacecraft.

    Returns:
    numpy array: A 3x1 array representing the course correction vector.
    """
    course_correction = desired_position - current_position
    return course_correction

def calculate_delta_v(current_velocity, desired_velocity):
    """
    Calculates the delta-v required to reach the desired velocity.

    Parameters:
    current_velocity (numpy array): A 3x1 array representing the current velocity of the spacecraft.
    desired_velocity (numpy array): A 3x1 array representing the desired velocity of the spacecraft.

    Returns:
numpy array: A 3x1 array representing the delta-v vector.
    """
    delta_v = desired_velocity - current_velocity
    return delta_v

def calculate_time_of_flight(initial_velocity, final_velocity, acceleration):
    """
    Calculates the time of flight required to reach the final velocity from the initial velocity.

    Parameters:
    initial_velocity (numpy array): A 3x1 array representing the initial velocity of the spacecraft.
    final_velocity (numpy array): A 3x1 array representing the final velocity of the spacecraft.
    acceleration (float): The acceleration of the spacecraft.

    Returns:
    float: The time of flight required to reach the final velocity from the initial velocity.
    """
    v_initial = np.linalg.norm(initial_velocity)
    v_final = np.linalg.norm(final_velocity)
    distance = v_final**2 - v_initial**2
    time_of_flight = np.sqrt(2*distance/acceleration)
    return time_of_flight

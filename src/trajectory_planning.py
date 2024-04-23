import math

def calculate_position(velocity, time, initial_position):
    """
    Calculates the position of an object after a certain time given its initial position and velocity.

    Parameters:
    velocity (tuple): A tuple containing the x, y, and z components of the velocity vector.
    time (float): The time in seconds.
    initial_position (tuple): A tuple containing the x, y, and z coordinates of the initial position.

    Returns:
    tuple: A tuple containing the x, y, and z coordinates of the final position.
    """
    x_velocity, y_velocity, z_velocity = velocity
    x_position, y_position, z_position = initial_position
    x_position += x_velocity * time
    y_position += y_velocity * time
    z_position += z_velocity * time
    return (x_position, y_position, z_position)

def calculate_velocity(acceleration, time, initial_velocity):
    """
    Calculates the velocity of an object after a certain time given its initial velocity and acceleration.

    Parameters:
    acceleration (tuple): A tuple containing the x, y, and z components of the acceleration vector.
    time (float): The time in seconds.
    initial_velocity (tuple): A tuple containing the x, y, and z components of the initial velocity vector.

    Returns:
    tuple: A tuple containing the x, y, and z components of the final velocity vector.
    """
    x_acceleration, y_acceleration, z_acceleration = acceleration
    x_velocity, y_velocity, z_velocity = initial_velocity
    x_velocity += x_acceleration * time
    y_velocity += y_acceleration * time
    z_velocity += z_acceleration * time
    return (x_velocity, y_velocity, z_velocity)

def calculate_trajectory(initial_position, initial_velocity, acceleration, time_steps):
    """
    Calculates the trajectory of an object given its initial position, initial velocity, acceleration, and the number of time steps.

    Parameters:
    initial_position (tuple): A tuple containing the x, y, and z coordinates of the initial position.
    initial_velocity (tuple): A tuple containing the x, y, and z components of the initial velocity vector.
    acceleration (tuple): A tuple containing the x, y, and z components of the acceleration vector.
    time_steps (int): The number of time steps.

    Returns:
    list: A list of tuples containing the x, y, and z coordinates of the trajectory.
    """
    trajectory = []
    position = initial_position
    velocity = initial_velocity
    for i in range(time_steps):
        trajectory.append(position)
        position = calculate_position(velocity, 1, position)
        velocity = calculate_velocity(acceleration, 1, velocity)
    return trajectory

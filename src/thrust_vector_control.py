import numpy as np

def calculate_thrust_vector(attitude_matrix, desired_thrust_direction):
    """
    Calculates the thrust vector required to align the spacecraft with the desired thrust direction.

    Parameters:
    attitude_matrix (numpy array): A 3x3 rotation matrix representing the current attitude of the spacecraft.
    desired_thrust_direction (numpy array): A 3x1 array representing the desired thrust direction.

    Returns:
    numpy array: A 3x1 array representing the required thrust vector.
    """
    rotation_matrix = np.transpose(attitude_matrix)
    thrust_vector = np.dot(rotation_matrix, desired_thrust_direction)
    return thrust_vector

def calculate_attitude_matrix(quaternion):
    """
    Calculates the rotation matrix from a quaternion.

    Parameters:
    quaternion (list): A list of four elements representing the quaternion [x, y, z, w].

    Returns:
    numpy array: A 3x3 rotation matrix.
    """
    qx, qy, qz, qw = quaternion
    xx = qx**2
    xy = qx*qy
    xz = qx*qz
    xw = qx*qw
    yy = qy**2
    yz = qy*qz
    yw = qy*qw
    zz = qz**2
    zw = qz*qw
    
    rotation_matrix = np.array([
        [1 - 2*yy - 2*zz, 2*xy - 2*zw, 2*xz + 2*yw],
        [2*xy + 2*zw, 1 - 2*xx - 2*zz, 2*yz - 2*xw],
[2*xz - 2*yw, 2*yz + 2*xw, 1 - 2*xx - 2*yy]
    ])
    
    return rotation_matrix

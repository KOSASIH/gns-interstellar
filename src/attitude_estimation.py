import numpy as np

def quaternion_to_rotation_matrix(quaternion):
    """
    Converts a quaternion to a rotation matrix.

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

def kalman_filter(x, P, u, F, B, Q, H, R):
    """
    Performs a single iteration of a Kalman filter.

    Parameters:
    x (numpy array): A 1xn array representing the state vector.
    P (numpy array): A nxn array representing the covariance matrix.
    u (numpy array): A 1xm array representing the control vector.
    F (numpy array): A nxn matrix representing the state transition matrix.
    B (numpy array): A nxm matrix representing the control matrix.
    Q (numpy array): A nxn matrix representing the process noisecovariance matrix.
    H (numpy array): A pxn matrix representing the measurement matrix.
    R (numpy array): A pxp matrix representing the measurement noise covariance matrix.

    Returns:
    tuple: A tuple containing the updated state vector and covariance matrix.
    """
    x_pred = np.dot(F, x) + np.dot(B, u)
    P_pred = np.dot(np.dot(F, P), F.T) + Q
    y = np.dot(H, x_pred) - z
    S = np.dot(np.dot(H, P_pred), H.T) + R
    K = np.dot(np.dot(P_pred, H.T), np.linalg.inv(S))
    x = x_pred + np.dot(K, y)
    P = np.dot(np.dot((np.eye(len(x)) - np.dot(K, H)), P_pred), (np.eye(len(x)) - np.dot(K, H)).T) + np.dot(np.dot(K, R), K.T)
    
    return x, P

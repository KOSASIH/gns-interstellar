import matplotlib.pyplot as plt

def plot_map(positions):
    """
    Plots a map of the spacecraft's position over time.
    
    Parameters:
    positions (list): A list of positions, where each position is a tuple (x, y, time).
    """
    # Extract the x, y, and time coordinates
    x = [pos[0] for pos in positions]
    y = [pos[1] for pos in positions]
    time = [pos[2] for pos in positions]

    # Plot the map
    plt.plot(x, y, '-o')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Spacecraft Map')
    plt.show()

# Mapping Algorithms

The mapping algorithms in this directory are designed to build and maintain maps of environments in real-time. These maps can be used for a variety of purposes, including localization, navigation, and path planning.

## Grid-Based Mapping

The grid-based mapping algorithm divides the environment into a grid of cells, each representing a small area of the environment. The algorithm maintains a probability distribution over the occupancy state of each cell, indicating whether the cell is likely to be occupied, empty, or unknown.

### Key Features

- Simple and efficient
- Works well in structured environments
- Can be extended to incorporate sensor data and perform data association

## Occupancy Grid Mapping

The occupancy grid mapping algorithm is an extension of the grid-based mapping algorithm that incorporates sensor data to improve the accuracy of the map. The algorithm uses a probabilistic model to estimate the occupancy state of each cell based on the sensor data.

### Key Features

- Incorporates sensor data to improve map accuracy
- Can handle uncertainty in sensor measurements
- Can be used for localization and path planning
- 
## Elevation Mapping

The elevation mapping algorithm is used to build maps of the elevation of the environment. The algorithm uses laser range finder data to estimate the elevation of the environment and build a 3D map.

### Key Features

- Can be used for terrain analysis and mapping
- Works well in outdoor environments
- Can be used for path planning in 3D environments

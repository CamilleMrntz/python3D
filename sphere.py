import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_sphere(radius=1, num_points=50):
    """
    Create a 3D sphere.

    Parameters:
    -----------
    radius : float, optional, default: 1
        Radius of the sphere.
    num_points : int, optional, default: 50
        Number of points used to create the sphere.

    Returns:
    --------
    x, y, z : arrays
        Coordinates of the points on the sphere.
    """
    phi = np.linspace(0, np.pi, num_points)
    theta = np.linspace(0, 2 * np.pi, num_points)
    phi, theta = np.meshgrid(phi, theta)

    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)

    return x, y, z

def plot_sphere(x, y, z):
    """
    Plot a 3D sphere using matplotlib.

    Parameters:
    -----------
    x, y, z : arrays
        Coordinates of the points on the sphere.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color='b', alpha=0.6, edgecolor='w')

    # Set the aspect ratio to be equal
    ax.set_box_aspect([1,1,1])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

if __name__ == "__main__":
    x, y, z = create_sphere(radius=1, num_points=100)
    plot_sphere(x, y, z)

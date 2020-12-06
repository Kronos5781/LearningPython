from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def get_pts(infile):
    data = np.loadtxt(infile, delimiter=' ')
    print(len(data))
    data = data[0::10]
    print(len(data))
    return data[0:,0], data[0:,1], data[0:,2], data[0:, 3] #returns X,Y,Z points skipping the first 12 lines


def plot_ply(infile):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y, z, _ = get_pts(infile)
    ax.scatter(x, y, z, c='b', marker='.')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()


if __name__ == '__main__':
    infile = 'cloud.ply'
    plot_ply(infile)
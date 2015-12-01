import numpy as np
from scipy import special, optimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    task1a()


def task1a():
    ageArray = []
    temperatureArray = []
    lengthArray = []
    f = open("data/fish.txt")
    for line in f.readlines():
        row = line.split("\n")
        #[' 1   14  25   620', '']
        values = row[0].split()
        ageArray.append(values[1])
        temperatureArray.append(values[2])
        lengthArray.append(values[3])
    np_ageArray = np.array(ageArray).astype(np.float)
    np_temperatureArray = np.array(temperatureArray).astype(np.float)
    np_lengthArray = np.array(lengthArray).astype(np.float)
    A = np.vstack([np_ageArray,np_temperatureArray,np.ones(len(np_ageArray))]).T
    w, m ,c   = np.linalg.lstsq(A,np_lengthArray)[0]
    estimatedPoints = []
    for i in range(0,len(ageArray)):
        estimatedPoints.append(np_ageArray[i] * w + np_temperatureArray[i] * m +c )
    fig = plt.figure()
    ax =  Axes3D(fig)
    ax.scatter(np_ageArray,np_temperatureArray,np_lengthArray,c="r",marker="o")
    ax.scatter(np_ageArray,np_temperatureArray,estimatedPoints,c="g",marker="^")
    for i,j,k,h in zip(np_ageArray,np_temperatureArray,np_lengthArray,estimatedPoints):
        ax.plot([i,i],[j,j],[k,h],color = 'b')
    X,Y = np.meshgrid(np_ageArray,np_temperatureArray)
    ax.plot_surface(X,Y,estimatedPoints, cmap=plt.cm.jet, cstride=1, rstride=1)
    ax.set_xlabel('Age')
    ax.set_ylabel('Temperature')
    ax.set_zlabel('Length')
    plt.show()

main()

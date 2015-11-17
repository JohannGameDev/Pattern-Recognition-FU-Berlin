import numpy as np
from scipy import special, optimize
import matplotlib.pyplot as plt

def main():
   task2a()


def task2a():
    numberOfSamples = 100
    meanArray1 = np.array([5,10])
    meanArray2 = np.array([5,5])
    meanArray3 = np.array([10,6])
    covarianceMatrix1 = np.matrix(((1,1),(1,1)))
    covarianceMatrix2 = np.matrix(((2,-1),(-1,2)))
    covarianceMatrix3 = np.matrix(((0.1,0),(0,3)))
    x,y = np.random.multivariate_normal(meanArray1,covarianceMatrix1,numberOfSamples).T
    plt.plot(x,y,'x')
    x,y = np.random.multivariate_normal(meanArray2,covarianceMatrix2,numberOfSamples).T
    plt.plot(x,y,'x')
    x,y = np.random.multivariate_normal(meanArray3,covarianceMatrix3,numberOfSamples).T
    plt.plot(x,y,'x')
    plt.axis('equal')
    plt.show()

main()

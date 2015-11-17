import numpy as np
from scipy import special, optimize
import matplotlib.pyplot as plt

def main():
   task2aSolution = task2a()
   task2b(task2aSolution)

def task2a():
    numberOfSamples = 100
    meanArray1 = np.array([5,10])
    meanArray2 = np.array([5,5])
    meanArray3 = np.array([10,6])
    covarianceMatrix1 = np.matrix(((1,1),(1,1)))
    covarianceMatrix2 = np.matrix(((2,-1),(-1,2)))
    covarianceMatrix3 = np.matrix(((0.1,0),(0,3)))
    generatedPointClass1 = np.random.multivariate_normal(meanArray1,covarianceMatrix1,numberOfSamples)
    generatedPointClass2 = np.random.multivariate_normal(meanArray2,covarianceMatrix2,numberOfSamples)
    generatedPointClass3 = np.random.multivariate_normal(meanArray3,covarianceMatrix3,numberOfSamples)
    x,y = generatedPointClass1.T
    plt.plot(x,y,'x')
    x,y = generatedPointClass2.T
    plt.plot(x,y,'x')
    x,y = generatedPointClass3.T
    plt.plot(x,y,'x')
    plt.axis('equal')
    plt.show()
    return([generatedPointClass1,generatedPointClass2,generatedPointClass3])

def task2b():
    print("Here will be task 2b")

main()

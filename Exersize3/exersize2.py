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
    # save Plot 
    plt.savefig("plot.png", dpi=96)
    plt.show()
    return([generatedPointClass1,generatedPointClass2,generatedPointClass3])

def task2b(valueArray):
    startMessage = "Task 2b started"
    print(startMessage)
    f = open("task2b","w")
    covClassA = np.cov(valueArray[0].T)
    covClassB = np.cov(valueArray[1].T)
    covClassC = np.cov(valueArray[2].T)
    covAMessage = "\nCovariance of class A(In Image of the plot Blue) is \n"+np.array_str(covClassA)
    covBMessage = "\nCovariance of class B(In Image of the plot Red)is \n"+np.array_str(covClassB)
    covCMessage = "\nCovariance of class C(In Image of the plot Green)is \n"+np.array_str(covClassC)
    f.write(covAMessage + covBMessage + covCMessage)
    f.close()
main()

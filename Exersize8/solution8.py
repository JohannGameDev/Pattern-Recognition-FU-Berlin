from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
import math
import matplotlib.pyplot as plt
data = []
xValues = []
yValues = []
beta_list = []
best_beta = np.array([[0],[0]])
def main():
    processData()
    old_beta =np.array([[0],[0]])
    alpha = 0.1
    for i in range(0,1001):
        new_beta = old_beta + alpha * next_gradient(old_beta)
        old_beta = new_beta
        if i in [1,10,100,1000] :
            beta_list.append(new_beta)
    best_beta = new_beta
    plot_data1a()#1a
    plot_data1c()

def plot_data1a():
    generate_data = []
    list = np.arange(-1.0,2.0,0.01)
    iteration = 1
    for beta in beta_list:
        for x in list:
            xVec = np.array([[1],[x]])
            generate_data.append(float(probability(xVec,beta)))
        plt.plot(list,generate_data,label="After "+str(iteration)+" iterations")
        generate_data = []
        iteration *= 10
    plt.plot(xValues,yValues,'o')
    plt.ylim([-0.25,1.25])
    plt.xlim([-1.0,2])
# Place a legend above this legend, expanding itself to
# fully use the given bounding box.
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
    plt.show()
def plot_data1c():
    fakeBestBetaListX = best_beta[0]
    fakeBestBetaListY = best_beta[1]
    fakeBestBetaListZ =log_likelihood(fakeBestBetaListX,fakeBestBetaListY) 
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    beta1List = np.arange(-100,100,0.5)
    beta2List = np.arange(-100,100,0.5)
    X,Y = np.meshgrid(beta1List,beta2List)
    zs = np.array([log_likelihood(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)
    ax.plot_surface(X, Y, Z)
    ax.scatter(fakeBestBetaListX,fakeBestBetaListY,fakeBestBetaListZ,c="y",marker="o",s=400)
    ax.set_xlabel('beta 0 ')
    ax.set_ylabel('beta 1')
    ax.set_zlabel('log-likelihood')
    plt.show()
def next_gradient(beta):
    local_gradient = np.array([[0],[0]])
    for i in range(0,len(data)):
        currentX = xValues[i]
        xVec = np.array([[1],[currentX]])
        local_gradient = np.add(local_gradient,xVec*(yValues[i] - probability(xVec,beta)))
    return local_gradient
def probability(x,beta):
    return np.exp(np.dot(np.transpose(beta),x))/(1 +np.exp(np.dot(np.transpose(beta),x)))
def log_likelihood(beta1,beta2):
    firstSum = 0
    for i in range(0,len(data)):
        firstSum += yValues[i] * beta1 + xValues[i] * beta2
    secondSum = 0
    for j in range(0,len(data)):
        secondSum +=math.log1p(1+math.exp(beta1 + beta2*xValues[j]))
    return firstSum - secondSum
def processData():
    file = open("data/spiders.txt")
    for line in file:
        temp = line.split(",")
        xValue = float(temp[0].strip())
        yValue =float (temp[1].strip())
        xValues.append(xValue)
        yValues.append(yValue)
        data.append((xValue,yValue))
main()

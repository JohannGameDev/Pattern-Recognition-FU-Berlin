import numpy as np
import random
import matplotlib.pyplot as plt
data = []
xValues = []
yValues = []
beta_list = []
def main():
    processData()
    old_beta =np.array([[0],[0]])
    alpha = 0.1
    for i in range(0,1001):
        new_beta = old_beta + alpha * next_gradient(old_beta)
        old_beta = new_beta
        if i in [1,10,100,1000] :
            beta_list.append(new_beta)
    plot_data()
def plot_data():
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

def next_gradient(beta):
    local_gradient = np.array([[0],[0]])
    for i in range(0,len(data)):
        currentX = xValues[i]
        xVec = np.array([[1],[currentX]])
        local_gradient = np.add(local_gradient,xVec*(yValues[i] - probability(xVec,beta)))
    return local_gradient
def probability(x,beta):
    return np.exp(np.dot(np.transpose(beta),x))/(1 +np.exp(np.dot(np.transpose(beta),x)))

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

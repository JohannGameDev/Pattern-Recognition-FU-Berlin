import numpy as np
import random
import matplotlib.pyplot as plt
data = []
xValues = []
yValues = []
def main():
    processData()
    old_beta =np.array([[0],[0]])
    alpha = 0.1
    for i in range(0,1000):
        new_beta = old_beta + alpha * next_gradient(old_beta)
        old_beta = new_beta
    plot_data(new_beta)
def plot_data(beta):
    generate_data = []
    list = np.arange(-1.0,2.0,0.01) 
    for x in list:
        xVec = np.array([[1],[x]])
        generate_data.append(float(probability(xVec,beta)))
    plt.plot(list,generate_data)
    plt.show()

def next_gradient(beta):
    local_gradient = np.array([[0],[0]])
    for i in range(0,len(data)-1):
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
        yValue =float (temp[0].strip())
        xValues.append(xValue)
        yValues.append(yValue)
        data.append((xValue,yValue))
main()

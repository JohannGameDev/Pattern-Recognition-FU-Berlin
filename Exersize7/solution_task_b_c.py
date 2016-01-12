import numpy as np
import random
from scipy import special, optimize
import matplotlib.pyplot as plt

def main():
    taskb()




def taskb():
    zeroList = []
    oneList = []
    f = open("data/klausur.txt")
    for line in f.readlines():
        row = line.replace("\n","").split(";")
        print(row)
        if row[1] == "1":
            oneList.append(row[0])
        if row[1] == "0":
            zeroList.append(row[0])
    zeroList = np.array(zeroList).astype(np.float)
    oneList = np.array(oneList).astype(np.float)
    print(zeroList)
    print(oneList)
    A = np.vstack((zeroList,np.ones(len(zeroList)))).T
    B = np.vstack((oneList,np.ones(len(oneList)))).T
    x_list_zero = [x for [x, y] in A]
    y_list_zero = [y for [x, y] in A]
    x_list_one = [x for [x, y] in B]
    y_list_one = [y for [x, y] in B]
    i =0
    k = 0
    w = np.array([0,0])
    oldW =np.array([0,0])
    wList = []
    row = 0
    j= 0 
    while i<440:
        rnd = random.random()
        choosePositiv = False
        if rnd >= 0.5:
            choosePositiv = True
        rndVec = []
        if choosePositiv:
            rndVec = B[random.randint(0,len(B)-1)]
        else:
            rndVec = A[random.randint(0,len(A)-1)]
        dot = np.vdot(rndVec,w)
        if choosePositiv:
            if dot < 0:
                oldW = w
                w = np.add(w,rndVec)
        else:
            if dot >= 0 :
                oldW = w
                w = np.subtract(w,rndVec)
        i = i+1
        if np.allclose(w,oldW):
            k = k+1
        #plt.subplot(10,10,i)
        #plt.scatter(x_list_zero,y_list_zero,marker=u"+")
        #plt.scatter(x_list_one,y_list_one,marker=u"o")
        #print(w)
    plt.scatter(x_list_zero,y_list_zero,marker=u"+")
    plt.scatter(x_list_one,y_list_one,marker=u"o")#plt.plot(w)
    plt.plot(w)
    plt.show()


main()

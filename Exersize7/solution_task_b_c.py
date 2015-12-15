import numpy as np
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
    plt.scatter(x_list_zero,y_list_zero)
    plt.scatter(x_list_one,y_list_one)
    print("plt show")
    plt.show()


main()

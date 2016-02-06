import numpy as np
import sys
import math
def main():
    f = open("data/sparse_checkboard.csv")
    data = []
    for line in f.readlines():
        line = line.replace("\n","")
        line = line.split(",")
        data.append((float(line[0]),float(line[1]),float(line[2])))
    alpha_vec = np.ones(20)
    classifiers = np.array([])
    #############################################
    classifiers = np.append(classifiers,[lambda x:2* (x[0] > 0) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[1] > 0) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[0] > 1) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[1] > 1) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[0] > 2) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[1] > 2) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[0] > 3) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[1] > 3) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[0] > 4) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[1] > 4) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[0] > 5) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[1] > 5) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[0] > 6) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[1] > 6) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[0] > 7) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[1] > 7) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[0] > 8) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[1] > 8) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[0] > 9) -1])
    classifiers = np.append(classifiers,[lambda x:2* (x[1] > 9) -1])
    ###########################################################################################
    print "The Classifiers are ordered in the folowing way : k_1(x) = 2* (x.X > 0 ) -1 ,k_2(x) = 2*(x.Y > 0) -1 ,k_3(x) = 2 * (x.X >  1) -1 , ... , k_20(x) = 2 * (x.Y > 9) -1 .The following written alpha's are in the same way as well as the classified ratio."
    ScoutMatrix = np.zeros((len(data),len(classifiers)))
    ClassifiedMatrix = np.ones((len(data),len(classifiers)))
    ####init weights with 1/numberOfPoints
    weights = np.array([])
    detectionRate = np.ones(500)
    for i in range(len(data)):
        weights = np.append(weights,np.array([1/float(len(data))]))
    entry = 0
    for i in range(len(data)):
        currentPoint = data[i]
        currentRow = np.array([])
        for j in range(len(classifiers)):
            if(classifiers[j](currentPoint)!=data[i][2]):#Check wheather the current classifier clasifies the data right
                ScoutMatrix[i,j] = 1#if the classifier classifies wrong : put an 1 in the scout matrix (later the weight will be *)
            ClassifiedMatrix[i,j] = classifiers[j](currentPoint)
    print "Solution a)"
    print "The  classification ratio(classifier got the right class) for the unweighted data set for k_1 ...k_m is "
    print 1 - np.dot(weights,ScoutMatrix)
    deleteIndizeList = []
    for m in range(len(classifiers)):
        sumOfClassifiedElements = np.dot(weights,ScoutMatrix)#vektor of detectionrate of all classifiers from all points
        #detectionValues = np.dot(detectionRate,ScoutMatrix)#only for debug purposes
        indexFirstMinClassifier = my_min(sumOfClassifiedElements,deleteIndizeList)
        deleteIndizeList.append(indexFirstMinClassifier)
        W = weights.sum()
        e_m = sumOfClassifiedElements[indexFirstMinClassifier]/W
        alpha_vec[indexFirstMinClassifier] = 1/float(2)* math.log((1-e_m)/e_m)
        #print "current alpha_vec " +str(alpha_vec[indexFirstMinClassifier])
        for i in range(len(data)):
            if ScoutMatrix[i,indexFirstMinClassifier]==1:
                weights[i] = weights[i] * np.exp(alpha_vec[indexFirstMinClassifier])
            else:
                weights[i] = weights[i] * np.exp(-alpha_vec[indexFirstMinClassifier])
    print "Solution b)"
    print "Alpha for k_1..k_m  printet out in the same order so alpha_1 ....alpha_m." 
    print str(alpha_vec)
    C = np.dot(ClassifiedMatrix,alpha_vec.T)
    C =np.sign(C)
    correct =0
    for i in range(len(data)):
        if data[i][2] == C[i]:
            correct +=1
    print "solution c)"
    print "Correct classification of C for all points is : "+ str(correct) + " of " +str(len(data)) + ".So the ratio is " + str(correct/float(len(data)))


#get min from the list of classifiers but only if the min is not at an position that was drafted before
def my_min(indizeList,dontTakeThisIndizeList):
    currentMin = sys.maxint
    for i in range(len(indizeList)):
            if (indizeList[i] < currentMin or 1- indizeList[i] < currentMin)and  not(i in(dontTakeThisIndizeList)):
                currentMin = indizeList[i]
                currentMinIndize = i
    return currentMinIndize

main()

import numpy as np
from scipy.special import expit
import random as rnd
def main():
    S = np.array([[0,0,0],[0,1,1],[1,0,1],[1,1,0]])
    W1BIAS = np.array([[rnd.uniform(-1,1),rnd.uniform(-1,1)],[rnd.uniform(1,-1),rnd.uniform(-1,1)],[rnd.uniform(-1,1),rnd.uniform(-1,1)]])
    W2Bias = np.array([[rnd.uniform(-1,1)],[rnd.uniform(-1,1)],[rnd.uniform(-1,1)]])
    W1 = np.delete(W1BIAS,2,0)
    W2 = np.delete(W2Bias,2,0)
    totalError = 1
    gamma = 10
    threshold = 0.000000001
    while float(totalError) > threshold:
        s = S[rnd.randint(0,3)]
        X = np.array([[s[0],s[1],1]])
        t = np.array([s[2]])      #target
        print "target"
        print t
        O1 = expit(np.dot(X,W1BIAS))
        print "O1"
        print O1
        D1 = np.array([[O1[0][0] * (1-O1[0][0]),0],[0,O1[0][0] * (1- O1[0][0])]]) # Derivative Matrix,on the diagonal the derivatives of inner node are stored
        print "O1"
        print O1
        O1BIAS = np.append(O1,1)
        #O1BIAS = np.append(O1,1)
        print "O1BIAS"
        print O1BIAS
        O2 = np.array(expit(np.dot(O1BIAS,W2Bias)))
        D2 = np.array([[np.dot(O2,1 - O2)]])
        print "Derivitive 2"
        print D2
        print "o2"
        print O2
        tempError = np.subtract(O2,np.array([t]))
        print "TEmpEroor"
        print tempError
        print "dot product"
        print np.dot(tempError,tempError)
        e = 1/float(2) * np.dot(tempError,tempError)
        print "error"
        print e
        E = np.array([O2 -t]) #derivative of e
        SDelta2 = np.dot(D2,E)# SDelta stands for small delta
        print "small delta 2"
        print SDelta2
        print " "
        DELTAW2 = -gamma *np.dot(SDelta2,np.array([O1BIAS]))
        print "DeltaW2"
        print DELTAW2
        print "S"
        print s
        SDelta1 = np.dot(np.dot(D1,W2),SDelta2)
        print "SDELta1"
        print SDelta1
        DELTAW1 = -gamma *np.dot(SDelta1,np.array([s]))
        print "DeltaW1"
        print DELTAW1
        print "W1 und w2"
        print W1BIAS
        print W2Bias
        W1BIAS = np.subtract(W1BIAS,np.transpose(DELTAW1))
        W2Bias = np.subtract(W2Bias,np.transpose(DELTAW2))
        totalError = e
        print "totalError"
        print float(totalError)
        print "ITERATTION"
    print W1BIAS
    print W2Bias

main()



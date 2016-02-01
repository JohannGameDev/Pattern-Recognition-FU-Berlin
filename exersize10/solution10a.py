import numpy as np
import math as m

#alpha=10.0
gamma_min = 0.01 
gamma_max = 20
d = 0.2#factor that will be multiplied if gradient switches the side d < 1
u = 1.5#factor that will be multiplied if gradient stays on the same side u >1
n=2
k=2
m=1
W1 = np.matrix(np.random.random((n+1, k)))
W2 = np.matrix(np.random.random((k+1, m)))
input = np.matrix('0 0; 1 0; 0 1; 1 1')
output = np.matrix('0; 1; 1; 0')
OLD_GRADIENT_W2 =  np.ones((k+1,m))
OLD_GRADIENT_W1 =  np.ones((n+1,k))
OLD_GAMMA_W2 =  np.zeros((k+1,m))
OLD_GAMMA_W1 =  np.zeros((n+1,k))
E=1
CURRENT_GAMMA_W2=  np.ones((k+1,m))
CURRENT_GAMMA_W1 =  np.ones((n+1,k))
def getCurrentGamma(oldGradient,currentGradient,oldGamma):
    print "oldGradient " +str(oldGradient)
    print "currentGradient " +str(currentGradient)
    print "oldGamme " +str(oldGamma)
    if float(oldGradient) * float(currentGradient) > 0:
        print "minimum in same side"
        print min(oldGamma*u,gamma_max)
        return min(oldGamma*u,gamma_max)
    elif float(oldGradient)* float(currentGradient) < 0:
        print "maximum on other side"
        print max(oldGamma*d,gamma_min)
        return max(oldGamma*d,gamma_min)
    else:
        print "third elseblock "+ str(oldGamma)
        return oldGamma

while E > 1e-5:

    delta_W2 = np.zeros((k+1,m))
    delta_W1 = np.zeros((n+1,k))

    E=0
    for i in range(len(input)):

        o=input[i]
        y = output[i]

        o_dach = np.append(o, [[1]], axis=1)

        net1 = o_dach*W1
        o1 = 1.0/(1+np.exp(-net1))

        net2 = np.append(o1, [[1]], axis=1)*W2
        o2 = 1.0/(1+np.exp(-net2))

        e = (o2-y).T

        f = np.power(e,2)/2.0
        print "PRINT SUN"
        print sum(f)
        E = E+sum(f)
# %        E = sum(f)

        a1 = np.multiply(o1,(1-o1))
        D1 = np.diag(np.array(a1)[0])

        a2 = np.multiply(o2,(1-o2))
        D2 = np.diag(np.array(a2)[0])

        s2 = D2*e
        s1=D1*W2[:-1, :]*s2

        # delta_W2=(-alpha*s2 * np.append(o1, [[1]], axis=1)).T
        # delta_W1=(-alpha*s1 * np.append(o, [[1]], axis=1)).T
        # W1=W1+delta_W1
        # W2=W2+delta_W2

        #delta_W1=delta_W1+(-alpha*s1 * np.append(o, [[1]], axis=1)).T
        #delta_W2=delta_W2+(-alpha*s2 * np.append(o1, [[1]], axis=1)).T
        CURRENT_GRADIENT_W2 = (s2 *np.append(o1, [[1]], axis=1)).T
        CURRENT_GRADIENT_W1= (s1 *np.append(o, [[1]], axis=1)).T
        #calculate gamma for each weight for W2
        print " Old Gamma w1"
        print OLD_GAMMA_W1
        print "Old gamma w2"
        print OLD_GAMMA_W2
        print "CURRENT_GAMMA_W1 :" 
        print CURRENT_GAMMA_W1
        print "CURRENT_GAMMA_W2 :" 
        print CURRENT_GAMMA_W2
        print "Current OLD_GRADIENT_W1"
        print OLD_GRADIENT_W1
        print "print old Gradient W2"
        print OLD_GRADIENT_W2
        print "Current CURRENT_GRADIENT_W1"
        print CURRENT_GRADIENT_W1
        print "Current CURRENT_GRADIENT_W2"
        print  CURRENT_GRADIENT_W2
        for i in range(0,1,2):
            CURRENT_GAMMA_W2.itemset(i,getCurrentGamma(OLD_GRADIENT_W2.item(i),CURRENT_GRADIENT_W2.item(i),OLD_GAMMA_W2.item(i)))
        OLD_GAMMA_W2 = CURRENT_GAMMA_W2
        OLD_GRADIENT_W2 = CURRENT_GRADIENT_W2
        #calculate gamma for each weight for W2
        for i in range(0,1,2):
            for j in range(0,1):
                CURRENT_GAMMA_W1.itemset((i,j),getCurrentGamma(OLD_GRADIENT_W1.item((i,j)),CURRENT_GRADIENT_W1.item((i,j)),OLD_GAMMA_W1.item((i,j))))
                print "After setting current gamma" + str(CURRENT_GAMMA_W1.item((i,j)))
        OLD_GAMMA_W1 = CURRENT_GAMMA_W1
        OLD_GRADIENT_W1 = CURRENT_GRADIENT_W1

        #assign oldgradient the current gradient

    for i in range(k+1):
        W2.itemset(i,W2.item(i)-CURRENT_GAMMA_W2.item(i) * np.sign(CURRENT_GRADIENT_W2.item(i)))
    for i in range(n+1):
        for j in range(k):
            W1.itemset((i,j),W1.item((i,j)) -CURRENT_GAMMA_W1.item((i,j)) * np.sign(CURRENT_GRADIENT_W1.item((i,j))))
    print "W1 and W2"        
    print W1
    print W2
    #W1=W1+delta_W1
    #W2=W2+delta_W2
    print "ERROR " + str(E)

print W1
print W2




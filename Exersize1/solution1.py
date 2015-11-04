import random
import struct
import math
import Image
import numpy as np
import cv2

def getLabelList(fileName):
	labelList = []
	f = open(fileName,'rb')#open file in read binary mode
	myByteBuffer =  bytearray(f.read());#create a byteArray
	numberOfLabels = struct.unpack_from(">i",myByteBuffer,4)#">i" stands for big endian 32 bit (4 Byte) Integer required by the file specification  
	#print(numberOfItems);
	offsetLabel = 8 # bytes representing the label starts a posstion 8 
	for i in range(0,numberOfLabels[0]):
		labelList.append(struct.unpack_from("B",myByteBuffer,i+offsetLabel)[0])#"B" means unsigned char (one byte).unpack gives always tuple so the first argument can be extracted with [0]	
		#print(struct.unpack_from("B",myByteBuffer,i)[0])	
	return labelList

def getImages(fileName):
	f = open(fileName,"rb")
	myByteBuffer = bytearray(f.read())
	numberOfImages = struct.unpack_from(">i",myByteBuffer,4)[0]
	numberOfColumns = struct.unpack_from(">i",myByteBuffer,8)[0]
	numberOfRows = struct.unpack_from(">i",myByteBuffer,12)[0]
	offsetImages = 16
	imageWidth = numberOfColumns
	imageHeight = numberOfRows
	bytesPerImage = imageWidth * imageHeight
	images = []
	for i in range(0,numberOfImages):#iterate through images 	
		tempImage = []
		for j in range(i*bytesPerImage, i*bytesPerImage + bytesPerImage,imageWidth):#Iterate through rows of current Image
			tempRow = []
			for k in range(j,j+imageWidth):#iterate through bytes(greyscale) in rows
				tempRow.append(struct.unpack_from("B",myByteBuffer,k)[0])
			tempImage.append(tempRow)
		images.append(tempImage)
	return images
#print(getLabelList("data/train-labels.idx1-ubyte"))
#print (getLabelList('data/t10k-labels.idx1-ubyte'))
def saveImages(byteImageList):
	i = 0
	for byteImage in byteImageList:
		i = i+1
		#print(byteImage)
		im = Image.new("L",(28,28))
		im.putdata(byteImage)
		im.save("images/number" + str(i) +  ".png",'PNG')
		#print(list(im.getdata()))


#byteImageList =  getImages("data/t10k-images.idx3-ubyte")
def kNearestNeighbours(k,trainingImages,trainingLabels,whatIsIt):
    #print(k)
    #print(whatIsIt[1])
    bytesPerImage = 28 * 28
    resultList = []#save euclidean distance and which Label it has in a tupel as a list
    bucketList = [0,0,0,0,0,0,0,0,0,0]#A List which saves how many neighbours which specific index there are
    for i in range(0,len(trainingImages)):#prepare 2d-array of bytes to one-diminsial array(26*26 Vector)
        #print("Which Image: " + str(i) + "lenList: "+ str(len(trainingImages))+ "len labels" + str(len(trainingLabels)))
        currentTrainingsVector = []
        myImage=trainingImages[i]
        for j in range(0,27): #28 each row from byteImage
            myRow = myImage[j]
            for e in range(0,27):
                currentTrainingsVector.append(myRow[e]) #index j define the row of the Image which is located at 28*28(one Image) * i(current processed iamage)	
        resultList.append((getEuclideanDistance(currentTrainingsVector,whatIsIt[0]),trainingLabels[i]))

    resultList.sort(key=lambda tup: tup[0])#sort by euclidean distance
    #print(resultList)
    for l in range(0,k):#for every k - neighbours save how much of which label there are 
        labelTupel = resultList[l]
        label = labelTupel[1]
        print(label)
        bucketList[label] +=1
    #print(bucketList)
    myMax = max(bucketList)#dicision
    winner = [i for i, j in enumerate(bucketList) if j == myMax]#making
    return winner

def getEuclideanDistance(vector1,vector2):
    eDistance = 1
    for i in range(0,len(vector1)):#for every element of both vector subtract them and add it to ediStance
        eDistance += math.pow((vector1[i] - vector2[i]),2)
    eDistance = math.sqrt(eDistance) #now take the sqaure root
    return eDistance

def getAllVectorList(imageList):
    allVectors = []
    for i in range(0,len(trainingImages)):#prepare 2d-array of bytes to one-diminsial array(26*26 Vector)
            currentTrainingsVector = []
            myImage=trainingImages[i]
            for j in range(0,27): #28 each row from byteImage
                myRow = myImage[j]
                for e in range(0,27):
                    currentTrainingsVector.append(myRow[e])
            allVectors.append(currentTrainingsVector)
    return allVectors

def minIndex(myList):
    myIndex = -1
    value = -1
    for element in myList:
       if(value < element):
        myIndex = myList.index(element)
    return myIndex


def kMeansMain(k,iteration,vectorList,labelList):
    kcluster = []
    generatedVectorList = []
    for generateRnd in range(0,k):
       rnd = random.randint(0,len(vectorList))
       kcluster.append(vectorList[rnd],labelList[rnd]) #a list with k tupel in form(rndVector,label)
    for vector in vectorList:
        euclideanList = []
        for cluster in kcluster:
            eDistance = getEuclideanDistance(cluster,vector)
            euclideanList.append(eDistance)   
        minIndex = minIndex(euclideanList)
        generatedVectorList.append(minIndex,vector,vectorList.index(vector)) #generated vectorList with (linked cluster,vector itself,label)


def getZeroVector():
    zeroVector = []
    for i in range(0,28*28):
        zeroVector.apend(0)
    return zeroVector

def addVectors(vec1,vec2):
    for i in range(0,len(vec1)):
        vec1[i] += vec2[i]
    return vec1

def nextIteration(kcluster,vectorList,iteration):
    middlePoints = []
    for i in range(0,len(kcluster)):
        middlePoints.append((getZeroVector(),0)) #list of tupels (middlePoint,numberOfVectors)
    for data in vectorList:
        middlePoints[data[0]][0] = addVectors(middlePoints[data[0]][0],data[1])
        middlePoints[data[0]][1] += 1
    for middlePoint in middlePoints:
        for e in middlePoint[0]:
            e = e/ middlePoint[1]

def aufgabe1():
     print("Aufgabe1")
     byteImages = getImages("data/t10k-images.idx3-ubyte")
     print(byteImages[len(byteImages)-1]) #vorletzer datenpunkt

def aufgabe2():
    print("aufgabe2")
    byteImages = getImages("data/t10k-images.idx3-ubyte")
    labels = getLabelList("data/t10k-labels.idx1-ubyte")
    kNeighbours = [1,3,11,37]
    resultList = [0,0,0,0]
    for k in kNeighbours:
        for n in range(4865,4875):
            tupel = ([j for i in byteImages[n] for j in i],labels[n])
            print("Search" + str(labels[n]))
            found = kNearestNeighbours(k,byteImages,labels,tupel)[0]
            print("found " + str(found))
            if(labels[n] == found):
                print("YEAH")
                print(kNeighbours.index(k))
                resultList[kNeighbours.index(k)] += 1
            print("---------------")
    print(resultList)

def aufgabe3():
   iterations = 100
   for k in [9,10,20]:
    print(k)
   #kMeansMain(k,iterations,getAllVectors("data/t10k-images.idx3-ubyte"),getLabelList("data/10k-labels.idx1-ubyte")) 

aufgabe1()
aufgabe2()
aufgabe3()

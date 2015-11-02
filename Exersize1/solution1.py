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
	for i in range(offsetLabel,numberOfLabels[0]):
		labelList.append(struct.unpack_from("B",myByteBuffer,i)[0])#"B" means unsigned char (one byte).unpack gives always tuple so the first argument can be extracted with [0]	
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
	print(k)
	print(whatIsIt[1]) 
	bytesPerImage = 28 * 28 
	resultList = []#save euclidean distance and which Label it has in a tupel as a list
	bucketList = [0,0,0,0,0,0,0,0,0]#A List which saves how many neighbours which specific index there are
	for i in range(0,len(trainingImage)/28):#prepare 2d-array of bytes to one-diminsial array(26*26 Vector)
		currentTrainingsVector = []
		for j in range(0,28): #28 each row from byteImage
			currentVector.append(trainingImages[j+i*bytesPerImage] #index j define the row of the Image which is located at 28*28(one Image) * i(current processed iamage)	
			resultList.append((getEuclideanDistance(currentTrainingsVector,whatIsIt[0]),trainingLabels[i])
	resultList.sort(key=lambda tup: tup[0])#sort by euclidean distance
	for l in range(0,k):#for every k - neighbours save how much of which label there are 
		bucketList[resultList[k][1]] +=1	
	myMax = max(bucketList)#dicision
	winner = [i for i, j in enumerate(a) if j == m]#making
	return winner

def getEuclideanDistance(vector1,vector2):
	eDistance = 0 
	for i in range(0,len(vector1)):#for every element of both vector subtract them and add it to ediStance
		eDistance += math.pow((vector1[i] - vector2[i]),2) 
	eDistance = math.sqrt(eDistance) #now take the sqaure root
	return eDistance


























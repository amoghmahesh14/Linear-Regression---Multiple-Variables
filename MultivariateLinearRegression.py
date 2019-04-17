import csv
import matplotlib.pyplot as plt
import numpy as np

def normalize(X):
	mean = np.mean(X,axis=0) # axis = 0 indicates that we take the mean of each column , axis=1 for row
	sd = np.std(X,axis=0)
	X = (X- mean)/ sd
	return mean,sd,X
#X*theta is same as theta*X we are not using matrix multiplication here
#each element is multiplied with corresponding element in the whokle code
	error=hofx-y
def costFuction(X,y,theta):
	hofx=np.sum(X*theta,axis=1) 
	squarederror=np.sum(np.square(error))
	cost = squarederror/(2*m)
	return cost

def gradientDescent(X,y,theta,alpha,iterations):
	for i in range(iterations):
		hofx=np.sum(X*theta,axis=1)
		error=hofx-y
		error=error[:,np.newaxis]
		temp=(alpha/m)*np.sum(error*X,axis=0)
		theta=theta-temp
	return theta

fp = open('ex1data2.txt' , 'r')
reader = csv.reader(fp , delimiter=',')
dataset = []
for row in reader:
	dataset.append(row)

data = np.array(dataset,dtype=int)
#print (np.array(dataset))
no_of_features = 2
m = len(dataset)
X = data[:,0:no_of_features]
y = data[:,no_of_features]
mean,sd,X=normalize(X)
ones=np.ones((m,1))
X=np.concatenate((ones,X),axis=1)

theta=[0,0,0]
alpha = 0.01
iterations = 1500


theta=gradientDescent(X,y,theta,alpha,iterations)
print(theta)

newX=[]

area=int(input("Enter square feet area:"))
newX.append(area)
rooms=int(input("Enter number of rooms:"))
newX.append(rooms)
newX=np.array(newX)
newX=(newX-mean)/sd
x1=np.array([1])
newX=np.concatenate((x1,newX))
price = np.sum(theta*newX)
print("Price of the house is:",price)
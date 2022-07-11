from pydoc import plain
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np


# Loading the data 
#x_train
X = pd.read_csv('/home/raghav/codes_new/Machine-Learning-from-scratch/01. Linear Regression/datasets/hardworkPaysOff/train/Linear_X_Train.csv').values
#y_train
y = pd.read_csv('/home/raghav/codes_new/Machine-Learning-from-scratch/01. Linear Regression/datasets/hardworkPaysOff/train/Linear_Y_Train.csv').values

theta = np.load("ThetaList.npy")

#100x2 - number of iteations,number of variables
T0 = theta[:,0]
T1 = theta[:,1]

plt.ion #on the interactive mode of matplotlib

for i in range(0,50,3):
    y_ = T1[i]*X + T0
    #points
    plt.scatter(X,y)
    #line
    plt.plot(X,y_,'red')
    plt.draw()
    plt.pause(1)
    plt.clf() #clear the last object
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 12:26:03 2017

@author: Ross
"""
import pandas
from pandas import read_csv
import matplotlib.pyplot as plt
from sklearn import svm 
import numpy as np
import scipy as sp
import DataConditioning
from sklearn.decomposition import PCA


train_data = DataConditioning.getTrainingData()


'''
Normalises data within the columns 
'''
def dimensionality_reduction():

    pca = PCA(n_components=14)
    X_PCA = pandas.DataFrame(pca.fit_transform(train_data))
    
    print(X_PCA.head(5))

dimensionality_reduction()

def visualise_items():
    '''
    The system can only process one chart at a time, thus each of these operations
    were conducted one at a time
    
    
      train_data["age"].plot.hist()
      train_data["job"].value_counts().plot(kind="bar")
      train_data["marital"].value_counts().plot(kind="bar")
      train_data["education"].value_counts().plot(kind="bar")
      train_data["default"].value_counts().plot(kind="bar")
      train_data["balance"].diff().hist(stacked= True, bins=50)
      train_data["housing"].value_counts().plot(kind="bar")
      train_data["loan"].value_counts().plot(kind="bar")
      train_data["contact"].value_counts().plot(kind="bar")
      train_data["day"].value_counts().plot(kind="bar")
      train_data["month"].value_counts().plot(kind="bar")
       train_data["duration"].plot.hist(bins= 100)
      train_data["campaign"].value_counts().plot(kind="bar")
      train_data["pdays"].plot.hist()
      train_data["previous"].value_counts().plot(kind="bar")
      train_data["poutcome"].value_counts().plot(kind="bar")
      train_data["subscribed"].value_counts().plot(kind="bar")
    '''

    
    
    '''
def scatter_items():
            
   
   numcol = 15
   j=0
   while j < 15:
     i=0
     while i < numcol: 
         print("cols:" + str(j) +" and "+ str(i))
         if j!=i and (i!=14 or j!=14):
    
             xpoints= train_data[[i]]
             ypoints = train_data[[j]]
             
             cPoints = train_data[[14]]
    
             plt.scatter(xpoints, ypoints, c=cPoints)
             plt.show()
         i=i+1
     j=j+1        
            
       
scatter_items()

XPoints= numpy.array(xpoints, ypoints)
XPoints= XPoints.T
YPoints = dataset[[16]]


def mean(data): 
    return np.mean(data)

def standardDev(data): 
    return sp.std(data)
'''
        
    
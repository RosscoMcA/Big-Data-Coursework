# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 12:26:03 2017

@author: Ross
"""

from pandas import read_csv
import matplotlib.pyplot as plt
from sklearn import svm 
import numpy as np
import scipy as sp
import DataConditioning


train_data = DataConditioning.getTrainingData()




def hist_items(data):
   fig, ax = plt.subplots()
   n, bins = np.histogram(data, 50)
   
   left = np.array(bins[:-1])
   right = np.array(bins[1:])
   bottom = np.zeros(len(left))
   top= bottom +n



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

    
    
 
def scatter_items(xData, yData):
    
  xpoints= xData
  ypoints = yData
  plt.scatter(xpoints, ypoints)
  plt.show()
          
scatter_items(train_data[[11], train_data[[0]])            
            
       

'''
XPoints= numpy.array(xpoints, ypoints)
XPoints= XPoints.T
YPoints = dataset[[16]]
'''

def mean(data): 
    return np.mean(data)

def standardDev(data): 
    return sp.std(data)
 
        
    
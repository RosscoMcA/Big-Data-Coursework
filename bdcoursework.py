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



def bar_items():
    train_data["job"].value_counts().plot(kind="bar")
    
    
bar_items()    
def scatter_items(data):
    numcol = 8
    j=0
    while j < 8:
        i=0
        while i < numcol: 
            print("cols:" + str(j) +" and "+ str(i))
            if j!=i:
                xpoints= data[i]
                ypoints = data[j]
    
                plt.scatter(xpoints, ypoints)
                plt.show()
            i=i+1
            
            
        j=j+1

'''
XPoints= numpy.array(xpoints, ypoints)
XPoints= XPoints.T
YPoints = dataset[[16]]
'''

def mean(data): 
    return np.mean(data)

def standardDev(data): 
    return sp.std(data)
 
        
    
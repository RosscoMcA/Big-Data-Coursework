# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:59:25 2017

@author: Ross
"""
import DataConditioning
from sklearn import svm 
import matplotlib.pyplot as plt
from sklearn.feature_selection import VarianceThreshold
import numpy as np

X = DataConditioning.getTrainingData()
sel = VarianceThreshold(threshold=(.5*(1-.5)))
sel.fit_transform(X)

numcol = 15
j=0
while j < 15:
  i=0
  while i < numcol: 
   print("cols:" + str(j) +" and "+ str(i))
   if j!=i and (i!=14 or j!=14):
    
    xpoints= X[[i]]
    ypoints = X[[j]]
             
    cPoints = X[[14]]
    
    plt.scatter(xpoints, ypoints, c=cPoints)
    plt.show()
   i=i+1
  j=j+1        
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
import sklearn.feature_selection
from sklearn.cross_validation import train_test_split



data = DataConditioning.getTrainingData()
x= data.drop('subscribed', 1)
y= data.subscribed
X_Train, X_Test, Y_Train, Y_Test = train_test_split(x, y, train_size=70, random_state=1)






    

'''
Normalises data within the columns 
'''
def dimensionality_reduction():

    pca = PCA(n_components=10)
    X_PCA = pandas.DataFrame(pca.fit_transform(data))
    
    print(X_PCA.head(5))

dimensionality_reduction()


def feature_selec():
    select = sklearn.feature_selection.SelectKBest(k=9)
    select_feature = select.fit(X_Train, Y_Train)
    indic_sel = select_feature.get_support(indices=True)
    colnames_select = [x.columns[i] for i in indic_sel]
    
    x_train_sel = X_Train[colnames_select]
    x_test_sel = X_Test[colnames_select]
    
    return x_train_sel, x_test_sel


final_train_case_x, final_test_case_x = feature_selec()
print(final_train_case_x)

def train(): 
    



















def visualise_items():
    '''
    The system can only process one chart at a time, thus each of these operations
    were conducted one at a time
    
    
      data["age"].plot.hist()
      data["job"].value_counts().plot(kind="bar")
      data["marital"].value_counts().plot(kind="bar")
      data["education"].value_counts().plot(kind="bar")
      data["default"].value_counts().plot(kind="bar")
      data["balance"].diff().hist(stacked= True, bins=50)
      data["housing"].value_counts().plot(kind="bar")
      data["loan"].value_counts().plot(kind="bar")
      data["contact"].value_counts().plot(kind="bar")
      data["day"].value_counts().plot(kind="bar")
      data["month"].value_counts().plot(kind="bar")
      data["duration"].plot.hist(bins= 100)
      data["campaign"].value_counts().plot(kind="bar")
      data["pdays"].plot.hist()
      data["previous"].value_counts().plot(kind="bar")
      data["poutcome"].value_counts().plot(kind="bar")
      data["subscribed"].value_counts().plot(kind="bar")
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
    
             xpoints= data[[i]]
             ypoints = data[[j]]
             
             cPoints = data[[14]]
    
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
        
    
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 12:02:06 2017

@author: Ross
"""
from pandas import read_csv
import matplotlib.pyplot as plt
from sklearn import svm 
import numpy as np


def outlier_ident(x):
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    inter_quart_r = q3-q1
    flr = q1-1.5*inter_quart_r
    cel = q3 + 1.5*inter_quart_r
    outlier_indices = list(x.index[(x<flr) | (x>cel)])
    return outlier_indices
    
def processOutliers(data, dataset):
    indices= outlier_ident(data)
        
    for item in indices:
       dataset.drop(item)
        
 

    return dataset

def getTrainingData():
   dataset = read_csv("bank.csv")
   
   dataset = dataset.drop(["contact", "poutcome", "month", "day"], axis=1)
    
   dataset = changeData(dataset)

   dataset = processOutliers(dataset["age"], dataset)
   dataset = processOutliers(dataset["job"], dataset)
   dataset = processOutliers(dataset["marital"], dataset)
   dataset = processOutliers(dataset["education"], dataset)
   dataset = processOutliers(dataset["balance"], dataset)
   dataset = processOutliers(dataset["duration"], dataset)
   dataset = processOutliers(dataset["campaign"], dataset)
   dataset = processOutliers(dataset["pdays"], dataset)
   dataset = processOutliers(dataset["previous"], dataset)
   
    
       
   return dataset
    





def changeData(dataset): 
    
    #mark zero values as missing or NaN 
    
    
    
    #count the number of Nan values in each column 
   
    
    
    
     # Numerical catergorisation of jobs within dataset 
     # 0 is unknown, 1 is admin., 2 is unemployed, 3 is management, 4 is housemaid
     # 5 is entrepreneur, 6 is student, 7 is blue-collar, 8 is self-employed
     # 9 is retired, 10 is technician, 11 is services
    dataset["job"]= dataset["job"].replace("unknown", 0)
    dataset["job"]= dataset["job"].replace("admin.", 1)
    dataset["job"]= dataset["job"].replace("unemployed", 2)
    dataset["job"]=dataset["job"].replace("management", 3)
    dataset["job"]=dataset["job"].replace("housemaid", 4)
    dataset["job"]=dataset["job"].replace("entrepreneur", 5)
    dataset["job"]=dataset["job"].replace("student", 6)
    dataset["job"]=dataset["job"].replace("blue-collar", 7)
    dataset["job"]=dataset["job"].replace("self-employed", 8)
    dataset["job"]=dataset["job"].replace("retired", 9)
    dataset["job"]=dataset["job"].replace("technician", 10)
    dataset["job"]=dataset["job"].replace("services", 11)
     
     #Numerical categorisation of maritial status 
     # 0 is single, 1 is married, 2 is divorced or widowed
    dataset["marital"]= dataset["marital"].replace("single",1)
    dataset["marital"]= dataset["marital"].replace("married",2)
    dataset["marital"]= dataset["marital"].replace("divorced",3)
     
    
    dataset["education"]=dataset["education"].replace("unknown", 0)
    dataset["education"]=dataset["education"].replace("secondary", 1)
    dataset["education"]=dataset["education"].replace("primary", 2)
    dataset["education"]=dataset["education"].replace("tertiary", 3)
     
    
  
     
    dataset["default"]=dataset["default"].replace("yes", 1)
    dataset["default"]=dataset["default"].replace("no", 0)
     
    
    dataset["housing"]= dataset["housing"].replace("yes", 1)
    dataset["housing"]=dataset["housing"].replace("no", 0)
     
    dataset["loan"]=dataset["loan"].replace("yes", 1)
    dataset["loan"]=dataset["loan"].replace("no", 0)
     
    
     
    
    '''
     Numerical categorisation of binary options for whether the customer subscribed or not
     1 is yes, 0 is No
    '''
    dataset["subscribed"]=dataset["subscribed"].replace("no", 0)
    dataset["subscribed"]=dataset["subscribed"].replace("yes", 1)
     
    dataset["age"]= dataset["age"].replace("0", np.NaN)
    dataset["job"]= dataset["job"].replace("0", np.NaN)
    dataset["education"]= dataset["education"].replace(0, np.NaN)
    dataset["pdays"]=dataset["pdays"].replace(-1, np.NaN)
    dataset = dataset.replace(" ", np.nan)
    dataset.dropna(inplace=True)
    return dataset



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
X_Train, X_Test, Y_Train, Y_Test = train_test_split(x, y, train_size=70, random_state=3)





'''
Normalises data within the columns 
'''
def dimensionality_reduction():

    pca = PCA(n_components=10)
    X_PCA = pandas.DataFrame(pca.fit_transform(data))
    
    print(X_PCA.head(5))

#dimensionality_reduction()


def feature_selec():
    select = sklearn.feature_selection.SelectKBest(k=12)
    select_feature = select.fit(X_Train, Y_Train)
    indic_sel = select_feature.get_support(indices=True)
    colnames_select = [x.columns[i] for i in indic_sel]
    
    x_train_sel = X_Train[colnames_select]
    x_test_sel = X_Test[colnames_select]
    
    return x_train_sel, x_test_sel


final_train_case_x, final_test_case_x = feature_selec()
#print(final_train_case_x)


def create_model():
    
    #svm_x = np.array([final_train_case_x["education"], final_train_case_x["default"]])
    print("Creating the model")
    classifier = svm.SVC(C=1, kernel="linear")
    
    classifier.fit(X_Train, Y_Train)
    print("Model is built")
    
    test_Model(classifier)
    
    

def test_Model(prediction_model):
    #test_items = np.array([X_Test["education"], X_Test["default"]])
    predict_results = [int(a) for a in prediction_model.predict(X_Test)]
    correct_total = sum(int(a==y) for a, y in zip(predict_results, Y_Test))
    
    print("Results of prediction are: ")
    print("%s of %s values correct." % (correct_total, len(Y_Test)))

create_model()
    
    

#def visualise_items():
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

    
    

def scatter_items():
    plt.scatter(data[""], data["marital"], c=data["subscribed"])
    plt.show()
 
#scatter_items()     
       
#scatter_items()





        
    
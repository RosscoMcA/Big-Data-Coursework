# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 12:26:03 2017

@author: Ross
"""

from pandas import read_csv
import matplotlib.pyplot as plt
from sklearn import svm 
import numpy 

dataset = read_csv("bank.csv", header=None)


# Numerical catergorisation of jobs within dataset 
# 0 is unknown, 1 is admin., 2 is unemployed, 3 is management, 4 is housemaid
# 5 is entrepreneur, 6 is student, 7 is blue-collar, 8 is self-employed
# 9 is retired, 10 is technician, 11 is services
dataset[[1]] = dataset[[1]].replace("unknown", 0)
dataset[[1]] = dataset[[1]].replace("admin.", 1)
dataset[[1]] = dataset[[1]].replace("unemployed", 2)
dataset[[1]] = dataset[[1]].replace("management", 3)
dataset[[1]] = dataset[[1]].replace("housemaid", 4)
dataset[[1]] = dataset[[1]].replace("entrepreneur", 5)
dataset[[1]] = dataset[[1]].replace("student", 6)
dataset[[1]] = dataset[[1]].replace("blue-collar", 7)
dataset[[1]] = dataset[[1]].replace("self-employed", 8)
dataset[[1]] = dataset[[1]].replace("retired", 9)
dataset[[1]] = dataset[[1]].replace("technician", 10)
dataset[[1]] = dataset[[1]].replace("services", 11)

#Numerical categorisation of maritial status 
# 0 is single, 1 is married, 2 is divorced or widowed
dataset[[2]] = dataset[[2]].replace("single",0)
dataset[[2]] = dataset[[2]].replace("married",1)
dataset[[2]] = dataset[[2]].replace("divorced",2)

'''
Numerical categorisation of education levels 
0 is unknown, 1 is secondary, 2 is primary, and 3 is teriary
'''
dataset[[3]] = dataset[[3]].replace("unknown", 0)
dataset[[3]] = dataset[[3]].replace("secondary", 1)
dataset[[3]] = dataset[[3]].replace("primary", 2)
dataset[[3]] = dataset[[3]].replace("tertiary", 3)

'''
Numerical categorisation of binary results in regards to having credit in default 
(yes is 1, no is 0)
'''
dataset[[4]] = dataset[[4]].replace("yes", 1)
dataset[[4]] = dataset[[4]].replace("no", 0)

'''
Numerical categorisation of binary results in regards to having a personal loan
yes is 1 and no is 0
'''
dataset[[6]] = dataset[[6]].replace("yes", 1)
dataset[[6]] = dataset[[6]].replace("no", 0)

'''
Numerical categorisation of contact methods for a customer
0 is unknown, 1 is telephone, 2 is cellular 
'''
dataset[[8]] = dataset[[8]].replace("unknown", 0)
dataset[[8]] = dataset[[8]].replace("telephone", 1)
dataset[[8]] = dataset[[8]].replace("cellular", 2)


'''
Numerical categorisation of the month of last contact
numbers correspond with the order of the months occurence
'''
dataset[[10]] = dataset[[10]].replace("jan", 1)
dataset[[10]] = dataset[[10]].replace("feb", 2)
dataset[[10]] = dataset[[10]].replace("mar", 3)
dataset[[10]] = dataset[[10]].replace("apr", 4)
dataset[[10]] = dataset[[10]].replace("may", 5)
dataset[[10]] = dataset[[10]].replace("jun", 6)
dataset[[10]] = dataset[[10]].replace("jul", 7)
dataset[[10]] = dataset[[10]].replace("aug", 8)
dataset[[10]] = dataset[[10]].replace("sep", 9)
dataset[[10]] = dataset[[10]].replace("oct", 10)
dataset[[10]] = dataset[[10]].replace("nov", 11)
dataset[[10]] = dataset[[10]].replace("dec", 12)

'''
Numerical categorisation of the outcome from last campaign 
0 is unknown, 1 is other, 2 is failure, 3 is success
'''
dataset[[15]] = dataset[[15]].replace("unknown", 0)
dataset[[15]] = dataset[[15]].replace("other", 1)
dataset[[15]] = dataset[[15]].replace("failure", 2)
dataset[[15]] = dataset[[15]].replace("success", 3)

'''
Numerical categorisation of binary options for whether the customer subscribed or not
1 is yes, 0 is No
'''
dataset[[16]] = dataset[[16]].replace("no", 0)
dataset[[16]] = dataset[[16]].replace("yes", 1)











print(dataset[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]])
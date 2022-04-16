#Logistic regression model to predict heart disease
#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the datset
dataset=pd.read_csv(r"C:\Users\abhir\Downloads\logistic regression\framingham.csv")

#finding the x- independent and y-dependent
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

#imputing the missing values
from sklearn.impute import SimpleImputer
imputer=SimpleImputer()
imputer.fit(x)
x=imputer.transform(x)

#splitting the dataset
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test = sc.transform(x_test)

#training the model with logistic regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(x_train,y_train)

#predicting the ytest
y_pred = classifier.predict(x_test)

#confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)

from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test, y_pred)
print(ac)

from sklearn.metrics import classification_report
cr=classification_report(y_test, y_pred)
cr

#calculating the bias and variance
bias=classifier.score(x_train,y_train)
print(bias)
variance=classifier.score(x_test, y_test)
print(variance)
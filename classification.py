import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn import metrics, cross_validation
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn import svm
from itertools import cycle
from scipy import interp
import statsmodels.api as sm

data = pd.read_csv('/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/LGA/G2.csv')
print(data.shape)
print(data.groupby('y').size())

feature_names = ['lat',	'lng', 'day', 'time', 'Median_age_persons',
                 'Average_num_psns_per_bedroom','Average_household_size',
                 'Lang_spoken_home_Eng_only_P', 'Australian_citizen_P','Marital_Prop']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X = data[feature_names]
y = data['y']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

print('Accuracy of Logistic regression classifier on training set: {:.2f}'
     .format(logreg.score(X_train, y_train)))
print('Accuracy of Logistic regression classifier on test set: {:.2f}'
     .format(logreg.score(X_test, y_test)))

from sklearn.feature_selection import RFE
classifier = LogisticRegression()
selector = RFE(classifier, 10, step=1)
selector = selector.fit(X, y)
print(selector.support_)

predicted = cross_validation.cross_val_predict(logreg, X, y, cv=10)
print(metrics.accuracy_score(y, predicted))
print(metrics.classification_report(y, predicted))

logit_model = sm.MNLogit(y,X)
result = logit_model.fit()
print(result.summary())

print(logreg.intercept_)
print(logreg.coef_)

# Binarize the output
y = label_binarize(y, classes=[1, 2, 3])
n_classes = y.shape[1]


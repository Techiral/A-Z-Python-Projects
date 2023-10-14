# -*- coding: utf-8 -*-
"""Diabetes Classifier.ipynb


# PIMA Indians Diabetes Classifier

### Context

This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.

## Importing the required libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

"""## Importing the dataset and checking the data"""



pima_df = pd.read_csv("diabetes.csv")

pima_df.head()

pima_df.tail()

pima_df.describe()

pima_df.info()

pima_df.isnull().sum()

"""## Exploratory Data Analysis (EDA)"""

plt.figure(figsize=(10,5))
sns.countplot(pima_df['Outcome'])
plt.title("Count of the Outcomes")
plt.xlabel("Diabetes Outcome (Binary)")
plt.ylabel("Count")

plt.figure(figsize=(8,5))
pima_df['Age'].hist()
plt.title("Histogram of Age")
plt.xlabel("Age")
plt.ylabel("Count")

plt.figure(figsize=(10,7))
sns.boxplot(x='Outcome', y='Pregnancies', data=pima_df)
plt.title("How Pregnancies Influences the Diabetes Outcome")
plt.xlabel("Diabetes Outcome (Binary)")
plt.ylabel("Pregnancy")

plt.figure(figsize=(10,7))
sns.boxplot(x="Outcome", y="Glucose", data= pima_df)
plt.title("How Glucose Influences the Diabetes Outcome")
plt.xlabel("Diabetes Outcome (Binary)")
plt.ylabel("Glucose")

plt.figure(figsize=(10,7))
sns.boxplot(x="Outcome", y="BloodPressure", data= pima_df)
plt.title("How BP Influences the Diabetes Outcome")
plt.xlabel("Diabetes Outcome (Binary)")
plt.ylabel("BP")

plt.figure(figsize=(10,7))
sns.boxplot(x="Outcome", y="SkinThickness", data= pima_df)
plt.title("How Skin Thickness Influences the Diabetes Outcome")
plt.xlabel("Diabetes Outcome (Binary)")
plt.ylabel("Skin Thickness")

plt.figure(figsize=(10,7))
sns.boxplot(x="Outcome", y="Insulin", data= pima_df)
plt.title("How Insulin Influences the Diabetes Outcome")
plt.xlabel("Diabetes Outcome (Binary)")
plt.ylabel("Insulin")

plt.figure(figsize=(10,7))
sns.boxplot(x="Outcome", y="BMI", data= pima_df)
plt.title("How BMI Influences the Diabetes Outcome")
plt.xlabel("Diabetes Outcome (Binary)")
plt.ylabel("BMI")

plt.figure(figsize=(10,7))
sns.boxplot(x="Outcome", y="DiabetesPedigreeFunction", data= pima_df)
plt.title("How Diabetes Pedigree Function Influences the Diabetes Outcome")
plt.xlabel("Diabetes Outcome (Binary)")
plt.ylabel("Diabetes Pedigree Function")

plt.figure(figsize=(10,7))
sns.boxplot(x="Outcome", y="Age", data= pima_df)
plt.title("How Age Influences the Diabetes Outcome")
plt.xlabel("Diabetes Outcome (Binary)")
plt.ylabel("Age")

plt.figure(figsize=(10,7))
sns.scatterplot(x="Age", y="Glucose", hue="Outcome", data= pima_df)
plt.title("Age Vs. Glucose based on Outcome")
plt.xlabel("Age")
plt.ylabel("Glucose")

plt.figure(figsize=(10,7))
sns.scatterplot(x="Age", y="BloodPressure", hue="Outcome", data= pima_df)
plt.title("Age Vs. BP based on Outcome")
plt.xlabel("Age")
plt.ylabel("BP")

plt.figure(figsize=(10,7))
sns.scatterplot(x="Age", y="SkinThickness", hue="Outcome", data= pima_df)
plt.title("Age Vs. Skin Thickness based on Outcome")
plt.xlabel("Age")
plt.ylabel("Skin Thickness")

plt.figure(figsize=(10,7))
sns.scatterplot(x="Age", y="Insulin", hue="Outcome", data= pima_df)
plt.title("Age Vs. Insulin based on Outcome")
plt.xlabel("Age")
plt.ylabel("Insulin")

plt.figure(figsize=(10,7))
sns.scatterplot(x="Age", y="BMI", hue="Outcome", data= pima_df)
plt.title("Age Vs. BMI based on Outcome")
plt.xlabel("Age")
plt.ylabel("BMI")

plt.figure(figsize=(10,7))
sns.scatterplot(x="Age", y="DiabetesPedigreeFunction", hue="Outcome", data= pima_df)
plt.title("Age Vs. Diabetes Pedigree Function based on Outcome")
plt.xlabel("Age")
plt.ylabel("Diabetes Pedigree Function")

plt.figure(figsize=(20, 8))
heatmap = sns.heatmap(pima_df.corr(), vmin=-1, vmax=1, annot=True, cmap='BrBG')
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':18}, pad=12)

plt.figure(figsize=(20,15))
sns.pairplot(pima_df)

"""### Partitioning the data set"""

X = pima_df.drop('Outcome', axis=1)
y = pima_df['Outcome']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

print(X_train.columns)

X_train.shape, X_test.shape

"""## Building Machine Learning Models (Primary Metric = Accuracy)"""

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import xgboost as xgb

from sklearn.metrics import accuracy_score

rfc = RandomForestClassifier(n_estimators=1000)
XGB = xgb.XGBClassifier()
grad = GradientBoostingClassifier()

"""### Random Forest Classifier"""

rfc.fit(X_train, y_train)

preds_rfc = rfc.predict(X_test)

print("Accuracy of the Random Forest model: ", accuracy_score(y_test, preds_rfc))

"""### XGBoost Classifier"""

XGB.fit(X_train, y_train)

preds_XGB = XGB.predict(X_test)

print("Accuracy of the XGB model: ", accuracy_score(y_test, preds_XGB))

"""### GradientBoosting Classifier"""

grad.fit(X_train, y_train)

preds_grad = grad.predict(X_test)

print("Accuracy of the Gradient Classifier model: ", accuracy_score(y_test, preds_grad))

"""## Evaluating the trained models"""

from sklearn.metrics import classification_report, confusion_matrix

"""### Evaluating Random Forest Classifier"""

print("Random Forest Classifier's Evalution Report: ")
print('\n')
print(classification_report(y_test, preds_rfc))

print(confusion_matrix(y_test, preds_rfc))

"""### Evaluating XGBoost Classifier"""

print("XGBoost Classifier's Evalution Report: ")
print('\n')
print(classification_report(y_test, preds_XGB))

print(confusion_matrix(y_test, preds_XGB))

"""### Evaluating GradientBoost Classifier"""

print("GradientBoost Classifier's Evalution Report: ")
print('\n')
print(classification_report(y_test, preds_grad))

print(confusion_matrix(y_test, preds_grad))

"""## HyperTuning the trained models

### Hyper-Tuning the XGBoost Classifier Model
"""

from sklearn.model_selection import RandomizedSearchCV

XGB_params = {
          "learning_rate"    : [0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ] ,
          "max_depth"        : [ 3, 4, 5, 6, 8, 10, 12, 15],
          "min_child_weight" : [ 1, 3, 5, 7 ],
          "gamma"            : [ 0.0, 0.1, 0.2 , 0.3, 0.4 ],
          "colsample_bytree" : [ 0.3, 0.4, 0.5 , 0.7 ]
       }

random_search = RandomizedSearchCV(XGB , param_distributions= XGB_params , n_iter=5, scoring='accuracy', n_jobs=-1, cv=5, verbose=3)

random_search.fit(X, y)

print(random_search.best_estimator_)

print(random_search.best_params_)

"""#### Training a Hyper-Tuned XGBoost Classifier Model"""

xgb_Classifier = xgb.XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=0.5, gamma=0.1,
              learning_rate=0.1, max_delta_step=0, max_depth=12,
              min_child_weight=7, missing=None, n_estimators=100, n_jobs=1,
              nthread=None, objective='binary:logistic', random_state=0,
              reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
              silent=None, subsample=1, verbosity=1)

xgb_Classifier.fit(X_train, y_train)

preds_HypXGB = xgb_Classifier.predict(X_test)

print("Evaluating the hyper-tuned XGBoost Classifier Model: ")
print("\n")
print("Accuracy of the Hyper-Tuned XGBoost Classifier model is ", accuracy_score(y_test, preds_HypXGB))
print("\n")
print(classification_report(y_test, preds_HypXGB))
print("\n")
print(confusion_matrix(y_test, preds_HypXGB))

"""### Hyper-Tuning the Gradient Boost Classifier Model"""

GradientBooster_params = {"n_estimators" : [100,500,1000],
               "subsample" : [0.6,0.8,1.0],
               "max_depth" : [5,10,15,20,25,30],
               "learning_rate" : [0.1, 0.01, 0.02, 0.5]
               }

random_search_GradBoost = RandomizedSearchCV( grad , param_distributions= GradientBooster_params , n_iter=5, scoring='accuracy', n_jobs=-1, cv=5, verbose=3)

random_search_GradBoost.fit(X, y)

print(random_search_GradBoost.best_estimator_)

print(random_search_GradBoost.best_params_)

"""#### Training a Hyper-Tuned GradientBoost Classifier Model"""

grad_Classifier = GradientBoostingClassifier(ccp_alpha=0.0, criterion='friedman_mse', init=None,
                           learning_rate=0.01, loss='deviance', max_depth=10,
                           max_features=None, max_leaf_nodes=None,
                           min_impurity_decrease=0.0, min_impurity_split=None,
                           min_samples_leaf=1, min_samples_split=2,
                           min_weight_fraction_leaf=0.0, n_estimators=500,
                           n_iter_no_change=None, presort='deprecated',
                           random_state=None, subsample=0.6, tol=0.0001,
                           validation_fraction=0.1, verbose=0,
                           warm_start=False)

grad_Classifier.fit(X_train, y_train)

preds_HypGrad = grad_Classifier.predict(X_test)

print("Evaluating the hyper-tuned Gradient Classifier Model: ")
print("\n")
print("Accuracy of the Hyper-Tuned Gradient Classifier model is ", accuracy_score(y_test, preds_HypGrad))
print("\n")
print(classification_report(y_test, preds_HypGrad))
print("\n")
print(confusion_matrix(y_test, preds_HypGrad))

"""## Cross-Validating the Hyper-Tuned Models

### Cross Validating the XGBoost Classifier Model
"""

from sklearn.model_selection import cross_val_score

XGB_Score = cross_val_score(xgb_Classifier, X, y, cv= 5)

print("Cross Validation Report of the XGBoost Classifier Model: ")
print("\n")
print(XGB_Score)

print("Average Cross Validation Report of the XGBoost Classifier Model: ", XGB_Score.mean())

"""### Cross Validating the Gradient Boost Classifier Model|"""

GradBoost_Score = cross_val_score(grad_Classifier, X, y, cv=5)

print("Cross Validation Report of the GradientBoost Classifier Model: ")
print("\n")
print(GradBoost_Score)

print("Average Cross Validation Report of the GradientBoost Classifier Model: ", GradBoost_Score.mean())

"""## Saving the Best Model"""

from joblib import dump
MODEL_NAME = "Diabetes_Model1.pkl"
dump(grad_Classifier, MODEL_NAME)
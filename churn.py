from __future__ import print_function
from xgboost import  XGBClassifier
from xgboost import plot_tree
import matplotlib.pyplot as plt
from numpy import loadtxt
import sys
from io import StringIO
from numpy import array
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree

import os
import subprocess

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz

def get_data():
    df = pd.read_csv("dataset.csv")
    return df

df = get_data()

X = df.values[::, 0:19]
y = df.values[::, 20]

X_train, Y_train, x_test, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

clf = tree.DecisionTreeClassifier()
clf.fit(X_train, Y_train)
clf.predict(x_test, y_test)

import graphviz

dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
print(graph)

print(X_train)
print(x_test)
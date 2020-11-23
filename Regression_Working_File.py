import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")
print(data.head())

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
print(data.head())

#predict = "G3"

# X = np.array(data.drop([predict], 1)) #features
# y = np.array(data[predict]) #labels

# x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

# linear = linear_model.LinearRegression()

# limear.fit(x_train, y_train

# acc = linear.score(x_test, y_test) # accuracy

# print(acc)

# print('Coefficient: \n', linear.coef_) # each slope val
# print('Intercept: \n', linear.intercept_) #intercept

# predictions = linear.predict(x_test)

# for x in range(len(predictions));
#   print(predictions[x], x_test[x], y_test[x])
# Multinomial Naive Bayes
from sklearn.naive_bayes import MultinomialNB, GaussianNB
m1 = MultinomialNB()
m1.fit(x_train,y_train)
print('Training Score', m1.score(x_train,y_train))
print('Testing Score', m1.score(x_test,y_test))
ypred_m1 = m1.predict(x_test)
print(ypred_m1)

# Gaussian Naive Bayes
m2 = GaussianNB()
m2.fit(x_train, y_train)
print('Training Score', m2.score(x_train,y_train))
print('Testing Score', m2.score(x_test,y_test))
print('Training Score', m2.score(x_train,y_train))
print('Testing Score', m2.score(x_test,y_test))
ypred_m2 = m2.predict(x_test)
print(ypred_m2)

# Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
m3 = RandomForestClassifier()
m3.fit(x_train,y_train)
print('Training Score', m3.score(x_train,y_train))
print('Testing Score', m3.score(x_test,y_test))

# K-Neighbours Classifier
from sklearn.neighbors import KNeighborsClassifier
m4 = KNeighborsClassifier(n_neighbors = 1)
m4.fit(x_train,y_train)
print(m4.score(x_train,y_train))
print(m4.score(x_test,y_test))

# Decision Tree
from sklearn import tree
m5 = tree.DecisionTreeClassifier()
m5.fit(x_train, y_train)
print('Training_score', m5.score(x_train, y_train))
print('Testing_score', m5.score(x_test, y_test))

# Gradient Boosting Classifier
from sklearn.ensemble import GradientBoostingClassifier
m6 = GradientBoostingClassifier()
m6.fit(x_train, y_train)
print('Training_score', m6.score(x_train, y_train))
print('Testing_score', m6.score(x_test, y_test))
from sklearn.ensemble import VotingClassifier
vc = VotingClassifier(estimators=[('mnb', m1), ('gnb', m2), ('rf', m3), ('knn', m4), ('dt', m5), ('gb', m6)], voting='hard')
vc.fit(x_train, y_train)
final_pred = print('Testing score', vc.score(x_test, y_test))

predictions = vc.predict(x_test)
print(predictions[:100])


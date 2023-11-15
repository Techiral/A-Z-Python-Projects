from sklearn.metrics import confusion_matrix, classification_report
cm = confusion_matrix(y_test, predictions)
print(cm)
print(classification_report(y_test,predictions))
x = sm              # independent variable
y = df['is_rumor']  # target variable
print(type(x))
print(type(y))
print(sm[:4])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


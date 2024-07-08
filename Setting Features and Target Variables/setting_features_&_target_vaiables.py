X = df_new.drop(['Sales','Store','Date','Year'] , axis = 1)
y= df_new.Sales
X.shape
X.head()
X.info()
y.head()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3, random_state=0)
columns=X_train.columns

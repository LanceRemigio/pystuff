# Machine Learning w/ Python

## Intro to Scikit Learn

We do all our machine learning baesd on the scikit learn python library. 

````python
from sklearn.family import Model # any model
# for example
from sklearn.linear_model import LinearRegression
````


- Every algorithm is exposed via an estimator and it can be set when it is instantiated. 
- The estimator comes with suitable defaults values.


**For example:**
````py
model = LinearRegression(normalize = True)
print(model)
# > LinearRegression(copy_x = True, fit_intercept = True, normalize = True) # these are the defaults
````

- Once the model is created, fit the model on some data.
- Keep in mind, you should split your data into a training set and a test set.
- We can do this by using the `train_test_split()` method.
- We can train/fit our model on the training data by using the `model.fit()` method. 

````python
model.fit(X_train, y_train)
````

- Now we are ready to predict labels or values on the test set (keep in mind these are steps to supervised learning).
- We can get the predicted values using the predict method:
````python
predictions = model.predict(X_test)
````
- We can now evaluate the perfomance of our model by comparing our predictions to the correct values.
- We can do this on our choice of the following machine learning algorithms; that is, Regression, Classfication, Clustering, and so on.


> Note: In all estimators 
> - `model.fit()`: fits the training data.
> - For supervised learning applications, this accepts two arguments: the data X and the labels y (e.g model.fit(X,y))
> - For unsupervised learning applications, this accepts only a single argument, the data X (e.g model.fit(X)).
>

- Additionaly, **supervised estimators** come included with a method called `model.predict()` that predicts the label of a new set of data. 
- This method accepts one argument, the new data `X_new` 
- For example, `model.predict(X_new)` returns the learned label for each object in the array.

Available in **supervised estimators**
- `model.predict_proba()`: In classification problems, some estimators also provide this method, which returns the probabiility that a new observation has each categorical label. In this case, the label with the highest probability is returned by `model.predict()`.

## Linear Regression

- The main idea of **regression** is that most data points are closer to the mean (average).
- **Regression** is all about creating a line such that the line **minimizes** the distance of all the data points in the line. 
- This is done by using the **least squares method**.
- Minimizing the distances involves minimizing the **sum of the squares of the residuals**.
- The **residuals** for an observation is the difference between the observation (actual values) and the fitted line (predicted values).

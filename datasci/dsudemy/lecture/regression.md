# Evaluating Regression

## Intro
> Definition: A task when a model attempts to predcit continuous values 

- This is unlike categorical values which aims to classify categorical values.

- Evaluation metrics such as accuracy or recall are not suited to solve regression problems. 
- We need other metrics designed for **continuous** values not **discontinuous**.

## Use cases

- An example of a regression problem is the task of predicting the price of a house given its properties.
- Whereas in a classfication problem, we are only concerned with the categorization of a house based on its country.


## Common Evaluation Metrics for Regression




### Mean Absolute Error 
- Mean of the absolute value errors.
- $\frac{1}{n} \sum_{i=1}^{n} |y_{i} - \hat{y}_{i}|$
- $\hat{y}_{i}$ is the prediction value
- $y_{i}$ is the actual value
- This formula contains an absolute value because we want to take into account differences that are either over or under.
- A problem with this metric is that it does not take into account outlier values which largely affects distribution of data.
###  Mean Squared Error
- The formula
$$\frac{1}{n}\sum_{i=1}^{n}(y_{i} - \hat{y}_{i})^{2}$$
takes these variances into account by squaring the errors instead.
- The squaring of these errors, however, converts the units of the values into something that is sometimes difficult to work with.
### Root Mean Square Error
$$\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_{i} - \hat{y}_{i})^{2}}$$
- This is the root of the mean of the squared errors.
- This solves both the problem of outliers and unit conversions

## Evaluating Results
- Note that these performance metrics have to be considered under context.
- A way to determine whether results are 'good' is to compare them to the average value of the label in your data set.
- Domain knowledge plays a big role in this. 




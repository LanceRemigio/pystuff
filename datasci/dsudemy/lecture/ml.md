# Intro to Machine Learning

## Supervised Learning

- **Supervised learning** algorithms are trained using **labeled** examples, such as an input where the desired output is known.
- For example, a portion of text could have a category label, such as:
    - **Spam** vs. **Legitimate** Email
    - **Positive** vs. **Negative** Movie Review

- The network receives a set of inputs along with the corresponding correct outputs. The 'machine learning' occurs when the algorithm compares the actual output to the correct outputs to find errors.
- The learning is the modification of the model to get the correct output.

- Machine learning is typically used to predict future events based on historical data. 

## Machine Learning Process

1. Get data (by any means)
2. Clean data using Pandas
3. Split data into two sets (three sets in the real world). One for test data and the other for model training and building.
4. Model testing. If errors are found, the model is subsequently adjusted to create more accurate results.
5. Once satisfied, we can deploy the ml algorithm in the real world.

- This is a simplified approach to supervised learning.
- Since we only split our data into two sets, we can tecnically go back, test, and update our data repeatedly. 
- One question we can ask is whether or not our test data is an accurate predictor of performance for our algorithm?
- We can fix this issue by creating another split to further test our data to get a more accurate performance metric.


## Solution

- Data is often split into **3 sets**
    - Training Data
        - Used to train model parameteres
    - Validation Data
        - Used to determine what model hyperparameters to adjust. (Used to see performance of model on unseen data)
    - Test Data
        - Used to get some final performance metric (not allowed to go back to adjust parameters)
- Note that without this third set, repeadtedly testing the model won't gauge how accurate our model is since the data it is being tested on has been seen before.


## Plan

- We will only have two splits where we train and test our models. 
- We will have the option to have a third split after going through the course.


# Model Evaluation

After the machine learning process is complete, we will use performance metrics to evaluate the how well our model did.


## Classfication Metrics

- The key classification metrics are: 
    - Accuracy 
    - Recall 
    - Precision
    - F1-score

- In a classification task, the model can only achieve binary results:
    - Either the model was **correct** in its prediction or the model was **incorrect** in its prediction.

- These binary results generalizes to situations where one can have multiple classes.
- In this context, let's assume we have a **binary classification** situation,  where we only have two available classes.

- Suppose we created an algorithm that will predict if an image is a dog or cat.
- Note that this is a supervised learning situation where we split our data into two sets; that is, we split the data into **training** data and **testing**  (new images that the model has not seen before) data.
- Once the model's predictions are obtained from the **X_test** data, we will then compare them to the **true y values** (the correct labels).


- This is done for all the images of dogs and cats in the test data.
- In the end, we will have a count of correct matches and a count of incorrect matches.
- Note that it isn't this simple when developing models in the real world; that is, not all incorrect or correct matches hold equal value.
- Furthermore, a single metric of evaluation will give us full information on the algorithm.
- We could organize our predicted values compared to real values via a **confusion matrix**.

## Defining Each Metric

## When Accuracy Metric is Appropriate and Inappropriate
- Accuracy 
    - In classification problems, this is the **number of correct predictions** made by the model divided by the **total number of predictions**; that is, how many predictions did the model get right based on a percentage. 
    - Useful when target classes are well balanced; that is, there is equal amount of each classfication in the test data.
    - However, this is **not** useful when there are **unbalanced** classes. For this situation, we will want to use recall to evaluate our model.
    - Otherwise, we have a nice intution on the perfomance of our algorithm.

## A better solution if Classes are unbalanced
- Recall
    - Evaluates the ability of the model to find all the relevant cases within a dataset.
    - The precise definition of recall is the number of true positives **divided by** the number of true positives plus the number of false negatives: 
    $$\text{Recall}=\frac{tp}{tp - fn}$$
- Precision
    - Abilitiy of a classfication model to identify only relevant data points. 
    - Precision is defined as the # of true positives divided by the number of true positives plus the number of false positives: 
    $$\text{Precision}=\frac{tp}{tp + np}.$$

- Recall and Precision 
    - There is a trade off between these two metrics
    - Recall expresses the ability of a model to find all relevant instances in a dataset, while precision expresses the proportion of data points that was actually relevant.

- F1-Score (Recall and Precision combined)
    - The F1 Score is the harmonic mean of the precision and recall taking both metrics into account in the following equation:
    $$F_1 = 2 \cdot \frac{\text{precision} \cdot \text{recall}}{\text{precision} + \text{recall}}.$$
    - Why the harmonic mean instead of a simple average? Because simple averages contains outliers that are not taking into account if we are trying to best evaluate the performance of models whereas harmonic takes these outliers into account.
    - For example, having a precision of 1.0 and a recall of 0.0 has a simple average of 0.5 but an F1 score of 0.

- We can view all correctly classfied versus incorrectly classfied images in the form of a confusion matrix.

## Confusion Matrix

-  True Positives (when both the condition and prediction is positive) 
-   False Negatives (when the condition is positive but the prediction is negative) *this is called a type II error*
- False Positive (when the condition is negative but the prediction is positive) *this is called a type I error*
- True Negative (when both the condition and prediction is negative)

## What's the point of all these methods?

- The confusion matrix in addition to the various metrics are all fundamental ways of comparing the predicted values versus the true values; that is, different ways of assessing the performance of a given model.
- What makes a metric "good" will largely depend on the situation.

## When to use a specific metric

- When diagnosing different diseases, it is often the case that we will have an unbalanced amount of classes.
- In identifying diseases, it is advantageous to minimize false negatives and maximize false positives because we need to make sure we correctly identify as many cases of the disesases as possible. 
- Not all problems can be solved by a general model created with Machine Learning. Every problem is going to be different and so are the models the come with solving them.




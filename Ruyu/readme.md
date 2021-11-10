## Do algorithm (easy leetcode level):
##### Data structure: 
      array, subarray, hash table, tuple, string, list, linked list (so far)
##### Method: 
     binary search, dynamic programming
#### Python tools:
     NumPy: provides a high-performance multidimensional array object, and tools for working with these arrays. https://www.kausalvikash.in/python-numpy-interview-questions-and-answers-for-freshers/
     Pandas: Pandas provide two data structures: Series, and DataFrames. Memory Efficient; Data Alignment; Reshaping; Merge and join; Time Series. https://www.kaggle.com/getting-started/119445
     scikit-learn:

## SQL: 
    Sql cookbook pivot, window function, do not use subquery, group by, self join and do leetcode sql 
## overfitting: 
To avoid over-fitting in RF models, the main thing you need to do is optimize a tuning parameter that governs the number of features that are randomly chosen to grow each tree from the bootstrapped data, and get more data. n_estimators: more trees the less likely the algorithm is to overfit.
max_features: Try reducing this number. The smaller, the less likely to overfit, but too small will start to introduce under fitting.
max_depth: Reduction of the maximum depth helps fighting with overfitting.
min_samples_leaf: This has a similar effect to the max_depth parameter, it means the branch will stop splitting once the leaves have that number of samples each.

## how to detect outliers
## decrease dim: PCA,  Neural Network Embedding, 
## Logistic Regression
## Time Series Analysis
## Experimental Design:
Treatment definition (i.e. objective definition)
Metrics definition and selection
Set up experiment, including sample size, randomization
Conduct hypothesis
Interpret experiment result
## Generalized Linear Models:
link function, assumptions
## Mixed Modeling
## Multivariate Statistics
## Large-Scale Predictive Modeling
## how to evaluate
Regression problem: Mean Squared Error (MSE), Mean Absolute Error (MAE)
Classification problem: Accuracy, Precision, Recall, F1, AUC (how to prioritize precision and recall metrics in different use cases? How to explain AUC from a probability perspective?)
## k-means clustering algorithm
## CHAID/decision trees
## Gradient Boosted Trees
## Random Forests:
For classification tasks, the output of the random forest is the class selected by most trees. For regression tasks, the mean or average prediction of the individual trees is returned. 
## Neural Networks
## Recommender system:
K-nearest neighbor: 也就是collaborative filtering最简单的实现方法, 直接基于item-based or user-based方法找出用户可能喜欢的一组商品. 模型比较简单, 更新速度快.
Matrix Factorization: 综合item & user全部信息进行推荐, 精度较高. 但每次计算比较耗时, 不便于实时更新.
Neural Network: 可以整合更多user profile信息进入模型, 是比Matrix Factorization更加通用的方法, 计算精度更高. 但是模型更加复杂, 做实时预测时会有一些延时或者需要较多computation resource.




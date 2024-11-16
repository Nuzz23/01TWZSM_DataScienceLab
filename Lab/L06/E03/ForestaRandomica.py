"""A random forest is an ensemble approach: it trains multiple trees on different portions of the dataset. This lowers
the chance of overfitting on the dataset (the single tree might overfit its portion of data, but the
overall “forest” will likely not). Each tree of the random forest is trained on N points extracted, with
replacement, from the entire dataset (comprised of N points). Note that, since the extraction of
the points is done with replacement, selecting N points does not necessarily extract all points of the
dataset. Indeed, only approximately 63.2% of all points will be extracted for each tree1.

Each tree, additionally, bases each split decision using a subset of all features. The size of this subset,
B, is often selected to be the square root of the total number of features available, but different
random forest may adopt different values. This parameter can be defined for each decision tree
through the max_features parameter. When building a tree, a random sample of max_features
features will be extracted and used to select the split.
Another important parameter for random forests is the number of trees used. We will call this
parameter n_estimators. During training, each of these trees (or estimators) is trained with its
subset of data. During the prediction of a new list of points, each tree of the random forest will make
its prediction. Then, through majority voting, the overall label assignment is made. Majority voting
is just a fancy way of saying that the class selected by the highest number of trees is selected."""

from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

from collections import Counter



class ForestaRandomica:
    def __init__(self, nEstimators:int, maxFeatures:str='sqrt'):
        """this function initializes the random forest

        Args:
            nEstimators (int): the number of trees of the forest
            maxFeatures (str, optional): The number of features per each tree. Defaults to 'sqrt'.

        Raises:
            ValueError: if the number of estimators is less than 2 
        """
        if not nEstimators or nEstimators <= 1:
            raise ValueError("Expected number of estimators to be an integer larger than 1")
    
        self.__forest = [DecisionTreeClassifier(max_features=maxFeatures) for _ in range(nEstimators)]
    
        
    def fit(self, X:pd.DataFrame, y:pd.DataFrame, percentageRowsPerTree:float=0.70) ->None:
        """fits the random forest

        Args:
            X (pd.DataFrame): the feature dataFrame
            y (pd.DataFrame): the class series
            percentageRowsPerTree (float, optional): the percentage of rows to be considered in training per each tree. Defaults to 0.70.

        Raises:
            ValueError: if the percentage is not a valid percentage so if x not in [0, 1]
        """
        if not 0 <= percentageRowsPerTree <= 1.0:
            raise ValueError("the percentage of value should be between 0 and 1")
        
        for i in range(len(self.__forest)):
            index = list(set(np.random.randint(low=0, high=X.shape[0], size=int(X.shape[0]*percentageRowsPerTree))))
            self.__forest[i].fit(X.iloc[index, :], y.iloc[index])
            
        return self
    
    
    def predict(self, X: pd.DataFrame)->str:
        """predicts the class for a dataFrame

        Args:
            X (pd.DataFrame): the dataFrame to be predicted

        Returns:
            prediction (pd.Series): the predicted class per each row
        """
        pred = pd.DataFrame([tree.predict(X) for tree in self.__forest])
        return pd.Series(Counter(pred.iloc[:,i]).most_common(n=1)[0][0] for i in range(X.shape[0]))
    
    
    def getTreeNumber(self)->int:
        """returns the number of tree fo the forest

        Returns:
            #Trees (int): number of tree of the forest
        """
        return len(self.__forest)
        
        
    def getFeatureImportance(self, sort:bool=False)->pd.DataFrame:
        """returns the importance of each feature
        
        Args:
            sort (bool): if the dataFrame should be return sorted. Defaults to False

        Returns:
            importance (pd.DataFrame): dataFrame of features
        """
        val = self.__forest[0].feature_importances_
        
        for i in range(1,self.getTreeNumber()):
            val = val + self.__forest[i].feature_importances_
        
        if not sort:
            return pd.DataFrame(val, columns=['importance'], index=list(range(val.shape[0])))
        
        return pd.DataFrame(val, columns=['importance'], index=list(range(val.shape[0]))).sort_values(by='importance', ascending=False)
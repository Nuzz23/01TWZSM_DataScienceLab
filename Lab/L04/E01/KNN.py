import numpy as np
from math import cos


class KNearestNeighbors:
    def __init__(self, k:int)->None:
        """_summary_
        Args:
            k (int): the number of neighbor to be evaluated
            
        Raises:
            ValueError: if k is lower than 1
        """       
        
        if k < 1:
            raise ValueError("K should be at least equal to 1")
        self.__k=k
    
    
    # GETTERS
    
    
    def getNeighborsValue(self)->int:
        """_summary_

        Returns:
            int: returns the k value
        """
        return self.__k
    
    
    # SETTERS
    
    
    def setNeighborsValue(self, k:int)->int:
        """_summary_

        Args:
            k (int): new neighbors value

        Raises:
            ValueError: if k is lower than 1
        """
        if k < 1:
            raise ValueError("K should be at least equal to 1")
        self.__k=k
        
    
    # FIT METHOD        
    
    
    def fit(self, data:np.dtypes.Float16DType, label:np.dtypes.StringDType)->int:
        """_summary_

        Args:
            data (np.dtypes.Float16DType): train data
            label (np.dtypes.StringDType): train labels

        Returns:
            int: the length of the given data
        """
        self.__data = data
        self.__label = label
        
        return data.shape[0]
    
    
    # PREDICT METHOD

        
    def predict(self, data: np.dtypes.Float16DType, distanceMethod:function=None)->np.dtypes.StringDType:
        """_summary_

        Tries to predict the classification of a given set of data

        Args:
            data (np.dtypes.Float16DType): The data you want to predict
            distanceMethod (function, optional): The function to be used to compute the distance. Defaults to Euclidean distance.

        Returns:
            predicted distances (np.dtypes.StringDType): returns the predicted labels as an numpy array
        """
        
        if not distanceMethod or not isinstance(distanceMethod, function):
            distanceMethod = self.euclidean
            
            
            
        return np.dtypes.StringDType
    
    # DISTANCE METHOD
    
    
    def euclidean(self, v1:np.dtypes.Float16DType, v2:np.dtypes.Float16DType)->float:
        """_summary_
        
        Computes the euclidean distance between two vectors

        Args:
            v1 (np.dtypes.Float16DType): vector v1
            v2 (np.dtypes.Float16DType): vector v2

        Returns:
            distance (float): the euclidean distance between vector v1 and vector v2
        """
        return sum([(v1[i]-v2[i])**2 for i in range(len(v1.shape[0]))])**0.5
        
    
    def cosine(self, v1:np.dtypes.Float16DType, v2:np.dtypes.Float16DType)->float:
        """_summary_
        
        Computes the cosine distance between two vectors

        Args:
            v1 (np.dtypes.Float16DType): vector v1
            v2 (np.dtypes.Float16DType): vector v2

        Returns:
            distance (float): the cosine distance between vector v1 and vector v2
        """
        
        piqi = 0
        pi = 0
        qi = 0
        for i in range(v1.shape[0]):
            piqi += v1[i]*v2[i]
            pi += v1[i]**2
            qi += v2[i]**2

        return  1 - abs(cos(piqi/((pi*qi)**0.5)))
    
    
    
    def manhattan(self, v1:np.dtypes.Float16DType, v2:np.dtypes.Float16DType)->float:
        """_summary_
        
        Computes the manhattan distance between two vectors

        Args:
            v1 (np.dtypes.Float16DType): vector v1
            v2 (np.dtypes.Float16DType): vector v2

        Returns:
            distance (float): the manhattan distance between vector v1 and vector v2
        """
        return sum(abs(v1[i]-v2[i]) for i in range(v1.shape[0]))    
    
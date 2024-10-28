import numpy as np


class KNearestNeighbors:
    def __init__(self, k:int, distance_metric:str="euclidean")->None:
        """_summary_
        Args:
            k (int): the number of neighbor to be evaluated
            distance_metric (str): the distance metric to be used
            
        Raises:
            ValueError: if k is lower than 1
        """       
        
        if k < 1:
            raise ValueError("K should be at least equal to 1")
        self.__k=k
        self.__distanceMetric = distance_metric
    
    
    # GETTERS
    
    
    def getNeighborsValue(self)->int:
        """_summary_

        Returns:
            int: returns the k value
        """
        return self.__k
    
    def getDistanceMetric(self)->str:
        """_summary_

        Returns:
            str: returns the current metric
        """
        return self.__distanceMetric
    
    
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
        
    
    def setDistanceMetric(self, newMetric:str="euclidean")->None:
        """_summary_

        Args:
            newMetric (str, optional): The given metric. Defaults to "euclidean".
        """
        
        if newMetric:
            self.__distanceMetric = newMetric
    
    
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
    
    
    
    
    
    
    
    
    # DISTANCE METHOD
    
    
    def euclidean():
        pass
    
    def cosine():
        pass
    
    def manhattan():
        pass
    
    
import numpy as np
from collections import Counter

class KNearestNeighbors:
    def __init__(self, k:int, weightScheme:list[float]=None)->None:
        """_summary_
        Args:
            k (int): the number of neighbor to be evaluated
            weightScheme (list(float) | np.array[float]): weight scheme to be used 
            to weight each feature. Defaults to an equally distributed weight for 
            each feature if none is given
            
        Raises:
            ValueError: if k is lower than 1
        """       
        
        if k < 1:
            raise ValueError("K should be at least equal to 1")
        self.__k=k
        
        if weightScheme:
            self.__weightSchema = np.array(weightScheme, dtype=np.dtypes.Float16DType) if isinstance(weightScheme, list) else weightScheme
        else:
            self.__weightSchema = None
            
    
    # GETTERS -----------------------------------------------------------
    
    
    def getWeightSchema(self)->np.dtypes.Float16DType:
        """
            Returns the current weight schema for knn
            if none was specified, the returned weighting schema is the 
            equally weighted one between each feature

        Returns:
            weightSchema (np.dtypes.Float16DType): returns the used weight schema
        """
        return self.__weightSchema
    
    
    def getNeighborsValue(self)->int:
        """_summary_

        Returns:
            int: returns the k value
        """
        return self.__k
    
    
    # SETTERS -----------------------------------------------------------
    
    
    def setWeightSchema(self, weights:np.dtypes.Float16DType)->None:
        """_summary_

            sets the weight schema to the given one, if a list is given its converted into a np.array

        Args:
            weights (np.dtypes.Float16DType | list[float]): given weighting schema
        """
        self.__weightSchema = np.array(weights, dtype=np.dtypes.Float16DType) if isinstance(weights, list) else weights    

    
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
        
    
    # FIT METHOD -----------------------------------------------------------    
    
    
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
    
    
    # PREDICT METHOD -----------------------------------------------------------

        
    def predict(self, data:np.dtypes.Float16DType, distanceMethod=None)->np.dtypes.StringDType:
        """

        Tries to predict the classification of a given set of data.
        if the used weight schema doesn't have enough feature to be supported
        it defaults to the equal weight weighting schema

        Args:
            data (np.dtypes.Float16DType): The data you want to predict
            distanceMethod (function, optional): The function to be used to compute the distance. Defaults to Euclidean distance.

        Returns:
            predicted distances (np.dtypes.StringDType): returns the predicted labels as an numpy array
        """
       
        try:
            if not distanceMethod or (str(KNearestNeighbors.euclidean).split()[1].split(".")[-1] not in
            {method for method in dir(KNearestNeighbors) if callable(getattr(KNearestNeighbors, method)) and not method.startswith("__")}):
                distanceMethod = self.euclidean
        except Exception:
            distanceMethod = self.euclidean


        if not self.__weightSchema or self.__weightSchema.shape[0] != data.shape[1]:
            self.__weightSchema = self.__createDefaultSchema(data.shape[1])


        # Only god knows what it does
        # creates a list with distance*weight, label for a single data
        # sorts it in ascending order and selects only the first k elements
        # maps the element into a list of class
        # Counts the occurrences of each class 
        # gets the most common, and selects only the label
        # repeats for each data given
        # builds an np 1D array
        return np.array(
            [Counter(list
                (map(lambda y:y[1], 
                    sorted(
                        [[distanceMethod(test, self.__data[i], self.__weightSchema), self.__label[i]] 
                        for i in range(len(self.__data))], key=lambda x:x[0])[:self.__k]
                    )))
            .most_common(1)[0][0] 
            for test in data], dtype=np.dtypes.StringDType)
    
    
    def predictWithDistance(self, data:np.dtypes.Float16DType, distanceMethod=None)->np.dtypes.StringDType:
        """
        Tries to predict the classification of a given set of data using the distance.
        if the used weight schema doesn't have enough feature to be supported
        it defaults to the equal weight weighting schema

        Args:
            data (np.dtypes.Float16DType): The data you want to predict
            distanceMethod (function, optional): The function to be used to compute the distance. Defaults to Euclidean distance.

        Returns:
            predicted distances (np.dtypes.StringDType): returns the predicted labels as an numpy array
        """
       
        try:
            if not distanceMethod or (str(KNearestNeighbors.euclidean).split()[1].split(".")[-1] not in
            {method for method in dir(KNearestNeighbors) if callable(getattr(KNearestNeighbors, method)) and not method.startswith("__")}):
                distanceMethod = self.euclidean
        except Exception:
            distanceMethod = self.euclidean


        # Only god knows what it does
        # creates a list with distance*weight, label for a single data
        # sorts it in ascending order and selects only the first k elements
        # maps the element into a list of class
        # Counts the occurrences of each class 
        # gets the most common, and selects only the label
        # repeats for each data given
        # builds an np 1D array
        return np.array(
            [Counter(list
                (map(lambda y:y[1], 
                    sorted(
                        [[1/distanceMethod(test, self.__data[i], self.__createDefaultSchema(data.shape[1])), self.__label[i]] 
                        for i in range(len(self.__data))], key=lambda x:x[0])[:self.__k], reversed=True
                    )))
            .most_common(1)[0][0] for test in data], dtype=np.dtypes.StringDType)
    
    
    # DISTANCE METHOD -----------------------------------------------------------
    
    
    def euclidean(self, v1:np.dtypes.Float16DType, v2:np.dtypes.Float16DType, weight:np.dtypes.Float16DType)->float:
        """
        
        Computes the euclidean distance between two vectors

        Args:
            v1 (np.dtypes.Float16DType): vector v1
            v2 (np.dtypes.Float16DType): vector v2

        Returns:
            distance (float): the euclidean distance between vector v1 and vector v2
        """
        return sum([weight[i]*((v1[i]-v2[i])**2) for i in range(v1.shape[0])])**0.5
    
    
    def cosine(self, v1:np.dtypes.Float16DType, v2:np.dtypes.Float16DType, weight:np.dtypes.Float16DType)->float:
        """
        
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
            piqi += v1[i]*v2[i]*weight[i]
            pi += (v1[i]**2)*weight[i]
            qi += (v2[i]**2)*weight[i]

        return  1 - abs(piqi/((pi*qi)**0.5))
    
    
    def manhattan(self, v1:np.dtypes.Float16DType, v2:np.dtypes.Float16DType, weight:np.dtypes.Float16DType)->float:
        """    
        Computes the manhattan distance between two vectors

        Args:
            v1 (np.dtypes.Float16DType): vector v1
            v2 (np.dtypes.Float16DType): vector v2

        Returns:
            distance (float): the manhattan distance between vector v1 and vector v2
        """
        return sum(weight[i]*abs(v1[i]-v2[i]) for i in range(v1.shape[0]))    
    
    
    ## Weight Schema --------------------------------------------------------
    
    
    def __createDefaultSchema(self, dim:int)->np.dtypes.Float16DType:
        """_summary_

        Args:
            dim (int): length of the schema to be created

        Returns:
            weight schema (np.dtypes.Float16DType): return the default weight schema
        """
        return np.ones(dim, dtype=np.dtypes.Float16DType)
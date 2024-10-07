class irisEnum:
    # Constructor of the class
    def __init__(self) -> None:
        self.SEPAL_LENGTH = 0
        self.SEPAL_WIDTH = 1
        self.PETAL_LENGTH = 2
        self.PETAL_WIDTH = 3
        self.SPECIES = 4
        self.values_list = [0,1,2,3]
            
    
    # Converts an int to a string as associated in the enumerator
    def value2string(self, val: int) -> str:
        # Checks the type and value
        if not isinstance(val, int) or not self.SEPAL_LENGTH <= val <=self.PETAL_WIDTH:
            raise TypeError("Input number not correct")
        
        # Returns the field as string
        if val == self.SEPAL_LENGTH:
            return "Sepal length"
        elif val == self.SEPAL_WIDTH:
            return "Sepal width"
        elif val == self.PETAL_LENGTH:
            return "Petal length"
        else:
            return "Petal width"
        
    # Returns the list of all possible values 
    def allValues(self)->list:
        return self.values_list

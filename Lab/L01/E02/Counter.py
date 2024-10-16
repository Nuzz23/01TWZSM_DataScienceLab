class Counter:
    def __init__(self) -> None:
        self.__count = 0
        
    def addValue(self, val:int)->int:
        self.__count+=val
        return self.totValue()
    
    def totValue(self)->int:
        return self.__count
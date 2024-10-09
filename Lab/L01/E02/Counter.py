class Counter:
    def __init__(self) -> None:
        self.__count = 0
        
    def addValue(self, val:int)->int:
        self.count+=val
        return self.__count
    
    def totValue(self)->int:
        return self.__count
class EnumData():
    def __init__(self):
        self.DATE = 0
        self.AVG_TEMP = 1
        self.AVG_DELTA = 2
        self.CITY = 3
        self.COUNTRY = 4
        self.LATITUDE = 5
        self.LONGITUDE = 6
        
    def returnValuesAsSet(self):
        return {0,1,2,3,4,5,6}
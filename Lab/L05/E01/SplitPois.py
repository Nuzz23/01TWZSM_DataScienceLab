import pandas as pd
import numpy as np

class SplitPois():
    def __init__(self, df:pd.DataFrame, size:int)->None:
        self.size = size
        self.long_max, self.long_min, = df['@lon'].max(), df['@lon'].min()  
        self.lat_max, self.lat_min = df['@lat'].max(), df['@lat'].min() 
    
    def plotGrid(self, ax):
        lat_steps = np.linspace(self.lat_min, self.lat_max, self.size + 1)
        long_steps = np.linspace(self.long_min, self.long_max, self.size + 1)
        
        ax.hlines(lat_steps, self.long_min, self.long_max)
        ax.vlines(long_steps, self.lat_min, self.lat_max)
        
    
    def point_to_cell_coord(self, long, lat):
        x = int((long - self.long_min)/(self.long_max - self.long_min)*self.size)
        y = int((lat - self.lat_min)/(self.lat_max - self.lat_min)*self.size)
        return x, y
    
    def point_to_cell_id(self, long, lat):
        x, y = self.point_to_cell_coord(long, lat)
        return y * self.size + x
    
        
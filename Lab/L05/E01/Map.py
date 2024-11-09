import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.cm import get_cmap

class Map:
    def __init__(self, df:pd.DataFrame):
        """ Store Dataset with POIs information."""
        self.pois_df = df
        self.lat_min = df['@lat'].min()
        self.lat_max = df['@lat'].max()
        self.long_min = df['@lon'].min()
        self.long_max = df['@lon'].max()
        
        
    def plot_map(self, path:str):
        """ Display an image with NY map and return the Axes object."""
        fig, ax = plt.subplots()
        nyc_img = plt.imread(path)
        ax.imshow(nyc_img, zorder=0, extent=[self.long_min,
                                            self.long_max,
                                            self.lat_min,
                                            self.lat_max])
        ax.grid(False)
        return ax
        
    def plot_pois(self, ax, category):
        """Plot data on specified Axis."""
        
        # Version 1: using pandas
        types = self.pois_df[category].unique()
        cmap = get_cmap('viridis')
        colors = cmap(np.linspace(0, 1, types.size))
        for i, t in enumerate(types):
            df_t = self.pois_df.loc[self.pois_df[category] == t]
            c = [colors[i]] *  df_t.shape[0]
            df_t.plot.scatter(x='@lon', y='@lat', ax=ax, c=c, alpha=.6, label=t)
        
        # Version 2: using seaborn
        # sns.scatterplot(df['@lon'], df['@lat'], hue=df[category], ax=ax, 
        #                 marker='o', s=3, linewidth=0, palette="viridis", legend='full')

        ax.legend() # show the legend, required by Version 1
        ax.grid(False)
        return ax
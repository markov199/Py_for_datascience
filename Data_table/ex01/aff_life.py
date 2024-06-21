import pandas as pd
import numpy as np
from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, MultipleLocator

def main():
    campus = "United Arab Emirates"
    df = load("../life_expectancy_years.csv")
    plot_data = ft_plot(df, campus)

def ft_plot(data, campus:str):
    dfc = (data[data['country'] == campus]).set_index('country')
    x_axis = np.asarray(dfc.columns)
    y_axis = np.asarray(dfc).flatten()
    title = campus + " Life Expectancy Projections"
   
    
    plt.plot(x_axis, y_axis)
    plt.xticks(x_axis[::40])
    plt.xlabel("year")
    plt.ylabel("Life expectancy")
    plt.title(title)
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.show()
    # return dfc
    
if __name__ == "__main__":
    main()

"""ref
https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
https://matplotlib.org/stable/gallery/ticks/ticks_too_many.html
"""
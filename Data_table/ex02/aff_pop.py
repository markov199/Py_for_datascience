import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from load_csv import load


def main():
    try:
        campus = ["United Arab Emirates", "France"]
        # campus = "France"
        df = load("../population_total.csv")
        plot_data = ft_plot(df, campus)
    
    except Exception as e:
        print(f"{type(e).__name__} :  {e}")


def ft_plot(data, campus):
    print(campus[0])
    dfc = (data[(data['country'] == campus[0])]).set_index('country')
    print(dfc.T)
    # data_country2 = (data[data['country'] == campus[1]]).set_index('country')
    # x_axis = np.asarray(dfc.columns)
    # y_data1 = np.asarray(dfc).flatten()
    # y_data2 = np.asarray(data_country2).flatten()
    # title = " Population Projections"
   
    
    # plt.plot(x_axis, y_data1, label=campus[0])
    # plt.plot(x_axis, y_data2, 'g', label=campus[1])
    
    # plt.xticks(x_axis[::40])
    # plt.xlabel("year")
    # plt.ylabel("Population")
    # plt.title(title)

    # plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.show()

if __name__ == "__main__":
    main()
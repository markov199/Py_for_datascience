from load_csv import load
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter, MaxNLocator

def main():
    df_income = load("..\income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_life_expectancy = load("..\life_expectancy_years.csv")
    df_income = df_income.set_index('country')
    df_life_expectancy = df_life_expectancy.set_index('country')
    df = pd.DataFrame()
    df['income'] = (df_income['1900'])
    df['life expectancy'] = df_life_expectancy['1900']
    x = df['income']
    y = df['life expectancy']
    plt.xlabel('Gross Domestic Product')
    plt.ylabel('Life Expectancy')
    formator = EngFormatter()
    plt.gca().set_xscale('log')
    plt.gca().xaxis.set_major_formatter(formator)
    plt.scatter(x,y)
    plt.show()
    


if __name__ == "__main__":
    main()
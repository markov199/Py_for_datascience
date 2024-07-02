def load(path: str):
    import pandas as pd

    df = pd.read_csv(path)
    print (f"Loading dataset of dimensions {df.shape}")
    return df
   

"""ref
creating dataframes:
https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/
 """
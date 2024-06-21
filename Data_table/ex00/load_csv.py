def load(path: str):
    import pandas as pd

    df = pd.read_csv(path)
    print (f"Loading dataset of dimensions {df.shape}")
    return df
   
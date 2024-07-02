def load(path: str):
    import pandas as pd

    df = pd.read_csv(path)
    print (f"Loading dataset of dimensions {df.shape}")
    return df
   

"""ref
using Engineering formater :
https://matplotlib.org/3.2.2/api/_as_gen/matplotlib.axis.XAxis.set_major_formatter.html
https://matplotlib.org/stable/gallery/text_labels_and_annotations/engineering_formatter.html
 using regex: 
 https://www.geeksforgeeks.org/python-regex-cheat-sheet/
 https://www.dataquest.io/blog/regular-expressions-data-scientists/
 https://www.dataquest.io/blog/regex-cheatsheet/
 https://stackoverflow.com/questions/39684548/convert-the-string-2-90k-to-2900-or-5-2m-to-5200000-in-pandas-dataframe
 """
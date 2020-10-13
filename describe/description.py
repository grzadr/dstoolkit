#!/env/bin/python3

from typing import List
Vector = List[float]

import pandas as pd
from pandas import DataFrame as dt

def describe_data(dataframe: dt, describe:bool=True, counts:bool=True, percentiles:Vector = [0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99]):
    
    print("Basic information:")
    print(dataframe.info())
    print()
    
    if counts:
        print("Value Counts:")
        for column in dataframe.select_dtypes(include='object').columns:
            print(dataframe[column].value_counts())
        print()
        
    if describe:
        print("Description:")
        print(dataframe.describe(percentiles=percentiles))
        print() 

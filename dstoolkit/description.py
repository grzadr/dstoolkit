#!/env/bin/python3

from collections import defaultdict 
from typing import List
Vector = List[float]

import pandas as pd
from pandas import DataFrame as df

def split_columns_by_type(dataframe: df):
    result = defaultdict(list)
    for name, dtype in dataframe.dtypes.iteritems():
        result[dtype.name].append(name)
    
    return result

def count_na(dataframe: df):
    return dataframe.isna().sum()

def describe_data(dataframe: df,
                  describe:bool=True,
                  counts:bool=True,
                  head:bool=True,
                  missing=True,
                  memory=False,
                  percentiles:Vector = [0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99]):
    
    print("Shape:", dataframe.shape)
    print(f"Names: {'|'.join(dataframe.columns)}")
    columns_dtypes = split_columns_by_type(dataframe)
    max_width = max([len(key) for key in columns_dtypes.keys()]) + 1
    print("Types:")
    for dtype, names in columns_dtypes.items():
        print(f"    {dtype:>{max_width}} - {len(names)}")
    print("Information:")
    print(dataframe.info())
    print()
    
    if missing:
        print("Missing:")
        print(count_na(dataframe))
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

    if memory:
        print("Memory:")
        print(dataframe.memory_usage())
        print()

    if head:
        print(dataframe.head())
        print()



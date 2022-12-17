import pandas as pd
import numpy as np 
    
def feature1(df):
    df['happy'] = df['valence'].apply(lambda x: 1 if x>=0.5 else 0)
    return df

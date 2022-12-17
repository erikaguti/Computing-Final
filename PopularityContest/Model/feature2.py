import pandas as pd
import numpy as np 

def genre(df):
    df['HipHop']=df['tempo'].apply(lambda x: 1 if (x>=85) & (x<=95) else 0)
    df['Reggaeton']=df['tempo'].apply(lambda x: 1 if (x>=90) & (x<=100) else 0)
    df['Pop']=df['tempo'].apply(lambda x: 1 if (x>=100) & (x<=140) else 0)
    df['House/Electro/Techno']=df['tempo'].apply(lambda x: 1 if x>=120 else 0)
    return df

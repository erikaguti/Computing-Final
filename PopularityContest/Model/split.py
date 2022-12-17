import pandas as pd
from sklearn.model_selection import train_test_split

def tt_split(df, target:str):
    X= df.drop(columns = [target], axis = 1)
    y= df[target]      
    return train_test_split(X, y,test_size=0.33, random_state=1)
        
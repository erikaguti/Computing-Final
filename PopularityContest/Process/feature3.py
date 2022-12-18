import pandas as pd 
import numpy as np 

def time(df, time:str):
    if time == "seconds":
        df['duration_s'] = df['duration_ms'] / 1000
        del df['duration_ms']
            
    elif time == "minutes":
        df['duration_m'] = df['duration_ms'] / 60000
        del df['duration_ms']
            
    else:
        print("Please enter a valid time unit")
            
    return df
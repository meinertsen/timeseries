import numpy as np
import pandas as pd

def AR(p,n,seed=None):
    np.random.seed(seed)
    errors= np.random.random(n)
    phis = np.random.random(p)
    ts = [0 for i in range(p)]  
    for period in range(n):
        ts.append(errors[period]+sum([phi*ts[-i-1] for i,phi in enumerate(phis)]))
    return pd.Series(ts[p:],index = range(n))
"""    
    Generate an AR(3) process with 20 observations
    In []: AR(3, 20, 12345)
    Out[]: 
    0       0.929616
    1       0.913631
    2       1.437861
    3       2.218526
    4       3.451884
    5       5.077327
    6       7.740519
    7      10.883113
    8      15.668655
    9      22.147882
    10     31.307649
    11     44.292424
    12     61.283291
    13     85.896632
    14    120.164184
    15    168.141791
    16    235.214173
    17    328.814068
    18    459.597769
    19    641.898670
    dtype: float64
    
"""

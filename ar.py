import numpy as np
import pandas as pd

def AR(p,n):
    errors= np.random.random(n)
    phis = np.random.random(p)
    ts = [0 for i in range(p)]  
    for period in range(n):
        ts.append(errors[period]+sum([phi*ts[-i-1] for i,phi in enumerate(phis)]))
    return pd.Series(ts[p:],index = range(n))
    
AR(3, 20) # Generate an AR(3) with 20 observations

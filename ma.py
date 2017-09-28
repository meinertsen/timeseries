def MA(theta,n,seed=None):
    np.random.seed(seed)
    errors= np.random.random(n)    
    ts=[]
    for i in range(1,n):
        ts.append(errors[i]+theta*errors[i-1])
    return pd.Series(ts[1:],index=range(1,n-1))
MA(0.5 , 10)
"""
Out[768]: 
1    1.120388
2    0.619690
3    1.057745
4    0.835835
5    0.446865
6    0.237199
7    0.931316
8    1.080488
dtype: float64
"""

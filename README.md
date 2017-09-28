# Timeseries generators
A companion piece to statmodels with generalized process generators that returns the timeseries in  a Pandas Series

- **AR**(p,n,seed): Generate an autoregressive process with n periods and optional seed for reproducibility
  - errors are drawn from a Gaussian distribusion 
  - phi's are drawn from a Gaussian distribusion (will make this more flexible in next version)

- **MA**(theta, n, seed): Generate a moving average process with n periods and optional seed for reproducibility
  - errors are drawn from a Gaussian distribusion 
  - phi's are drawn from a Gaussian distribusion (will make this more flexible in next version)

- ARMA

- ARIMA

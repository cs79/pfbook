# Black-Scholes-Merton setup for MC modeling of European call option

# imports
import numpy as np

# initial parameters
S0 = 100.       # initial stock index level
K = 105.        # strike price
T = 1.0         # time to maturity
r = 0.05        # risk-free short term rate
sigma = 0.2     # constant volatility

I = 100000      # number of simulations

# valuation algorithm
z = np.random.standard_normal(I)    # pseudorandom numbers
ST = S0 * exp((r - 0.5 * sigma ** 2) * T + sigma * sqrt(T) * z) # index values at maturity
hT = maximum(ST - K, 0)     # inner values at maturity
C0 = exp(-r * T) * sum(hT) / I  # Monte Carlo estimator

# result output
print("Value of the European call option is %5.3f" % C0)

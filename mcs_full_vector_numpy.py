#
# MC valuation of European call options with NumPy (log version)
# mcs_full_vector_numpy.py
#

from numpy import *
from time import time
from __future__ import division

random.seed(20000)
t0 = time()

# Parameters
S0 = 100
K = 105
T = 1
r = 0.05
sigma = 0.2
M = 50
dt = T / M
I = 250000

# Simulating I paths with M time steps
S = S0 * exp(cumsum((r - 0.5 * sigma ** 2) * dt + sigma * math.sqrt(dt) \
    * random.standard_normal((M + 1, I)), axis = 0))

S[0] = S0

# Calculating the Monte Carlo estimator
C0 = math.exp(-r * T) * sum(maximum(S[-1] - K, 0)) / I

# Results output
tnp2 = time() - t0
print "European Option value %7.3f" %C0
print "Duration in Seconds   %7.3f" %tnp2

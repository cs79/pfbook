# BSM model with vega function and implied vol estimation

# analytical Black-Scholes-Merton formula


def bsm_call_value(S0, K, T, r, sigma):
    ''' Valuation of European-style call option in BSM model.
    Analytical Formula.

    Parameters
    ==========
    S0 : float
        initial stock/index level
    K : float
        strike price
    T : float
        maturity date (in year fractions)
    r : float
        constant risk-free short relative
    sigma : float
        volatility factor in diffusion term

    Returns
    =======
    value : float
        present value of the European-style call option
    '''
    from math import log, sqrt, exp
    from scipy import statistics

    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = (log(S0 / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    value = (S0 * stats.norm.cdf(d1, 0.0, 1.0) - K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))
    return value

# Vega function


def bsm_vega(S0, K, T, r, sigma):
    # add docstring later
    from math import log, sqrt
    from scipy import stats

    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    vega = S0 * stats.norm.cdf(d1, 0.0, 1.0) * sqrt(T)
    return vega

# Implied vol function


def bsm_call_imp_vol(S0, K, T, r, C0, sigma_est, it=100):
    # add docstring later
    for i in range(it):
        sigma_est -= ((bsm_call_value(S0, K, T, r, sigma_est) - C0) / bsm_vega(S0, K, T, r, sigma_est))
    return sigma_est

#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

def simulate_gbm_paths(S0, mu, sigma, T, n_steps, n_paths, seed=None):
    '''

    Simulates stock price paths using Geometric Brownian Motion (GBM).

    Parameters:
        S0 (float): Initial stock price
        mu (float): Drift (expected return or risk-free rate)
        sigma (float): Volatility of the stock
        T (float): Time to maturity in years
        n_steps (int): Number of time steps
        n_paths (int): Number of simulated paths
        seed (int, optional): Random seed for reproducibility

    Returns:
        tuple: times (1D array), paths (2D array of shape (n_paths, n_steps + 1))
    '''
    if seed is not None:
        np.random.seed(seed)

    dt = T / n_steps #time increment per step
    times = np.linspace(0, T, n_steps + 1) 

    paths = np.zeros((n_paths, n_steps + 1))
    paths[:, 0] = S0

    Z = np.random.normal(0, 1, size=(n_paths, n_steps))
    for t in range(1, n_steps + 1):
        paths[:, t] = paths[:, t - 1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z[:, t - 1])

    return times, paths


def monte_carlo_price_european_option(S0, K, T, r, sigma, n_steps, n_paths, option_type='call', seed=None, return_std=False):
    '''
    Prices a European call or put option using Monte Carlo simulation.

    Parameters:
        S0 (float): Initial stock price
        K (float): Strike price
        T (float): Time to maturity (in years)
        r (float): Risk-free interest rate
        sigma (float): Volatility 
        n_steps (int): Number of simulation time steps
        n_paths (int): Number of Monte Carlo simulation paths
        option_type (str): 'call' or 'put'
        seed (int, optional): Random seed
        return_std (bool): If True, returns standard error of the estimate

    Returns:
        float or (float, float): Estimated option price (and standard error if requested)
    '''
    _, paths = simulate_gbm_paths(S0, r, sigma, T, n_steps, n_paths, seed)
    S_T = paths[:, -1]

    if option_type == 'call':
        payoffs = np.maximum(S_T - K, 0)
    elif option_type == 'put':
        payoffs = np.maximum(K - S_T, 0)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    discounted_payoffs = np.exp(-r * T) * payoffs
    price = np.mean(discounted_payoffs)
    std_error = np.std(discounted_payoffs, ddof=1) / np.sqrt(n_paths)

    if return_std:
        return price, std_error
    else:
        return price



# In[5]:


pwd


# In[ ]:





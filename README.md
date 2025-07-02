# Project 1

## Module 1: Black-Scholes Pricing and Greeks Engine

This module builds an analytical engine for European option pricing under the Black-Scholes framework.

### Key Features
- **Modular implementation** of call and put pricing
- **Analytical Greeks**: Delta, Gamma, Vega, Theta, Rho
- All functions stored in `functions_Black_Scholes.py`

### Visual Explorations
- Option price vs spot price and time to expiration
- Greek sensitivities vs time and spot for both calls and puts
- Moneyness and maturity effects visualized clearly

### Results Interpretation
- Greeks peak around ATM, especially for short maturities
- Delta transitions are sharper for short expiry
- Vega and Theta show meaningful time-decay patterns

This module forms the foundation for future modules involving stochastic volatility, numerical schemes, and delta hedging strategies.

### Numerical Greeks via Finite Differences
This introduces a general-purpose finite difference engine to compute numerical estimates of Greeks and validate them against the analytical solutions. Both call and put options are tested, with results showing strong agreement and low absolute error, confirming the accuracy of the model implementation.

# Lesson 06: Bayesian Inference with PyMC

## Overview
For R users coming from `brms` or `rstan`, **PyMC** is the standard tool for Bayesian modeling in Python. It allows you to specify models using a intuitive syntax and perform MCMC sampling efficiently.

## 1. Defining a Model (Linear Regression)
In PyMC, models are defined within a `with` statement (a context manager).

```python
import pymc as pm
import numpy as np
import arviz as az

# 1. Generate synthetic data
true_alpha, true_beta, true_sigma = 1, 2, 1
X = np.random.randn(100)
y = true_alpha + true_beta * X + np.random.randn(100) * true_sigma

# 2. Define the Model
with pm.Model() as linear_model:
    # Priors (Informative or weakly informative)
    alpha = pm.Normal('alpha', mu=0, sigma=10)
    beta = pm.Normal('beta', mu=0, sigma=10)
    sigma = pm.HalfNormal('sigma', sigma=1)
    
    # Expected value (The linear predictor)
    mu = alpha + beta * X
    
    # Likelihood (Sampling distribution)
    # observed=y tells PyMC this is the data we're fitting to
    Y_obs = pm.Normal('Y_obs', mu=mu, sigma=sigma, observed=y)
    
    # 3. Sample from the Posterior
    # This runs the MCMC chains (equivalent to chains=4 in Stan)
    trace = pm.sample(draws=1000, tune=1000, chains=4)
```

## 2. Diagnostics and Summaries (ArviZ)
`ArviZ` is the companion library for analyzing Bayesian results.

```python
# View the trace plots (Look for "fuzzy caterpillars")
az.plot_trace(trace)

# Statistical summary of the posterior
# Includes Mean, SD, HDI (Highest Density Interval), and R-hat
summary = az.summary(trace)
print(summary)

# Forest plot of the parameters
az.plot_forest(trace, var_names=['alpha', 'beta'])
```

## 3. Posterior Predictive Checks
Just like `pp_check()` in `brms`, we want to see if our model can simulate data that looks like our original data.

```python
with linear_model:
    # Generate predicted data based on the posterior
    ppc = pm.sample_posterior_predictive(trace)

# Plot the comparison
az.plot_ppc(ppc)
```

---

## 🏆 Challenge Exercise: The Robust Regression
1.  **Context:** Outliers can bias a Normal likelihood. A common solution is to use a **Student-T** distribution for the likelihood instead.
2.  Modify the linear regression model above to use `pm.StudentT` for the likelihood.
3.  Add a new prior for the degrees of freedom parameter (`nu`) of the Student-T distribution (e.g., `pm.Exponential('nu', 1/30)`).
4.  Run the model and compare the `beta` estimate with the original Normal model.
5.  **Bonus:** Use `az.plot_posterior` to visualize the distribution of `beta` and its 94% HDI.

---
[⬅️ Previous](../05_interactive/01_plotly_basics.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](../07_ml_deep_learning/01_ml_fundamentals.md)

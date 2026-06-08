# Block 1
import pymc as pm
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')

# Dummy data
hp_data = np.array([110, 175, 245, 62, 95])
wt_data = np.array([2.62, 3.21, 3.44, 2.14, 3.15])
y_data = np.array([21, 21, 14, 22, 19])

# For hierarchical examples
group_names = ['A', 'B', 'C']
group_idx = [0, 1, 2, 0, 1]
x = np.random.randn(5)
y = np.random.randn(5)
beta = 1.0

# Block 2
import pymc as pm
import numpy as np

with pm.Model() as model:
    # 1. Define Priors (The parameters we want to estimate)
    alpha = pm.Normal('alpha', mu=0, sigma=10)
    beta_hp = pm.Normal('beta_hp', mu=0, sigma=10)
    beta_wt = pm.Normal('beta_wt', mu=0, sigma=10)
    sigma = pm.HalfNormal('sigma', sigma=1)

    # 2. The Linear Predictor (The "Formula")
    mu = alpha + beta_hp * hp_data + beta_wt * wt_data

    # 3. The Likelihood (The "Family")
    # observed=y_data connects the model to your actual data
    y_obs = pm.Normal('y_obs', mu=mu, sigma=sigma, observed=y_data)

    # 4. Sampling (MCMC)
    # Similar to brm(... chains=4, iter=2000)
    trace = pm.sample(500, tune=500, chains=2)

# Block 3
import arviz as az

# 1. Trace Plots (Are the chains mixing?)
# R: plot(model)
az.plot_trace(trace)

# 2. Posterior Distributions
# R: mcmc_areas(model)
az.plot_dist(trace.posterior['beta_hp'])

# Block 4
# Hierarchical intercept example
with pm.Model(coords={"group": group_names}) as hierarchical_model:
    # Hyper-priors
    mu_a = pm.Normal("mu_a", mu=0, sigma=10)
    sigma_a = pm.HalfNormal("sigma_a", sigma=1)
    
    # Group-level intercepts (The "Random Effects")
    # dims="group" tells PyMC to create one 'a' for each group
    a = pm.Normal("a", mu=mu_a, sigma=sigma_a, dims="group")
    
    # Likelihood
    mu = a[group_idx] + beta * x
    y_obs = pm.Normal("y_obs", mu=mu, sigma=sigma, observed=y)


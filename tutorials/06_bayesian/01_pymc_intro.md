# Lesson 08: Bayesian Inference with PyMC

## Overview
For R users coming from `brms` or `rstan`, **PyMC** is the primary tool for Bayesian modeling in Python. While `brms` uses a formula interface to build Stan code, PyMC allows you to build the model directly in Python using a intuitive, block-based syntax.

## 1. The Mental Model: Formula vs. Graph
In `brms`, you define the model with a string like `y ~ x`. In PyMC, you define the **Generative Process**.

### Simple Linear Regression
**R (brms):**
```r
model <- brm(mpg ~ hp + wt, data = mtcars, family = gaussian())
```

**Python (PyMC):**
```python
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
    trace = pm.sample(2000, tune=1000, chains=4)
```

---

## 2. Comparing Terminology
| R (brms/Stan) | Python (PyMC/ArviZ) | Explanation |
| --- | --- | --- |
| `chains` | `chains` | Number of independent MCMC runs. |
| `iter` | `draws` | Number of samples to keep after tuning. |
| `warmup` | `tune` | Initial steps used to adapt the sampler. |
| `posterior` | `InferenceData` | The object containing the results (trace). |
| `summary()` | `az.summary()` | The table of means, sds, and HDIs. |

---

## 3. Diagnostics with ArviZ
In R, you use `bayesplot`. In Python, we use **ArviZ**.

```python
import arviz as az

# 1. Trace Plots (Are the chains mixing?)
# R: plot(model)
az.plot_trace(trace)

# 2. Posterior Distributions
# R: mcmc_areas(model)
az.plot_posterior(trace, var_names=['beta_hp', 'beta_wt'])

# 3. Forest Plot
# R: mcmc_intervals(model)
az.plot_forest(trace, hdi_prob=0.95)
```

---

## 4. Hierarchical Models
One of the strengths of `brms` is how easy it is to add random effects: `y ~ x + (1 | group)`. In PyMC, we use **Coords** and **Dims** to handle indexing.

```python
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
```

---

## 🏆 Challenge Exercise: The Robust Model
1.  **Task:** Build a simple linear regression in PyMC (like the first example).
2.  **Modification:** Change the likelihood from `pm.Normal` to `pm.StudentT`.
3.  **Prior:** Add a prior for the degrees of freedom `nu` (e.g., `pm.Exponential('nu', 1/30)`).
4.  **Comparison:** Why would an analyst choose a Student-T over a Normal distribution? (Hint: Outliers).
5.  **Diagnostic:** Use `az.plot_ppc(trace)` to see if the Student-T model fits the data better than a Normal model.

---
[⬅️ Previous](../05_interactive/01_plotly_basics.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](../07_ml_deep_learning/01_supervised_learning.md)

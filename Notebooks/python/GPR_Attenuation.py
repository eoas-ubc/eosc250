# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.1.7
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
# %matplotlib inline
from gpgLabs.GPR.Attenuation import *

# %% [markdown]
# # Attenuation of EM wave

# %% [markdown]
# To simplify the GPR problem, we assumed that we do not have conductivity effect. However, in practice, this is not true. For instance, the earth medium can have considerably high conductivity values. In this case, EM wave attenuates as a function of conductivity ($\sigma$), permittivity ($\epsilon$), and frequency ($f$). Thus, we can write velocity of EM wave as:
#
# $$ v(\sigma, f, \epsilon)$$
#
# In addition, electromagnetic wave, which propagates in the earth attenuates in several reasons why:
#
# - Geometric decaying
# - Electrical conductivity ($\sigma$, S/m)
#
# To measure how much it attenuates we define skin depth as the depth at which the intensity of the radiation inside the material falls to 1/e (about 37%) of its original value. And it can be written as:
#
# $$ \delta(\sigma, f, \epsilon) $$
#
# By adjusting parameters below, you will indentify how velocity and skin depth change as a function of $\sigma$, $\epsilon$, and $f$.

# %% [markdown]
# ## Parameters:

# %% [markdown]
# - epsr: Relative permittivity of the medium
#
# - sigma: Log10(Conductivity, S/m)
#
# You can read the value of the skin depth at 25, 100 & 1000 MHz above the graph.

# %%
AttenuationWidgetTBL()

# %%

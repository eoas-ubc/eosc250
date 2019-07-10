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
from gpgLabs.EM.ResponseFct import *
# %matplotlib inline

# %% [markdown]
# # Computing Apparent Resistivity
#
# In this app, we compute apparent resistivity using the response curves for a two-loop Frequency domain system for a two-layer earth. Below figure shows horizontal coplanar (HCP) configuration. 
#
# <img src="https://github.com/geoscixyz/gpgLabs/blob/master/figures/EM/ResponseFct/ResponseFct.png?raw=true"> </img>
#
# Assuming the coil spacing $s \ll \delta$, where $\delta$ is the skin depth, the apparent conductivity is given by
#
# $$
# \sigma_a = \int_0^\infty \phi(z) \sigma(z) dz
# $$
#
# Where 
#  - $\sigma_a$ is the apparent conductivity
#  - $\phi$ is the response function
#  - $\sigma$ is the conductivity structure
#
# Note that in the following plots, the y-axis is a normalized depth: $z/s$ where $s$ is the source-receiver separation.  

# %% [markdown]
# Two different configurations of source-receiver configurations are considered:
#
# - HCP: Horizontal coplanar system. The associated dipoles are perpendicular to the plane of the loops and are therefore in the vertical direction. The response function associated with this is .
#
# - VCP: Vertical coplanar system. The associated dipoles are perpendicular to the plane of the loops and are therefore in the horizontal direction. The response function associated with this is .
#
# For more, see the <a href="http://gpg.geosci.xyz/en/latest/content/electromagnetics/dual_loop_systems.html">GPG section on dual loop systems</a>

# %% [markdown]
# ## Parameters:
#
# - h$_{boom}$: height of the source-receiver boom from the surface [m]
#
# - h$_{1}$: thickness of the first layer [m]
#
# - $\sigma_{1}$: conductivity of the first layer [S/m]
#
# - $\sigma_{2}$: conductivity of the second layer [S/m]
#
# - configuration: configuration of the source-receiver

# %%
app = interactive_responseFct()
display(app)

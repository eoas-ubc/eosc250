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

# %% [markdown]
# # Expo site characterization using EM-31
#
#
# ## Import Necessary Packages

# %%
# %matplotlib inline
from gpgLabs.EM.FEMpipe import *

# %% [markdown]
# # Pipe Widget
#
# In the following app, we consider a loop-loop system with a pipe taget. Here, we simulate two surveys, one where the boom is oriented East-West (EW) and one where the boom is oriented North-South (NS). 
#
# <img src="https://github.com/geoscixyz/gpgLabs/blob/master/figures/EM/FEMpipe/model.png?raw=true" style="width: 40%; height: 40%"> </img>
#
# The variables are:
#
# - alpha: 
# $$\alpha = \frac{\omega L}{R} = \frac{2\pi f L}{R}$$
# - pipedepth: Depth of the pipe center
#
# We plot the percentage of Hp/Hs ratio in the Widget. 

# %%
pipe = interact_femPipe()
pipe

# %%

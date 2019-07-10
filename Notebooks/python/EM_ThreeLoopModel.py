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
# # Electromagnetics: 3-loop model
#
# In the first part of this notebook, we consider a 3 loop system, consisting of a transmitter loop, receiver loop, and target loop. 
#
# <img src="https://github.com/geoscixyz/gpgLabs/blob/master/figures/EM/FEM3Loop/SurveyParams.png?raw=true" style="width: 60%; height: 60%"> </img>
#
#
# ## Import Necessary Packages

# %%
# %matplotlib inline
from gpgLabs.EM.FEM3loop import *
from gpgLabs.EM.FEMpipe import *

# %% [markdown]
#
# Your Default Parameters should be: 
#
# <table>
# <tr>
# <th>Parameter </th>
# <th>Default value</th>
# </tr>
# <tr>
# <td>Inductance:</td>
# <td>L = 0.1</td>
# </tr>
# <tr>
# <td>Resistance:</td>
# <td>R = 2000</td>
# </tr>
# <tr>
# <td>X-center of target loop:</td>
# <td>xc = 0</td>
# </tr>
# <tr>
# <td>Y-center of target loop:</td>
# <td>yc = 0</td>
# </tr>
# <tr>
# <td>Z-center of target loop:</td>
# <td>zc = 1</td>
# </tr>
# <tr>
# <td>Inclination of target loop:</td>
# <td>I = 0</td>
# </tr>
# <tr>
# <td>Declination of target loop:</td>
# <td>D = 90</td>
# </tr>
# <tr>
# <td>Frequency:</td>
# <td>f = 10000 </td>
# </tr>
# <tr>
# <td>Sample spacing:</td>
# <td>dx = 0.25 </td>
# </tr>
# </table>
#
# To use the default parameters below, either click the box for "default" or adjust the sliders for R, zc, and dx. When answering the lab questions, make sure all the sliders are where they should be!

# %% [markdown]
# ## Run FEM3loop Widget

# %%
fem3loop = interactfem3loop()
fem3loop

# %% [markdown]
# # Pipe Widget
#
# In the following app, we consider a loop-loop system with a pipe taget. Here, we simulate two surveys, one where the boom is oriented East-West (EW) and one where the boom is oriented North-South (NS). 
#
# <img src="https://github.com/geoscixyz/gpgLabs/blob/master/figures/EM/FEM3Loop/model.png?raw=true" style="width: 40%; height: 40%"> </img>
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

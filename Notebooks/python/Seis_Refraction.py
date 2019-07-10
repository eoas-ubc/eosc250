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
from gpgLabs.Seismic.SeismicRefraction import *

# %% [markdown]
# # Interpretation and data acquisition strategies of seismic refraction data

# %% [markdown]
# In the <a href="https://www.3ptscience.com/app/SeismicRefraction">3pt Science app</a>, you explored the expected arrival times for refractions and reflections from a two-layer over a half-space model. 
#
# In this notebook, we will use synthetic seismic data to examine the impact of survey parameters on the expected seismic data.

# %% [markdown]
# ## Source 

# %% [markdown]
# In an ideal case, the source wavelet would be an impulse (ie. an instantaneous spike). However, in reality, the source energy is spread in space and in time (see the <a href="http://gpg.geosci.xyz/content/seismic/wave_basics.html#waves-and-rays">GPG: Waves and Rays</a>). The source wavelet used for these examples is shown below. 

# %%
plotWavelet()

# %% [markdown]
# ## Data
#
# Below, we show 3 plots:
# - **left**: expected arrival times for the direct, refracted waves and reflection from the first layer
# - **center**: clean data - the wavelet arriving at the expected arrival time. Each line represents what would be recorded by an ideal geophone.
# - **right**: noisy data - clean data + random noise. 
#
# The model used is the same as is in the lab write-up: 
# - v1 = 400 m/s
# - v2 = 1000 m/s
# - v3 = 1500 m/s
# - z1 = 5m (depth to layer 1)
# - z2 = 15m (depth to layer 2)

# %%
fig, ax = plt.subplots(1, 3, figsize=(15,6))
ax[0].set_title('Expected Arrival Times')
ax[1].set_title('Clean Data')
ax[2].set_title('Noisy Data')
ax[0]=viewTXdiagram(x0=1., dx=8, v1=400., v2=1000., v3=1500., z1=5., z2=15., ax=ax[0])
ax[1]=plotWiggleTX(x0=1., dx=8, v1=400., v2=1000., v3=1500., z1=5., z2=15., ax=ax[1])
ax[2]=plotWiggleTX(x0=1., dx=8, v1=400., v2=1000., v3=1500., z1=5., z2=15., ax=ax[2], noise=True)
plt.show()

# %% [markdown]
# ## Setup for the seismic refraction survey

# %% [markdown]
# Consider a shot gather for seismic refraction survey, which means we have one shot (source), and multiple receivers (12). Shot location is fixed at x=0. There are two survey parameters: 
#
# - x0: offset between shot and the first geophone
# - dx: spacing between two consecutive geophones
#
# In the widget below you can alter x0 or dx to change your survey setup. Run the next cell then try to change x0 and dx in the cell below that. Note that the next two cells are designed to help you visualize the survey layout. The x0 and dx parameter adjustment sliders here are not linked to the widget at the end of this notebook.

# %%
makeinteractSeisRefracSurvey()

# %% [markdown]
# ## Interpretation of seismic refraction data

# %% [markdown]
# Assume that you have seismic refraction data. The structure of the earth is unknown and you may want to obtain useful information about the subsurface. We will assume that the subsurface in the survey area has a three-layer structure and that the velocities increase with depth. 
# Thus, there can be four unknowns:
#
# - v1: velocity of the first layer (m/s)
# - v2: velocity of the second layer (m/s)
# - v3: velocity of the third layer (m/s)
# - z1: depth of the first layer (m)
# - z2: depth of the second layer (m)
#
# Based on the above information, we may expect to have up to four arrivals at a geophone, related to 
#
# - Direct
# - Reflected: interface 1
# - Refraction: interface 1
# - Refraction: interface 2

# %% [markdown]
# The widget below will allow you to estimate the layer depths and velocities. The parameters for the widget are:
#
# - x0: offset between shot and the first geophone
# - dx: spacing between two consecutive geophones
# - Fit: checking this activates fittting function (if you click this red line will show up)
# - tI: intercept time for a line function (s)
# - v: inverse slope of the line function (m/s; which can be velocity of either direct and critically refracted wave)

# %% [markdown]
# ### Run below widget and find useful subsurface information!

# %%
makeinteractTXwigglediagram()

# %%

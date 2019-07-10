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
# # Seismic Resolution and Forward Modelling

# %%
# Import the necessary packages
# %matplotlib inline   
from gpgLabs.Seismic.syntheticSeismogram import *  

# %% [markdown]
# When referring to vertical resolution, the question to ask is: "Can the two arrivals (one from the top, and one from the bottom of the layer) be distinguished?" 
#
# Adjust the layer thickness for the middle layer (by adjusting d2 and/or d3) and the frequency of the input pulse to investigate vertical resolution. You can also add noise to the trace. 
#
# The geologic model is:
# <img src="https://github.com/geoscixyz/gpgLabs/blob/master/figures/Seismic/geoModel.png?raw=true" style="width: 50%; height: 50%"></img>
#

# %% [markdown]
# Parameters of the below widget are:
#
# - d2: depth of the interface between layer 1 and 2
# - d3: depth of the interface between layer 2 and 3
# - rho1: density of the layer 1 ($kg/m^3$)
# - rho2: density of the layer 2 ($kg/m^3$)
# - rho3: density of the layer 3 ($kg/m^3$)
# - v1: velocity of the layer 1 ($m/s$)
# - v2: velocity of the layer 2 ($m/s$)
# - v3: velocity of the layer 3 ($m/s$)
# - wavef: peak frequency of the Ricker wavelet
# - waveA: amplitude of Ricker wavelet
# - AddNoise: swith for adding noise 
# - usingT: switch for considering transmission coefficient for reflectivity

# %%
InteractSeismogramTBL()

# %%

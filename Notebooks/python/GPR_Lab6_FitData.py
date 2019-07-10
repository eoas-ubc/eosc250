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
# # Ground Penetrating Radar Lab 6 Notebook

# %% [markdown]
# This notebook contains two apps, which are used to complete **part 3** in GPR Lab 6:
#
# + **Pipe Fitting App**: This app simulates the radargram signature from a cylindrical pipe and lays it over a set of field collected data.
# + **Slab Fitting App**: This app simulates the radargram signature from a rectangular slab and lays it over a set of field collected data.
#
# By using the models provided (pipe/slab) to fit data signatures within field collected radargram data, we can determine the existence, location and dimensions of pipes and slabs. You may also use this app to learn how radargram signatures from pipes and rectangular slabs change as the parameters provided are altered.

# %% [markdown]
# ## Importing Packages

# %%
# %matplotlib inline
from gpgLabs.GPR.GPRlab1 import *
from SimPEG.Utils import download

# %% [markdown]
# ## Pipe Fitting App
#
# <img style="float: right; width: 500px" src="https://github.com/geoscixyz/gpgLabs/blob/master/figures/GPR/pipemodel.png?raw=true">
#
# In the context of the lab exercise (Interpretation of Field Data), it is known that several pipes are likely buried below the GPR acquisition line. Unfortunately, we do no know the location or dimensions of the pipes. Here, you will attempt to fit radargram signatures corresponding to pipe-shaped objects. Parameters which provide the best fit can be used to infer characteristics of buried pipes.
#
# ### Parameters for the App:
#
# + **epsr:** Relative permittivity of the background medium
# + **h:** Distance from center of the pipe to the surface
# + **xc:** Horizontal location of the pipe center
# + **r:** radius of the pipe

# %%
URL = "http://github.com/geoscixyz/gpgLabs/raw/master/figures/GPR/ubc_GPRdata.png"
radargramImage = downloadRadargramImage(URL)
PipeWidget(radargramImage)

# %% [markdown]
# ## Slab Fitting App
#
# <img style="float: right; width: 500px" src="https://github.com/geoscixyz/gpgLabs/blob/master/figures/GPR/slabmodel.png?raw=true">
#
# In the context of the lab exercise (Interpretation of Field Data), it is known that a concrete casing is buried below the GPR acquisition line. Unfortunately, we do no know the location or depth of the casing. Here, you will attempt to fit radargram signatures corresponding to the casing using a rectangular slab model. Parameters which provide the best fit can be used to infer information about the casing.
#
# ### Parameters for the App:
#
# + **epsr:** Relative permittivity of the background medium
# + **h:** Distance from center of the pipe to the surface
# + **x1:** Horizontal location of left boundary of the concrete casing model
# + **x2:** Horizontal location of horizontal location of right boundary of the concrete casing modelradius of the pipe

# %%
URL = "http://github.com/geoscixyz/gpgLabs/raw/master/figures/GPR/ubc_GPRdata.png"
radargramImage = downloadRadargramImage(URL)
WallWidget(radargramImage)

# %%

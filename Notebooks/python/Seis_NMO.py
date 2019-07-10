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
# # Seismic NMO Widget

# %% [markdown]
# ## Using the Notebook

# %% [markdown]
# This is the <a href="https://jupyter.org/">Jupyter Notebook</a>, an interactive coding and computation environment. For this lab, you do not have to write any code, you will only be running it. 
#
# To use the notebook:
# - "Shift + Enter" runs the code within the cell (so does the forward arrow button near the top of the document)
# - You can alter variables and re-run cells
# - If you want to start with a clean slate, restart the Kernel either by going to the top, clicking on Kernel: Restart, or by "esc + 00" (if you do this, you will need to re-run Step 0 before running any other cells in the notebook) 
#
# Instructions as to how to set up Python and the iPython notebook on your personal computer are attached in the appendix of the lab

# %% [markdown]
# ## Step 0: Import Necessary Packages

# %%
# %pylab inline
from gpgLabs.Seismic.NMOwidget import *

# Define path to required data files
synDataFilePath = 'http://github.com/geoscixyz/gpgLabs/raw/master/assets/Seismic/syndata1.npy'
obsDataFilePath = 'https://github.com/geoscixyz/gpgLabs/raw/master/assets/Seismic/obsdata1.npy'
timeFilePath= 'https://github.com/geoscixyz/gpgLabs/raw/master/assets/Seismic/time1.npy'

# Download the data
synData = download(synDataFilePath,overwrite=True,verbose=False)
obsData = download(obsDataFilePath,overwrite=True,verbose=False)
timeData = download(timeFilePath,overwrite=True,verbose=False)

# %% [markdown]
# # Two common-mid-point (CMP) gathers: Clean and Noisy

# %% [markdown]
# We have two CMP gathers generated from different geologic models. One data set is clean and the other is contaminated with noise. The seismic data were adapted from SeismicLab (http://seismic-lab.physics.ualberta.ca/). 
#
# In this notebook, we will walk through how to construct a normal incidence seismogram from these data sets.
#
# We will do this in the following steps:
# - Plot the data
# - Fit a hyperbola to the reflection event in the data
# - Perform the NMO correction and stack

# %% [markdown]
# ## Step 1: Plot the data

# %% [markdown]
# As you can see from clean CMP gather, you can recognize that we have only have one reflector, meaning there is a single interface seperating two geologic units visible in these data. 
# (Note: The direct and any refracted arrivals have been removed). 
#
# It is difficult to distinguish any reflectors in the noisy data. However, there is a single reflector in these data, and we will perform normal moveout (NMO) and stacking operations to construct a normal-incidence seismogram where this reflector is visible.  

# %%
# Plot the data
ViewWiggle(synData, obsData)

# %% [markdown]
# ### Step 2: Fit A Hyperbola to the Data

# %% [markdown]
# - Each reflection event in a CMP gather has a travel time that corresponds to a hyperbola: 
#
# $$ t(x) = \sqrt{\frac{x^2}{v^2_{stacking}} + t_0^2}$$ 
#
# where $x$ is offset between source and receiver, $v_{stacking}$ is stacking velocity, and $t_0$ is the intercept time: 
#
# $$ t_0 = \sqrt{\frac{4d^2}{v^2_{stacking}}}$$
#
# where $d$ is the thickness of the first layer.
#
# - For each reflection event hyperbola, perform a velocity analysis to find $v_{stacking}$. This is done by first choosing $t_o$. Then choose a trial value of velocity. <img src="http://www.eos.ubc.ca/courses/eosc350/content/methods/meth_10d/assets/kearey_fig4_21.gif"></img>
#
# - Calculate the Normal Moveout Correction: Using the hyperbolia corresponding to $v_{stacking}$, compute the normal moveout for each trace and then adjust the reflection time by the amount $\triangle T$: $$ \triangle T = t_0-t(x) \\ $$ <img src="http://www.eos.ubc.ca/courses/eosc350/content/methods/meth_10d/assets/ch1_fig8.gif"></img>
#
# Estimate $t_0$, and a plausible $v_{stack}$ by altering t0 and v using below widget. This hyperbola will be drawn as red hyperbola on the middle panel. On the right panel we apply stack with the velocity that you fit, and provice stacked trace.

# %% [markdown]
# Parameters of the below widget to fit observed reflection event are:
#
# - t0: intercept time of the hyperbola 
# - v: velocity of the hyperbola

# %%
# Fit hyperbola to clean data
clean = InteractClean(synData,timeData)
clean

# %% [markdown]
# ### Step 3: Applying NMO correction to the Noisy Data

# %% [markdown]
# Compared to the previous data set, this one is quite noisy. There is a reflector in the data, and your goal is to construct a stacked trace where this reflection is visible. 
#
# Estimate $t_0$, and a plausible $v_{stack}$ by altering t0 and v using below widget. This hyperbola will be drawn as red hyperbola on the middle panel. On the right panel we apply stack with the velocity that you fit, and provice stacked trace.

# %%
noisy = InteractNosiy(obsData,timeData)
noisy

# %% [markdown]
# ### Step 4: Apply CMP stack with estimated $v_{stack}$ (For noisy CMP gather)

# %% [markdown]
# In the previous step, you chose an intercept time (t0) and a stacking velocity (v). Running below cell will generate trhee stacked traces:
# - Left: using t0 and v-200 m/s that we fit from Step 3
# - Middle: using t0 and v that we fit from Step 3
# - Right: using t0 and v+200 m/s that we fit from Step 3

# %%
NMOstackthree(obsData, noisy.kwargs["t0"], noisy.kwargs["v"]-200., noisy.kwargs["v"], noisy.kwargs["v"]+200.,timeData)

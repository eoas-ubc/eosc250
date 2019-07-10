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
from gpgLabs.DC import *
from IPython.display import display
# %matplotlib inline

# %% [markdown]
# # 1. Understanding currents, fields, charges and potentials

# %% [markdown]
# ## Cylinder app
#
#  - **survey**: Type of survey
#  - **A**: (+) Current electrode  location
#  - **B**: (-) Current electrode  location
#  - **M**: (+) Potential electrode  location
#  - **N**: (-) Potential electrode  location
#  - **r**: radius of cylinder
#  - **xc**: x location of cylinder center
#  - **zc**: z location of cylinder center
#  - **$\rho_1$**: Resistivity of the halfspace
#  - **$\rho_2$**: Resistivity of the cylinder
#  - **Field**: Field to visualize
#  - **Type**: which part of the field
#  - **Scale**: Linear or Log Scale visualization

# %%
app = cylinder_app();
display(app)

# %% [markdown]
# # 2. Potential differences and Apparent Resistivities
#
# Using the widgets contained in this notebook you will develop a better understand of what values are actually measured in a DC resistivity survey and how these measurements can be processed, plotted, inverted, and interpreted.
#
# ## Computing Apparent Resistivity
#
# In practice we cannot measure the potentials everywhere, we are limited to those locations where we place electrodes. For each source (current electrode pair) many potential differences are measured between M and N electrode pairs to characterize the overall distribution of potentials. The widget below allows you to visualize the potentials, electric fields, and current densities from a dipole source in a simple model with 2 layers. For different electrode configurations you can measure the potential differences and see the calculated apparent resistivities. 
#
# In a uniform halfspace the potential differences can be computed by summing up the potentials at each measurement point from the different current sources based on the following equations:
#
# \begin{align}
#     V_M = \frac{\rho I}{2 \pi} \left[ \frac{1}{AM} - \frac{1}{MB} \right] \\
#     V_N = \frac{\rho I}{2 \pi} \left[ \frac{1}{AN} - \frac{1}{NB} \right] 
# \end{align} 
# where $AM$, $MB$, $AN$, and $NB$ are the distances between the corresponding electrodes. 
#
# The potential difference $\Delta V_{MN}$ in a dipole-dipole survey can therefore be expressed as follows,
#
# \begin{equation}
#     \Delta V_{MN} = V_M - V_N = \rho I \underbrace{\frac{1}{2 \pi} \left[ \frac{1}{AM} - \frac{1}{MB} - \frac{1}{AN} + \frac{1}{NB} \right]}_{G}
# \end{equation}
#
# and the resistivity of the halfspace $\rho$ is equal to,
#
# $$
#     \rho = \frac{\Delta V_{MN}}{IG}
# $$
#
# In this equation $G$ is often referred to as the geometric factor. 
#
# In the case where we are not in a uniform halfspace the above equation is used to compute the apparent resistivity ($\rho_a$) which is the resistivity of the uniform halfspace which best reproduces the measured potential difference.
#
# In the top plot the location of the A electrode is marked by the red +, the B electrode is marked by the blue -, and the M/N potential electrodes are marked by the black dots. The $V_M$ and $V_N$ potentials are printed just above and to the right of the black dots. The calculted apparent resistivity is shown in the grey box to the right. The bottom plot can show the resistivity model, the electric fields (e), potentials, or current densities (j) depending on which toggle button is selected. Some patience may be required for the plots to update after parameters have been changed.

# %% [markdown]
# ## Two layer app

# %% [markdown]
# - **A**: (+) Current electrode  location
# - **B**: (-) Current electrode  location
# - **M**: (+) Potential electrode  location
# - **N**: (-) Potential electrode  location
# - **$\rho_1$**: Resistivity of the top layer
# - **$\rho_2$**: Resistivity of the bottom layer
# - **h**: thickness of the first layer
# - **Plot**: Field to visualize
# - **Type**: which part of the field

# %%
app = plot_layer_potentials_app()
display(app)

# %% [markdown]
# # 3. Building Pseudosections 
#
# 2D profiles are often plotted as pseudo-sections by extending $45^{\circ}$ lines downwards from the A-B and M-N midpoints and plotting the corresponding $\Delta V_{MN}$, $\rho_a$, or misfit value at the intersection of these lines as shown below. For pole-dipole or dipole-pole surveys the $45^{\circ}$ line is simply extended from the location of the pole. By using this method of plotting, the long offset electrodes plot deeper than those with short offsets. This provides a rough idea of the region sampled by each data point, but the vertical axis of a pseudo-section is not a true depth.
#
# In the widget below the red dot marks the midpoint of the current dipole or the location of the A electrode location in a pole-dipole array while the green dots mark the midpoints of the potential dipoles or M electrode locations in a dipole-pole array. The blue dots then mark the location in the pseudo-section where the lines from Tx and Rx midpoints intersect and the data is plotted. By stepping through the Tx (current electrode pairs) using the slider you can see how the pseudo section is built up.
#
# The figures shown below show how the points in a pseudo-section are plotted for pole-dipole, dipole-pole, and dipole-dipole arrays. The color coding of the dots match those shown in the widget.
# <br />
# <br />
# <img style="float: center; width: 60%; height: 60%" src="https://github.com/geoscixyz/gpgLabs/blob/master/figures/DC/PoleDipole.png?raw=true">
# <center>Basic skematic for a uniformly spaced pole-dipole array.
# <br />
# <br />
# <br />
# <img style="float: center; width: 60%; height: 60%" src="https://github.com/geoscixyz/gpgLabs/blob/master/figures/DC/DipolePole.png?raw=true">
# <center>Basic skematic for a uniformly spaced dipole-pole array. 
# <br />
# <br />
# <br />
# <img style="float: center; width: 60%; height: 60%" src="https://github.com/geoscixyz/gpgLabs/blob/master/figures/DC/DipoleDipole.png?raw=true">
# <center>Basic skematic for a uniformly spaced dipole-dipole array.
# <br />
#

# %% [markdown]
# ## Pseudo-section app

# %%
app = MidpointPseudoSectionWidget();
display(app)

# %% [markdown]
# ## DC pseudo-section app

# %% [markdown]
#  - **$\rho_1$**: Resistivity of the first layer (thickness of the first layer is 5m)
#  - **$\rho_2$**: Resistivity of the cylinder
#  - resistivity of the second layer is 1000 $\Omega$m
#  - **xc**: x location of cylinder center
#  - **zc**: z location of cylinder center
#  - **r**: radius of cylinder
#  - **surveyType**: Type of survey

# %%
app = DC2DPseudoWidget()
display(app)

# %% [markdown]
# # 4. Parametric Inversion
#
# In this final widget you are able to forward model the apparent resistivity of a cylinder embedded in a two layered earth. Pseudo-sections of the apparent resistivity can be generated using dipole-dipole, pole-dipole, or dipole-pole arrays to see how survey geometry can distort the size, shape, and location of conductive bodies in a pseudo-section.  Due to distortion and artifacts present in pseudo-sections trying to interpret them directly is typically difficult and dangerous due to the risk of misinterpretation. Inverting the data to find a model which fits the observed data and is geologically reasonable should be standard practice.   
#
# By systematically varying the model parameters and comparing the plots of observed vs. predicted apparent resistivity a parametric inversion can be preformed by hand to find the "best" fitting model. Normalized data misfits, which provide a numerical measure of the difference between the observed and predicted data, are useful for quantifying how well and inversion model fits the observed data. The manual inversion process can be difficult and time consuming even with small examples sure as the one presented here. Therefore, numerical optimization algorithms are typically utilized to minimized the data misfit and a model objective function, which provides information about the model structure and complexity, in order to find an optimal solution.
#
# ## Parametric DC inversion app
#
# Definition of variables:
# - **$\rho_1$**: Resistivity of the first layer 
# - **$\rho_2$**: Resistivity of the cylinder
# - **xc**: x location of cylinder center
# - **zc**: z location of cylinder center
# - **r**: radius of cylinder
# - **predmis**: toggle which allows you to switch the bottom pannel from predicted apparent resistivity to normalized data misfit
# - **suveyType**: toggle which allows you to switch between survey types.
#
# Knonw information
# - resistivity of the second layer is 1000 $\Omega$m
# - thickness of the first layer is known: 5m
#
# Unknowns are: $\rho_1$, $\rho_2$, xc, zc, and r

# %%
app = DC2DfwdWidget()
display(app)

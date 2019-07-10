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
# # Ground Penetrating Radar TBL4 Notebook
#
# ## Overview
#
# This notebook contains two apps, which are used to complete **part 2** and **part 3** in team TBL assignment 4:
# + **GPR Zero Offset App**: This app simulates radargram data from two reflectors buried in a homogeneous Earth. The range of parameter values for this app are set such that we may assume we are operating in the wave regime.
# + **Attenuation App**: This app computes the propagation velocity and skin depth for GPR signals as a function of operating frequency.

# %% [markdown]
# ## Importing Packages

# %%
# %matplotlib inline
from gpgLabs.GPR.GPR_zero_offset import *
from gpgLabs.GPR.Attenuation import *

# %% [markdown]
# ## GPR Zero Offset App (Wave Regime)
#
# This app is used to complete **part 2** of the team TBL. As previously mentionned, the app simulates radargram data from two reflectors buried in a homogeneous Earth. The range of parameter values for this app are set such that we may assume we are operating in the wave regime. In the wave regime, the following formulas can be used to approximate propagation velocity and skin depth:
# + **Propagation Velocity:** $\;\;\; v = \dfrac{c}{\sqrt{\varepsilon_r}}$
# + **Skin Depth:** $\;\;\; \delta = 0.0053 \, \dfrac{\sqrt{\varepsilon_r}}{\sigma}$
#
# *Note however, that expressions for the horizontal resolution, vertical layer resolution and wavelength found in the GPG are still valid.*
#
# ### Parameters for the App:
#
# + $\sigma$: Conductivity for the Earth in mS/m
# + $\varepsilon_r$: Relative permittivity for the Earth (unitless)
# + $f_c$: Central operating frequency for the instrument in MHz
# + $x_1, d_1$ and $R_1$: The x-location, depth and radius of reflector 1 in metres
# + $x_2, d_2$ and $R_2$: The x-location, depth and radius of reflector 2 in metres

# %%
fc = 250*1e6
d = 6
v = 3*1e8 / np.sqrt(4)
np.sqrt(v*d / (2*fc))

# %%
WidgetWaveRegime()

# %% [markdown]
# ## Attenuation App
#
# This app is used to complete **part 3** of the team TBL. As mentionned previously, the app computes the propagation velocity and skin depth for GPR signals as a function of operating frequency. Because we are working in the general case, the propagation velocity and skin depth are given by:
#
# + **Propagation Velocity:** $\;\;\; v = \sqrt{\dfrac{2}{\mu \varepsilon}} \Bigg [ \Bigg ( 1 + \bigg ( \dfrac{\sigma}{\omega \varepsilon} \bigg )^2 \Bigg )^{1/2} + 1 \; \Bigg ]^{-1/2}$
# + **Skin Depth:** $\;\;\; \delta = \sqrt{\dfrac{2}{\omega^2 \mu \varepsilon}} \Bigg [ \Bigg ( 1 + \bigg ( \dfrac{\sigma}{\omega \varepsilon} \bigg )^2 \Bigg )^{1/2} - 1 \; \Bigg ]^{-1/2}$
#
# where $\omega = 2\pi f_c$ and $f_c$ is the operating frequency. Here, we assume that the Earth is non-magnetic (e.g. $\mu = \mu_0$). The app provides the values for the propagation velocity and skin depth at frequencies $f_c$ = 25,100 and 1000 MHz.
#
# ### Parameters for the App:
#
# + $epsr$: Relative permittivity of the medium (unitless)
# + $sigma$: Log (base 10) conductivity of the medium. *Note that sigma = -1.5 corresponds to a true conductivity of* $\sigma$ *= 0.0316 S/m*.

# %%
AttenuationWidgetTBL()

# %%

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
# # GPG Labs
#
# <a href="http://gpg.geosci.xyz"><img src="http://gpg.geosci.xyz/_images/intro.png" alt="http://gpg.geosci.xyz" align="right" width="200"></a>
#
# This collection of notebooks covers basic principles of applied geophysics. Associated material can be found in the <a href="http://gpg.geosci.xyz">GPG: Geophysics for Practicing Geoscientists</a>.
#
#
#
# If you have feedback, we would like to hear from you! 
# - <a href="http://geosci.xyz/contact">Contact us</a>
# - <a href="https://github.com/ubcgif/gpgLabs/issues">Report issues</a>
# - <a href="https://github.com/ubcgif/gpgLabs/">Join the development</a>

# %% [markdown]
# ## Contents
#
# ### Magnetics
# - <a href="MagneticDipoleApplet.ipynb">MagneticDipoleApplet.ipynb</a> - Magnetic dipole applet
# - <a href="MagneticPrismApplet.ipynb">MagneticPrismApplet.ipynb</a> - Magnetic prism applet
# - <a href="Mag_Induced2D.ipynb">Mag_Induced2D.ipynb</a> - Induced magnetic anomaly demo
# - <a href="Mag_FitProfile.ipynb">Mag_FitProfile.ipynb</a> - Fit one magnetic profile from field observation
#
# ### Seismic
# - <a href="SeismicApplet.ipynb">SeismicApplet.ipynb</a> - Seismic Applet
# - <a href="Seis_Refraction.ipynb">Seis_Refraction.ipynb</a> - Seismic refraction survey demo
# - <a href="Seis_Reflection.ipynb">Seis_Reflection.ipynb</a> - Synthetic reflection seismogram
# - <a href="Seis_NMO.ipynb">Seis_NMO.ipynb</a> - Normal moveout demo
# - <a href="Seis_VerticalResolution.ipynb">Seis_VerticalResolution.ipynb</a> - Vertical resolution in reflection
#
# ### Ground Penetrating Radar
# - <a href="GPR_TBL4_DOI_Resolution.ipynb">GPR_TBL4_DOI_Resolution.ipynb</a> - Horizontal resolution + Probing distance of GPR
# - <a href="GPR_Lab6_FitData.ipynb">GPR_Lab6_FitData.ipynb</a> - Fit field GPR data
#
# ### Electromagnetics
# - <a href="InductionRLcircuit_Harmonic.ipynb">InductionRLcircuit_Harmonic.ipynb</a> - Two coil app
# - <a href="EM_ThreeLoopModel.ipynb">EM_ThreeLoopModel.ipynb</a> - EM induction explained by a 3-loop circuit model
# - <a href="EM_Pipeline.ipynb">EM_Pipeline.ipynb</a> - EM response over a pipeline
# - <a href="EM_EM31.ipynb">EM_ResponseFunction.ipynb</a> - EM-31 response and apparent conductivity
#
# ### Direct Current Resistivity
# - <a href="DC_SurveyDataInversion.ipynb">DC_SurveyDataInversion.ipynb</a> - Physics, survey, data and interpretation

# %% [markdown]
# <center><a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" width=60 src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a> 
#
# This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.</center>

# %%
# # !pip install git+https://github.com/geoscixyz/gpgLabs.git@master

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

# %% [markdown] {"extensions": {"jupyter_dashboards": {"version": 1, "views": {"grid_default": {"col": 0, "height": 11, "hidden": false, "row": 0, "width": 12}, "report_default": {"hidden": false}}}}}
# This is the <a href="https://jupyter.org/">Jupyter Notebook</a>, an interactive coding and computation environment. For this lab, you do not have to write any code, you will only be running it. 
#
# To use the notebook:
# - "Shift + Enter" runs the code within the cell (so does the forward arrow button near the top of the document)
# - You can alter variables and re-run cells
# - If you want to start with a clean slate, restart the Kernel either by going to the top, clicking on Kernel: Restart, or by "esc + 00" (if you do this, you will need to re-run the following block of code before running any other cells in the notebook) 

# %%
from gpgLabs.Mag.MagDipoleApp import MagneticDipoleApp

# %% [markdown]
# # Magnetic Prism Applet
#
#

# %% [markdown] {"extensions": {"jupyter_dashboards": {"version": 1, "views": {"grid_default": {"col": 0, "height": 3, "hidden": true, "row": 11, "width": 12}, "report_default": {"hidden": true}}}}}
# ## Purpose
#
# From the Magnetic Dipole applet, we have learned how anomalous magnetic field observed at ground's surface look
# The objective is to learn about the magnetic field observed at the ground's surface, caused by a retangular susceptible prism. 
#
#
# ## What is shown
#
# - <b>The colour map</b> shows the strength of the chosen parameter (Bt, Bx, By, or Bz) as a function of position.
#
# - Imagine doing a two dimensional survey over a susceptible sphere that has been magentized by the Earth's magnetic field specified by inclination and declination.  "Measurement" location is the centre of each coloured box. This is a simple (but easily programmable) alternative to generating a smooth contour map.
#
# - The anomaly depends upon magnetic latitude, direction of the inducing (Earth's) field, the depth of the buried dipole, and the magnetic moment of the buried dipole.
#
#
# ## Important Notes:
#
# - <b>Inclination (I)</b> and <b>declination (D)</b> describe the orientation of the Earth's ambient field at the centre of the survey area. Positive inclination implies you are in the northern hemisphere, and positive declination implies that magnetic north is to the east of geographic north.
#
# - The <b>"length"</b> adjuster changes the size of the square survey area. The default of 72 means the survey square is 72 metres on a side.
#
# - The <b>"data spacing"</b> adjuster changes the distance between measurements. The default of 1 means measurements were acquired over the survey square on a 2-metre grid. In other words, "data spacing = 2" means each coloured box is 2 m square.
#
# - The <b>"depth"</b> adjuster changes the depth (in metres) to the top of the buried prism.
#
# - The <b>"magnetic moment (M)"</b> adjuster changes the strength of the induced field. Units are Am2.  This is related to the strength of the inducing field, the susceptibility of the buried sphere, and the volume of susceptible material.
# - <b>Bt, Bx, By, Bz</b> are Total field, X-component (positive northwards), Y-component (positive eastwards), and Z-component (positive down) of the anomaly field respectively.
#
# - Checking the <b>fixed scale</b> button fixes the colour scale so that the end points of the colour scale are minimum and maximum values for the current data set.
#
# - You can generate a <b>profile</b> along either "East" or "North" direction
#
# - Check <b>half width</b> to see the half width of the anomaly. Anomaly width is noted on the botton of the graph.
#
# - Measurements are taken 1m above the surface.

# %% [markdown] {"extensions": {"jupyter_dashboards": {"version": 1, "views": {"grid_default": {"col": 0, "height": 11, "hidden": false, "row": 11, "width": 6}, "report_default": {"hidden": false}}}}}
# ## Define a 3D prism
# Compared to the MagneticDipoleApplet, there are additional parameters to define a prism.
#
# - $\triangle x$: length in North (X) direction (m)
# - $\triangle y$: length in East (Y) direction (m)
# - $\triangle z$: length in Depth (z) direction (m) below the receiver
# - depth: top boundary of the prism (meter)
# - I$_{prism}$: inclination of the prism (reference is north direction)
# - D$_{prism}$: declination of the prism (reference is north direction) 

# %%
mag = MagneticDipoleApp()
mag.interact_plot_model_prism()

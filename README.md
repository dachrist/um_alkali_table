# um_alkali_table
Scripts to make alkali abundance tables for the UM

Relevant scripts and input files:
make_grid_input.py - This script creates the table of temperatures and pressures to be used by ATMO
atmo_grid.in - This is the ATMO input script that, once the table of pressures and temperatures is made, computes the equilibrium abundances.
make_table.py - This script takes the ATMO outputs and makes a text file table to be used by the UM.

chem_venot_plus_alkali.ncdf - This is the list of species used by ATMO.  It is simply the Venot et al. (2019) species list plus gas phase neutral alkali species.  

Using the species:

If you don't want to change the PT grid:

1) Run make_grid_input.py to make the initial grid for atmo (python make_grid_input.py)
2) Edit atmo_grid.in to set the metallicity and change any chemical abundances (c/o ratio, etc).  You may also need to set the paths for the NASA coeffs.
2) Run atmo (atmo.x atmo_grid.in, if atmo.x is in your path)
3) Edit make_table.py to choose your input and output file names (the input file here being the output of ATMO).
4) Run make_table.py to convert the ATMO data into the UM input (python make_table.py)

If you want to change the grid:
1) Edit make_grid_input to change the grid parameters (hopefully self explanatory).
2) Edit atmo_grid.in to set the number of grid elements.  If you don't set this appropriately, ATMO will try to build a hydrostatic grid and you'll get nonsense.

Things not included but that you might want to consider:

1) There aren't condensed or ionized species included.  The ionized species might be interesting especially as ionization will reduce the alkali abundances in hotter hot Jupiters.
2) If molecules including alkali species (NaOH, etc.) are included as opacity sources, these tables could be extended to include those species as well.

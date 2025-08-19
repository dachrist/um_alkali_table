# A python routine to read an ATMO chemistry file 

import netCDF4 as nc

def read_atmo_chem(fname):

  #Read atmo chemistry file
  data = nc.Dataset(fname)

  #Get pressure, abundances and molecule names
  pressure   = data.variables['pressure'][:]*0.1 # Convert to Pa 
  abundances = data.variables['abundances'][:,:]
  names      = data.variables['molname'][:]

  
  species_name = []
  for j in range(len(names[:,0])):
    name = names[j,0]+names[j,1]+names[j,2]+names[j,3]+names[j,4]+names[j,5]+names[j,6]+names[j,7]+names[j,8]+names[j,9]
    species_name.append((name.decode("utf-8")).strip())
  
  return pressure, abundances, species_name

def read_atmo_chem_cpmmw(fname):

  #Read atmo chemistry file
  data = nc.Dataset(fname)

  #Get pressure, cp and mean molecular weight
  pressure   = data.variables['pressure'][:]*0.1 # Convert to Pa 
  #cp         = data.variables['cp'][:]
  mmw        = data.variables['mean_mol_mass'][:]

  return pressure, mmw


def read_atmo_pt(fname):

    #Read atmo chemistry file
    data = nc.Dataset(fname)

    #Get pressure, abundances and molecule names
    pressure    = data.variables['pressure'][:]*0.1 # Convert to Pa
    temperature = data.variables['temperature'][:]


    
    return pressure, temperature

import numpy as np
import netCDF4 as nc

ntemp = 80
npres = 60
t1d = np.linspace(400,4000,ntemp) # K
p1d = np.logspace(-2,8,npres) # si

p1d = p1d*10.

t3d,p3d = np.meshgrid(t1d,p1d)

t = t3d.ravel()
p = p3d.ravel()

nlevel = ntemp*npres

print("nlevel = ",nlevel)

fout = "pt.nc"

nout = nc.Dataset(fout,'w')

#nout.createDimension('nz',1)
#nout.createDimension('ny',1)
nout.createDimension('nlevel',nlevel)
npres=nout.createVariable('pressure','f8',('nlevel'))
ntemp=nout.createVariable('temperature','f8',('nlevel'))

npres.units  = 'dyne cm-2'
ntemp.units  = 'K'

npres[:]  = p[:]
ntemp[:]  = t[:]

nout.close()



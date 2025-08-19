import numpy as np
import netCDF4 as nc
from read_atmo_chem import read_atmo_chem,read_atmo_pt,read_atmo_chem_cpmmw

ntemp = 80
npres = 60


fin = 'chem_grid_mdh3.ncdf'
fout = 'tables/alkali_table_mdh3.txt'

p,ab,names = read_atmo_chem(fin)
names = np.array(names)
p,mmw = read_atmo_chem_cpmmw(fin)
p,t = read_atmo_pt(fin)


mmw = mmw.reshape(npres,ntemp)

mmw = 2.33

mw_Na = 22.98976928
mw_K  = 39.0983
mw_Cs = 132.9055
mw_Rb = 85.4678
mw_Li = 6.94

# find the chemical indices
idx_Na = np.where(names == 'Na')[0]
idx_Rb = np.where(names == 'Rb')[0]
idx_Cs = np.where(names == 'Cs')[0]
idx_K = np.where(names == 'K')[0]
idx_Li = np.where(names == 'Li')[0]

t1d = (t.reshape(npres,ntemp))[0,:]
p1d = (p.reshape(npres,ntemp))[:,0]
NaData = (ab[idx_Na,:].reshape(npres,ntemp))*mw_Na/mmw
KData =  (ab[idx_K,:].reshape(npres,ntemp))*mw_K/mmw
CsData = (ab[idx_Cs,:].reshape(npres,ntemp))*mw_Cs/mmw
RbData = (ab[idx_Rb,:].reshape(npres,ntemp))*mw_Rb/mmw
LiData = (ab[idx_Li,:].reshape(npres,ntemp))*mw_Li/mmw


f = open(fout,"w")
f.write("{} {}\n".format(ntemp,npres))
f.write("Temperatures\n")
f.write(" ".join(str(x) for x in t1d))
f.write("\n")
f.write("Pressures\n")
f.write(" ".join(str(x) for x in p1d))
f.write("\n")

f.write("Na Data\n")
for i in range(0,npres):
    f.write(" ".join(str("{:>16.8e}".format(x)) for x in NaData[i,:]))
    f.write("\n")
f.write("K Data\n")
for i in range(0,npres):
    f.write(" ".join(str("{:>16.8e}".format(x)) for x in KData[i,:]))
    f.write("\n")
f.write("Cs Data\n")
for i in range(0,npres):
    f.write(" ".join(str("{:>16.8e}".format(x)) for x in CsData[i,:]))
    f.write("\n")

f.write("Rb Data\n")
for i in range(0,npres):
    f.write(" ".join(str("{:>16.8e}".format(x)) for x in RbData[i,:]))
    f.write("\n")

f.write("Li Data\n")
for i in range(0,npres):
    f.write(" ".join(str("{:>16.8e}".format(x)) for x in LiData[i,:]))
    f.write("\n")
    
f.close()

import sys
import numpy as np
import netCDF4 as nc

def ncread(filename, ncVariable='guess'):
  
  ncIn = nc.Dataset(filename, 'r')

  print(ncIn)

  if (ncVariable=='guess'):
    #find variable with max size
    v = ncIn.variables.keys()
    sizeMax=0
    vMax=0
    for vKey in v:
      vShape = ncIn.variables[vKey].shape
      sizeCurr=1
      for dim in np.arange(len(vShape)):
        sizeCurr *= vShape[dim]
      if (sizeCurr > sizeMax):
        sizeMax = sizeCurr
        vMax = vKey
    var = ncIn.variables[vMax]
    print("Determined variable %s to be the data to be read in file: %s"%(vMax,filename))
  else:
    var = ncIn.variables[ncVariable]
    
  data = var[:]
    
  ncIn.close()
  
  return data


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        volume = ncread(filename)
        
        ##add your code here


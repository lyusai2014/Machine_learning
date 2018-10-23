#!/home/sxl1036/python/installing/python355/bin/python3

import numpy as np
import scipy
import math

# the self-learning part


class linearfitting: pass

lf=linearfitting()   
lf.eta=0.01
lf.n_iter=200
lf.ww=[0,0]

def dis (a,b) :
  X=np.array([1,2,3])
  Y=np.array([2,3,4])
  dis=0
  for xi,yi in zip(X,Y):
    dis=dis+(xi*a+b-yi)**2
  return dis

for i  in range(lf.n_iter) :
     if dis(lf.ww[0],lf.ww[1]) >= dis(lf.ww[0]+lf.eta,lf.ww[1]):
        lf.ww[0] += lf.eta
     if dis(lf.ww[0],lf.ww[1]) <  dis(lf.ww[0]+lf.eta,lf.ww[1]):
        lf.ww[0] -= lf.eta
     if dis(lf.ww[0],lf.ww[1]) >= dis(lf.ww[0],lf.ww[1]+lf.eta):
        lf.ww[1] += lf.eta
     if dis(lf.ww[0],lf.ww[1]) <  dis(lf.ww[0],lf.ww[1]+lf.eta):
        lf.ww[1] -= lf.eta
print(lf.ww)




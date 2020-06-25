#!/usr/bin/env python

import sys
import numpy as np
import scipy.linalg
from astropy.io import fits

matrices = list()
with fits.open(sys.argv[1]) as fx:
    # for i in range(10):
    for i in range(len(fx)):
        matrices.append(np.array(fx[i].data))

w1 = list()
v1 = list()
w2 = list()
v2 = list()

for m in matrices:
    w, v = scipy.linalg.eigh(m)
    w1.append(w)
    v1.append(v)

for m in matrices:
    w, v = scipy.linalg.eigh(m)
    w2.append(w)
    v2.append(v)

print('If scipy.linalg.eigh is completely reproducible,')
print('all of the following will be True:')
print('  - close/exact: the eigval/eigvec pass np.allclose and np.all')
print('  - Mclose/Mexact: M = (V W V.T) pass np.allclose and np.all')
print()
for i in range(len(w1)):
    m1 = (v1[i]*w1[i]).dot(v1[i].T)
    m2 = (v2[i]*w2[i]).dot(v2[i].T)
    print('{:2d} close:{:6s}  exact:{:6s}  Mclose:{:6s}  Mexact:{:6s}'.format(i,
        str(np.allclose(w1[i],w2[i]) and np.allclose(v1[i],v2[i])),
        str(np.all(w1[i]==w2[i]) and np.all(v1[i]==v2[i])),
        str(np.allclose(m1,m2)),
        str(np.all(m1==m2)),
        ))


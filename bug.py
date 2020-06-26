# coding: utf-8
import numpy as np
import scipy.linalg

def load_from_fits():
    from astropy.io import fits
    matrices = list()
    fn = 'eigh.fits'
    with fits.open(fn) as fx:
        # for i in range(10):
        for i in range(len(fx)):
            matrices.append(np.array(fx[i].data))
    return matrices

def load_from_csv():
    matrices = list()
    matrices.append(np.loadtxt('matrix0.csv', dtype='d', delimiter=','))
    return matrices

def load_from_npz():
    matrices = list()
    zf = np.load('all.npz')
    for i in range(len(zf)):
        matrices.append(zf['arr_' + str(i)])
    return matrices


if __name__ == '__main__':

    m = load_from_npz()
    r = 4

    ws, vs = list(), list()
    for _ in range(r):
        # print(hex(m[0].__array_interface__['data'][0]))
        w, v = scipy.linalg.eigh(m[0])
        ws.append(w)
        vs.append(v)
    
    eq_m = np.empty((r,r), dtype='?')
    for i in range(r):
        for j in range(r):
            eq_m[i, j] = np.allclose(ws[i], ws[j]) and np.allclose(vs[i], vs[j])

    if np.all(eq_m):
        print("All ok!")
    else:
        print(eq_m)
        print(m[0].flags)
        #print((m.shape, m.dtype))

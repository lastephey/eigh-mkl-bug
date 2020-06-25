# eigh-mkl-bug

Summary: numpy/scipy linalg.eigh results are not reproducible when using MKL
and `OMP_NUM_THREADS=1` (but they are when using OpenBLAS). We have tested on two
different Linux systems.

We find that eigh is not reproducible when using MKL and export
`OMP_NUM_THREADS=1` for both numpy.linalg.eigh and scipy.linalg.eigh. We do not
find any problems when using OpenBLAS.

In this repo you will find:

1) `mkl-requirements.txt`

2) `blas-requirements.txt`

3) `test_numpy_eigh.py`

4) `test_scipy_eigh.py`

5) `eigh.fits`

You can run the test with

```
python test_numpy_eigh.py eigh.fits

```
for 3 cases:

```
OMP_NUM_THREADS not set
export OMP_NUM_THREADS=1
export OMP_NUM_THREADS=2
```

We have seen reproducibility issues when `OMP_NUM_THREADS=1`.

Thank you for your help.



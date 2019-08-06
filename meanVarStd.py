#Python 3
#Mean, Var, and STD using numpy


import numpy as np

n, m = map(int, input().split())
b =[]
b = np.array([list(map(int, input().split())) for _ in range(n)])
np.set_printoptions(legacy='1.13')
print(np.mean(b, axis=1))
print(np.var(b, axis=0))
print(np.std(b, axis=None))
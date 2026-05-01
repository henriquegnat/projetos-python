import numpy as np

A = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

N = int(input("Digite um número: "))

if N in A:
    print("Número está matriz!!")
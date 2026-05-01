import numpy as np

A = np.array = ([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])

pares = 0 
for num in A:
    for numero in num:
        if numero%2 == 0:
            pares += 1

print(pares)

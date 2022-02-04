import numpy as np
import copy


def llenavector(n):
    vector = np.zeros(n)
    for i in range(n):
        vector[i] = int(input())
    return vector


def ordenarvector(vector):
    n = vector.shape[0]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vector[j] < vector[i]:
                aux = vector[j]
                vector[j] = vector[i]
                vector[i] = aux
    return vector


vec1 = llenavector(6)
vec2 = ordenarvector(copy.copy(vec1))

print(vec1)
print(vec2)

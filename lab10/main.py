import numpy as np
import cmath
from scipy.linalg import dft
# 1

def fourier_matrix(N):
    F = []
    w = complex(cmath.cos(cmath.pi*2/N),(-1)*cmath.sin(2*cmath.pi/N))
    for i in range(N):
        F.append([])
        for k in range(N):
            F[i].append(complex(0,0))
            F[i][k] = (pow(w,i*k))
    return F

def my_dft(A):
    N =  len(A)
    return np.dot(fourier_matrix(N),A)


# print(my_dft([1,2,3,4]))

# print(dft(4))
# print(np.fft.fft([1,2,3,4]))
# print(np.ifft())
# 2

def my_idft(A):
    N =  len(A)
    F = np.conjugate(fourier_matrix(N))
    F /= N
    return np.dot(F,A)

# print(np.fft.ifft([1,2,3,4]))
# print(my_idft([1,2,3,4]))


# 3


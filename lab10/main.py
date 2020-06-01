import numpy as np
import cmath
from scipy.linalg import dft
from random import random
import matplotlib.pyplot as pyplot
import math
import time
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

def are_equals(A,B, delta):
    for i,e in enumerate(A):
            if(math.fabs(math.fabs(A[i].real) - math.fabs(B[i].real)) > delta or math.fabs(math.fabs(A[i].imag) - math.fabs(B[i].imag)) > delta):
                return False
    return True

for i in range(5):
    A = [random() for _ in range(5)]
    print(A)
    C = np.fft.fft(A)
    B = my_dft(A)

    print(C)
    print(B)
    print("Are equals ? ",are_equals(C,B,0.001))


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

for i in range(5):
    A = [random() for _ in range(5)]
    print(A)
    C = np.fft.ifft(A)
    B = my_idft(A)

    print(C)
    print(B)
    print("Are equals ? ",are_equals(C,B,0.001))

# 3

# https://www.youtube.com/watch?v=WsJlJexWKPw
# http://ortografia4.appspot.com/wiki/Algorytm_Cooleya-Tukeya

def my_cooley_turkey(X):
    n = len(X)
    val = cmath.exp(-2*cmath.pi*1j/n)
    if n > 1:
        X = my_cooley_turkey(X[::2]) + my_cooley_turkey(X[1::2])
        for k in range(n//2):
            xk = X[k]
            X[k] = xk + val**k*X[k+n//2]
            X[k+n//2] = xk - val**k*X[k+n//2]
    return X

X = [complex(random(),random()) for _ in range(8)]
print(X)
A = np.fft.fft(X)
print("Are equals ? ",are_equals(my_cooley_turkey(X),A,0.001))


for i in [2**5,2**6,2**7,2**8,2**9,2**10,2**11,2**12]:
    X = [complex(random(),random()) for _ in range(i)]

    print(f"Test dla macierzy o wielkosci {i} ")
    start = time.time()
    A = np.fft.fft(X)
    stop = time.time()
    t_lib = stop - start

    start = time.time()
    my_cooley_turkey(X)
    stop = time.time()
    t_wl = stop - start

    start = time.time()
    my_dft(X)
    stop = time.time()
    t_kw = stop - start

    print(f"Czasy:\n Biblioteka: {t_lib} Własny: {t_wl} kwadratowy: {t_kw}")

def generate_signal(ran):

    n1 = random()*10
    n2 = random()*10
    n3 = random()*10
    n4 = random()*10
    n5 = random()*10

    return (lambda x: cmath.sin(n1*x) + cmath.sin(n2*x) + cmath.sin(n3*x) + cmath.sin(n4*x) + cmath.sin(n5*x),
    lambda x: cmath.sin(n1*x) if x>=0 and x < ran/5 else cmath.sin(n2*x) if x>= ran/5 and x < 2*ran/5  else cmath.sin(n3*x) if x>= 2*ran/5 and x < 3*ran/5 else cmath.sin(n4*x) if x>= 3*ran/5 and x < 4*ran/5 else cmath.sin(n5*x))
    # return lambda x: cmath.sin(2*x) + cmath.sin(0.1*x),lambda  x: cmath.sin(5*x)
N = 10
ran = 500
s1,s2 = generate_signal(N)
x = []
y = []
x2 = []
y2 = []

for i in range(ran):
    x.append(i* N/ran )
    y.append(s1(i*N/ran))

    x2.append(N/ran * i)
    y2.append(s2(N/ran * i))


pyplot.plot(x,y,'ro',markersize=1)
pyplot.show()

pyplot.plot(x2,y2,'ro',markersize=1)
pyplot.show()

y3 = my_dft(y)
y4 = my_dft(y2)

eps = 10e-4

def draw_real(x,y):
    X = []
    Y= []
    for i in range(len(x)//2):
        X.append(x[i])
        Y.append(y[i].real + y[len(y)-i-1].real)
    pyplot.plot(X,Y)
    pyplot.show()

def draw_imag(x,y):
    X = []
    Y= []
    for i in range(len(x)//2):
        X.append(x[i])
        Y.append(y[i].imag + y[len(y)-i-1].imag)
    pyplot.plot(X,Y)
    pyplot.show()

draw_real(x,y3)
draw_imag(x,y3)

draw_real(x2,y4)
draw_imag(x2,y4)
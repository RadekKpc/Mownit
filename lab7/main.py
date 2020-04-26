from numpy.linalg import eig, norm
from random import randint
import math
import numpy as np
import time
import matplotlib.pyplot as plt
import scipy.linalg as linalg

epsilon = 0.0000001
inteartions = 99999

def show_matrix(mat):
    for i in mat:
        for j in i:
            print(j, end=' ')
        print()
    print()

# zad 1

def get_matrx(size):
    A = []
    for i in range(size):
        A.append([])
        for j in range(size):
            A[i].append(randint(0,100))
    return A


def vector_normalization(vec):
    norm2 = norm(vec, ord=np.inf)
    return vec/norm2

def power_finding(size,A):
    x0 = np.array([1 for i in range(size)])
    x0 = np.array(x0/norm(x0,np.inf))
    out = False

    for i in range(inteartions):

        x1 = np.dot(A,x0)
        x2 = x1/norm(x1, np.inf)

        if norm(x2 - x0) < epsilon:
            out = True
        x0 = x2
        if out:
            break

    return norm(x1, np.inf), x0/norm(x0)


A = get_matrx(3)
show_matrix(A)
w, v = eig(A)
print("Funcja biblioteczna:")
print(w)
print(v)
print("Moja funckja:")
print(power_finding(3,A))

A = get_matrx(5)
show_matrix(A)
w, v = eig(A)
print("Funcja biblioteczna:")
print(w)
print(v)
print("Moja funckja:")
print(power_finding(5,A))

A = get_matrx(10)
show_matrix(A)
w, v = eig(A)
print("Funcja biblioteczna:")
print(w)
print(v)
print("Moja funckja:")
print(power_finding(10,A))


def check_power_finding():
    y = []
    check_list = [x for x in range(100,2501,100)]
    for c in check_list:
        A = get_matrx(c)
        start = time.process_time()
        power_finding(c,A)
        end = time.process_time()
        print("Czas spedzony dla N = ",c,": ", end - start)
        y.append(end - start)

    plt.plot(check_list,y,'ro',markersize=1)
    plt.axis([0, 2600, 0.0, 5.0])
    plt.show()


# check_power_finding()

# zad 2

def inverse_power_method(size,A,sig):
    x0 = np.array([1.5 for i in range(size)])
    x0 = np.array(x0/np.linalg.norm(x0, ord=np.inf))
    for i in range(size):
        A[i][i] = A[i][i] - sig

    out = False
    LU = linalg.lu_factor(A)

    for i in range(inteartions):
        # Musimy obliczyc x z równania Ax = y za pomoca LU

        x1 = linalg.lu_solve(LU, x0)
        x2 = x1/np.linalg.norm(x1, ord=np.inf)

        if norm(x2 - x0) < epsilon:
            out = True

        x0 = x2

        if out:
            break

    return x1/norm(x1)

def test_inverse_power_method():
    A = get_matrx(3)
    show_matrix(A)
    w, v = eig(A)
    print("Funcja biblioteczna:")
    print(w)
    print(v)
    print("Moja funckja:")
    print("Dla sigmy równej w przybliżeniu: ", w[0])
    print(inverse_power_method(3,A,w[0] + 0.0001))
    print("Dla sigmy równej w przybliżeniu: ", w[1])
    print(inverse_power_method(3,A,w[1] + 0.0001))
    print("Dla sigmy równej w przybliżeniu: ", w[2])
    print(inverse_power_method(3,A,w[2] + 0.0001))

test_inverse_power_method()
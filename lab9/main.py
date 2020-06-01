from numpy.linalg import qr
import numpy as np
import math
import matplotlib.pyplot as pyplot

def gram_schmid_qr(A,n):
    A = np.array(A)
    for i in range(n):
        A[i] = np.array(A[i])
    A = np.matrix.transpose(A)

    U0 = A[0]/np.linalg.norm(A[0])
    U0 = np.array(U0)
    U = []
    U.append(U0)
    for k in range(1,n):

        sum_vec =  np.array([np.float(0) for l in range(n)])
        for i in range(k):
            sum_vec = sum_vec + (np.dot(U[i],A[k])*U[i])
        U.append(A[k] - sum_vec)
        U[k] =  U[k]/np.linalg.norm(U[k])

    Q =[]
    for i in range(n):
        Q.append(U[i])

    Q = np.array(Q)
    Q = np.matrix.transpose(Q)

    R = [[0 for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(k+1):
            R[i][k] = np.dot(U[i],A[k])

    return Q,np.array(R)


def are_equals(A,B, delta):
    for i,e in enumerate(A):
        for j,f in enumerate(A[i]):
            if(math.fabs(math.fabs(A[i][j]) - math.fabs(B[i][j])) > delta):
                return False
    return True


for i in range(5):
    A = np.random.rand(i+1,i+1)
    print(A)
    Q,R = gram_schmid_qr(A,i+1)
    q,r = qr(A)

    print(Q)
    print(R)
    print()
    print(q)
    print(r)

    print("Are equals Q?: ",are_equals(Q,q,0.001))
    print("Are equals R?: ",are_equals(R,r,0.001))


Matixes = []
cond_m = []
for i in range(500):
    strength = 10000
    cond = (i+1)*strength
    S =  np.random.rand(8,8)
    s,v,d = np.linalg.svd(S)
    v[7] = v[0]/cond
    M = np.dot(s,np.dot(np.diag(v),d))
    Matixes.append(S)
    cond_m.append(cond)


diff = []
# Norma Frobeniusa
for m in Matixes:

    Q, R = gram_schmid_qr(m,len(m))
    I = np.diag([1 for i in range(8)])
    dif = I - np.dot(np.matrix.transpose(Q),Q)
    suma = 0
    for i in dif:
        for j in i:
            suma = suma +  math.fabs(j*j)
    diff.append(math.sqrt(suma))

pyplot.plot(cond_m,diff,'ro',markersize=1)
pyplot.show()


print(diff)
print(cond_m)

def slove_qr(A,B):
    Q, R = gram_schmid_qr(A,len(A))
    v = np.dot(np.matrix.transpose(Q),B)
    l = np.dot(np.dot(np.matrix.transpose(Q),Q),R)

    #  back substitution
    for i in range(len(A)):
        v[i] = v[i]/l[i][i]
        l[i] = l[i]/l[i][i]


    for i in range(len(B) -1,-1,-1):
        print(i)
        for j in range(i+1,len(A)):
            v[i] = v[i] - v[j]*l[i][j]

    return v

A = [[1,1,1],[1,2,3],[2,1,1]]
b = [6,14,7]

res = slove_qr(A,b)
print(res)

# aproksymacja sredniowadratowa

N = 11
M = 3
x = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
y = [2,7,9,12,13,14,14,13,10,8,4]

# https://eti.pg.edu.pl/documents/176593/26763380/Wykl_AlgorOblicz_3.pdf
# Dane testowe z linku powyzej
# N = 7
# M = 3
# x = [0,0.5,1,1.5,2,3,3.5]
# y = [1.02,0.62,0.5,0.6,0.98,3.12,5.08]

# Obliczanie współczynnikow s i t
S = []
T = []
for i in range(0,2*M -1):
    suma = 0
    for j in range(0,N):
        mult = 1
        for k in range(0,i):
            mult *= x[j]
        suma += mult

    S.append(suma)

for i in range(M):
    suma = 0
    for j in range(0,N):
        mult = y[j]
        for k in range(0,i):
            mult *= x[j]
        suma += mult

    T.append(suma)


# Ulozenie macierzy

X = []
for i in range(M):
    X.append([])
    for j in range(i,i+M):
        X[i].append(S[j])

print(X)

A = slove_qr(X,T)

print(A)

c = A[0]
b = A[1]
a = A[2]

func = lambda x : a*x*x + b*x + c

res_x = []
res_y = []

start = min(x) -1
end = max(x) + 1
div = 1000
x_tmp = min(x) - 1
for i in range(div):
    res_x.append(x_tmp)
    res_y.append(func(x_tmp))
    x_tmp += (end -start)/div


pyplot.plot(res_x,res_y,'bo',markersize=1)
pyplot.plot(x,y,'ro',markersize=2)
pyplot.show()
from numpy.linalg import solve
from numpy.linalg import lstsq
from math import fabs
from scipy.linalg import lu
import time


def wyswietl(mat):
    for i in mat:
        for j in i:
            print(j, end=' ')
        print()


with open('macierz.txt') as f:
    w, h = [float(x) for x in next(f).split()]
    matrix = [[float(x) for x in line.split()] for line in f]

with open('left_side.txt') as f:
    w, h = [float(x) for x in next(f).split()]
    left_side = [[float(x) for x in line.split()] for line in f]
    left_side = left_side[0]





def row_operation(row, func, ls, n):
    for i, r in enumerate(row):
        row[i] = func(row[i])
    ls[n] = func(ls[n])


def check_is_zero(m, n, eps, ls):
    while abs(m[n][n]) < eps:
        for h, w in enumerate(m):
            if w[n] != 0 and h > n:
                for j, p in enumerate(w):
                    m[n][j] = m[n][j] + w[j]
                ls[n] = ls[n] + ls[h]


def solve_matrix():
    for i, r in enumerate(matrix):
        check_is_zero(matrix, i, 0.0001, left_side)
        to_divide = matrix[i][i]
        row_operation(matrix[i], lambda x: x / to_divide, left_side, i)

        for j, k in enumerate(matrix):
            if j != i:
                to_multiply = matrix[j][i]
                left_side[j] = left_side[j] - to_multiply * left_side[i]
                for p, r in enumerate(k):
                    matrix[j][p] = matrix[j][p] - to_multiply * matrix[i][p]


start = time.process_time()
solve_matrix()
end = time.process_time()
print("Time spent in above function is:", end - start)
print("Macierz:")
wyswietl(matrix)
print("Rozwiazanie:")
print(left_side)

with open('macierz.txt') as f:
    w, h = [float(x) for x in next(f).split()]
    matrix = [[float(x) for x in line.split()] for line in f]

with open('left_side.txt') as f:
    w, h = [float(x) for x in next(f).split()]
    left_side = [[float(x) for x in line.split()] for line in f]
    left_side = left_side[0]

# numpy.linalg.solve
print("Dla funkcji bibliotecznej numpy.linalg.solve")
start = time.process_time()
result = solve(matrix, left_side)
end = time.process_time()
print("Time spent in above function is:", end - start)
print("Rozwiazanie:")
list(result)
print(result)

# numpy.linalg.lstsq
print("Dla funkcji bibliotecznej numpy.linalg.lstsq")
start = time.process_time()
result = lstsq(matrix, left_side, rcond=None)
end = time.process_time()
print("Time spent in above function is:", end - start)
print("Rozwiazanie:")
list(result)
print(result)

with open('faktoryzacja.txt') as f:
    w, h = [float(x) for x in next(f).split()]
    A = [[float(x) for x in line.split()] for line in f]


def triangular_matrix(n, down=False):
    A = []
    for i in range(n):
        A.append([])
        for j in range(n):
            A[i].append(0)
    if down:
        for i in range(n):
            A[i][i] = 1
    return A


def change_rows(M, r1, r2, n):
    for i in range(n):
        tmp = M[r1][i]
        M[r1][i] = M[r2][i]
        M[r2][i] = tmp


def find_pivot(M, L, U, col, N, perm_A):
    if col == N - 1:
        return

    # OBLICZANIE WAEROSCI DO POSZUKIWANIA ELEMENTU WIODACEGO
    left = []
    for i in range(N):
        sum = 0
        if i >= col:
            for j in range(col):
                sum += L[i][j] * U[j][col]
            left.append(M[i][col] - sum)
        else:
            left.append(0)

    # SZUKANIE ELEMENTU WIODACEGO
    ret = 0
    for i, e in enumerate(left):
        if fabs(left[i]) > fabs(left[ret]):
            ret = i
    if (ret > col):
        change_rows(L, col, ret, col)
        change_rows(M, col, ret, N)
        # ZAPISYWANIE PERMUTACJI
        tmp = perm_A[col]
        perm_A[col] = perm_A[ret]
        perm_A[ret] = tmp


def multiply_rows(A, B, x, y, N):
    sum = 0
    for j in range(N):
        sum += A[x][j] * B[j][y]
    return sum


def crout_alg(M):
    N = len(M)
    L = triangular_matrix(N, True)
    U = triangular_matrix(N)
    perm_A = [i for i in range(N)]

    # DLA KAZDEJ KOLUMNY
    for i in range(N):
        # UZUPELNIANIE MACIERZY U
        for j in range(N):
            if j < i:
                U[j][i] = M[j][i] - multiply_rows(L, U, j, i, N)

        # CZESCIOWE POSZUKIWANIE ELEMENTU WIODACEGO
        find_pivot(M, L, U, i, N, perm_A)

        # UZUPELNIANIE ELEMENATU U[i][i]
        U[i][i] = (M[i][i] - multiply_rows(L, U, i, i, N))
        div = U[i][i]

        # UZUPELNIANIE MACIERZY L
        for j in range(N):
            if j > i:
                L[j][i] = (M[j][i] - multiply_rows(L, U, j, i, N)) / div

    return L, U, perm_A


(L, U, perm_A) = crout_alg(A)

wyswietl(L)
print()
wyswietl(U)
print("Permutacja macierzy A: ", perm_A)
print("Liczby w tablicy oznaczaja kolejnosc wierszy w permutowanej macierzy względem oryginału \n: ")

# Sprawdzenie funkcji

with open('faktoryzacja.txt') as f:
    w, h = [float(x) for x in next(f).split()]
    A = [[float(x) for x in line.split()] for line in f]

p, l, u = lu(A, permute_l=False)

wyswietl(l)
print()
wyswietl(u)
print("Peruatation matrix A: ", p)

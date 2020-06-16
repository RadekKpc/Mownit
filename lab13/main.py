# http://iswiki.if.uj.edu.pl/images/2/20/AiSD_22._Symulowane_wy%C5%BCarzanie_%28problem_komiwoja%C5%BCera%29.pdf


import random
import math
import numpy as np
from scipy.optimize import dual_annealing
import matplotlib.pyplot as plt


def dual_annealing2(f, swap ,N, maxiter=10000, callback = lambda x: None, initial_temp= 100000,cold_speed = 0.98):
    X = [i for i in range(N)]
    Y = [i for i in range(N)]
    B = [i for i in range(N)]
    b_length = 999999999
    Pr = lambda x: math.exp((-1)*x/initial_temp)
    length = 999999999
    for i in range(maxiter):

        swap(X)
        opt = f(X)

        if opt < length:
            Y = [x for x in X]
            length = opt
            if length < b_length:
                b_length = length
                B = [x for x in X]
        else:
            delta_length = math.fabs(opt - length)
            pr = random.uniform(0,1)
            if pr <= Pr(delta_length):
                Y = [x for x in X]
                length = opt
        
        initial_temp = cold_speed*initial_temp
    
    return B,b_length

    
def uniform_points(N,x_min,x_max,y_min,y_max):
    X = []
    Y = []
    for _ in range(N):
        X.append(random.uniform(x_min,x_max))
        Y.append(random.uniform(y_min,y_max))

    return X,Y

def four_gropus(N,d,x_length,y_length):
    X = []
    Y = []

    for i in range(N):
        if i%4 == 0:
            X.append(random.uniform(0,x_length))
            Y.append(random.uniform(0,y_length))

        if i%4 == 1:
            X.append(random.uniform(x_length+d,2*x_length + d))
            Y.append(random.uniform(y_length+d,2*y_length + d))

        if i%4 == 2:
            X.append(random.uniform(x_length + d, 2*x_length + d))
            Y.append(random.uniform(0,y_length))
        if i%4 == 3:
            X.append(random.uniform(0,x_length))
            Y.append(random.uniform(y_length+d,2*y_length + d))
    
    return X,Y


def normal_points(N, mu, sigma):
    X = np.random.normal(mu, sigma, N)
    Y = np.random.normal(mu, sigma, N)
    return X,Y

def visualize_points(X,Y):
    plt.plot(X,Y)
    plt.plot(X,Y,'ro',markersize=4)
    plt.show()

def length(X,Y,N):
    leng = 0
    for i in range(N-1):
        leng += math.sqrt((X[i]-X[i+1])**2 + (Y[i] - Y[i+1])**2)
    return leng

def salesman_lib(X,Y,N, temp = 5230):

    def permutation(x):
        P = []
        x2_copy = [f for f in x]
        for i in range(N):
            P.append(i)
        
        x2_ziped = list(zip(P,x2_copy))
        x2_ziped.sort(key=lambda tup: tup[1])
        x2_unziped = list(zip(*x2_ziped))
        x2_copy = x2_unziped[1]
        P = x2_unziped[0]
        return P
        
    def length(x):
        P = permutation(x)
        leng = 0
        for i in range(N-1):
            leng += math.sqrt((X[P[i]]-X[P[i + 1]])**2 + (Y[P[i]] - Y[P[i+1]])**2)
        return leng

    def adapt_points_to_permutation(P):
        x2 = []
        y2 = []
        for i in range(N):
            y2.append(Y[P[i]])
            x2.append(X[P[i]])
        return x2,y2

    salesman_func = lambda x : length(x)

    lw = [0] * N
    up = [1] * N

    ret = dual_annealing(salesman_func, bounds=list(zip(lw, up)),maxiter=1000,initial_temp=temp)
    print(f"Optymalna permutacja: ",permutation(ret.x)," \nDługośc ścieżki :", ret.fun)
    return adapt_points_to_permutation(permutation(ret.x))

def salesman(X,Y,N,cons_swap = True, arb_swap = False, temp = 5230):
        
    def consecutive_swap(x):
        # if cons_swap:
        pair_to_swap = random.randint(0,N-2)
        x[pair_to_swap], x[pair_to_swap + 1] = x[pair_to_swap + 1], x[pair_to_swap]

    def arbitrary_swap(x):
        # if arb_swap:
        node_1 = random.randint(0,N-1)
        node_2 = random.randint(0,N-1)
        while node_2 == node_1:
            node_2 = random.randint(0,N-1)

        x[node_1], x[node_2] = x[node_2], x[node_1]

    def length(x):

        P = x
        leng = 0
        for i in range(N-1):
            leng += math.sqrt((X[P[i]]-X[P[i + 1]])**2 + (Y[P[i]] - Y[P[i+1]])**2)
        return leng

    def adapt_points_to_permutation(P):
        x2 = []
        y2 = []
        for i in range(N):
            y2.append(Y[P[i]])
            x2.append(X[P[i]])
        return x2,y2

    salesman_func = lambda x : length(x)

    if arb_swap:
        ret,leng = dual_annealing2(salesman_func, arbitrary_swap, N,initial_temp=temp)
    if cons_swap:
        ret,leng = dual_annealing2(salesman_func, consecutive_swap, N,initial_temp=temp)
        
    print(f"Optymalna permutacja: ",ret," \nDługośc ścieżki :", leng)
    return adapt_points_to_permutation(ret)


N = 10
for i in range(6):
    print("Wylosowane punkty:")
    X,Y = uniform_points(N,10,0,10,0)
    visualize_points(X,Y)
    print("Długośc ścieżki :", length(X,Y,N))

    print("Impplementacja z funkcja biblioteczną:")
    X2,Y2 = salesman_lib(X,Y,N)
    visualize_points(X2,Y2)

    print("Arbitary swap:")
    X2,Y2 = salesman(X,Y,N,arb_swap=True,cons_swap=False)
    visualize_points(X2,Y2)

    print("Consecutive wap:")
    X2,Y2 = salesman(X,Y,N,arb_swap=False,cons_swap=True)
    visualize_points(X2,Y2)
    N += 5

N = 10
for i in range(6):
    print("Wylosowane punkty:")
    X,Y = normal_points(N,0,1)
    visualize_points(X,Y)
    print("Długośc ścieżki :", length(X,Y,N))

    print("Impplementacja z funkcja biblioteczną:")
    X2,Y2 = salesman_lib(X,Y,N)
    visualize_points(X2,Y2)

    print("Arbitary swap:")
    X2,Y2 = salesman(X,Y,N,arb_swap=True,cons_swap=False)
    visualize_points(X2,Y2)

    print("Consecutive wap:")
    X2,Y2 = salesman(X,Y,N,arb_swap=False,cons_swap=True)
    visualize_points(X2,Y2)
    N += 5
N = 10

for i in range(6):

    print("Wylosowane punkty:")
    X,Y = four_gropus(N,30,10,10)
    visualize_points(X,Y)
    print("Długośc ścieżki :", length(X,Y,N))

    print("Impplementacja z funkcja biblioteczną:")
    X2,Y2 = salesman_lib(X,Y,N)
    visualize_points(X2,Y2)

    print("Arbitary swap:")
    X2,Y2 = salesman(X,Y,N,arb_swap=True,cons_swap=False)
    visualize_points(X2,Y2)

    print("Consecutive wap:")
    X2,Y2 = salesman(X,Y,N,arb_swap=False,cons_swap=True)
    visualize_points(X2,Y2)
    N += 5

# temperatura

start_temp = 0.0001
for i in range(20):
    print("Dla temperatury:",start_temp)
    X2,Y2 = salesman_lib(X,Y,N,temp=start_temp)
    visualize_points(X2,Y2)
    start_temp = start_temp*10

#  Wizualizacja metody minimalizujacej funkcje celu: Kolejne kroki


def salesman_visualize(X,Y,N,no_swap = True,cons_swap = False, arb_swap = False, temp = None ):

    def permutation(x):
        P = []
        x2_copy = [f for f in x]
        for i in range(N):
            P.append(i)
        
        x2_ziped = list(zip(P,x2_copy))
        x2_ziped.sort(key=lambda tup: tup[1])
        x2_unziped = list(zip(*x2_ziped))
        x2_copy = x2_unziped[1]
        P = x2_unziped[0]
        return P
        
    def consecutive_swap(x):
        if cons_swap:
            pair_to_swap = random.randint(0,N-2)
            x[pair_to_swap], x[pair_to_swap + 1] = x[pair_to_swap + 1], x[pair_to_swap]

    def arbitrary_swap(x):
        if arb_swap:
            node_1 = random.randint(0,N-1)
            node_2 = random.randint(0,N-1)
            while node_2 == node_1:
                node_2 = random.randint(0,N-1)

            x[node_1], x[node_2] = x[node_2], x[node_1]

    def length(x):

        consecutive_swap(x)
        arbitrary_swap(x)
       
        P = permutation(x)
        leng = 0
        for i in range(N-1):
            leng += math.sqrt((X[P[i]]-X[P[i + 1]])**2 + (Y[P[i]] - Y[P[i+1]])**2)
        return leng

    def adapt_points_to_permutation(P):
        x2 = []
        y2 = []
        for i in range(N):
            y2.append(Y[P[i]])
            x2.append(X[P[i]])
        return x2,y2

    def callback(x,y, context):
        x_plt,y_plt = adapt_points_to_permutation(permutation(x))
        visualize_points(x_plt,y_plt)

    salesman_func = lambda x : length(x)

    lw = [0] * N
    up = [1] * N
    ret = dual_annealing(salesman_func, bounds=list(zip(lw, up)),maxiter=1000,callback=callback)
    print(f"Optymalna permutacja: ",permutation(ret.x)," \nDługośc ścieżki :", ret.fun)
    return adapt_points_to_permutation(permutation(ret.x))

N = 15
X,Y = uniform_points(N,10,0,10,0)
visualize_points(X,Y)
print("Długośc ścieżki :", length(X,Y,N))
X2,Y2 = salesman_visualize(X,Y,N)
visualize_points(X2,Y2)
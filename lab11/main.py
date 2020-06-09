import numpy as np
from random import random
import scipy
import scipy.stats as stats
import matplotlib.pyplot as plt
from scipy.special import erfc
import math
import struct


N = [10,1000,5000]


# https://matplotlib.org/3.1.1/gallery/statistics/hist.html
# https://www.geeksforgeeks.org/python-program-to-convert-floating-to-binary/
# https://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hex

def binary(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in str(struct.pack('!f', num)))

def frequency(bits):
    s = 0
    for l in bits:
        if l == '0':
            s -= 1
        if l == '1':
            s += 1
    sobs = s/(len(bits))
    res = (erfc(math.fabs(sobs)/math.sqrt(2)))
    print(res)
    if res >= 0.1 :
        print("Accept the sequence as random")
    else:
        print("Not accept the sequence as random")

    return res



def test_generators(N):
    twister = []
    pcg64 = []
    n_bins = 10

    for _ in range(N):
        twister.append(random())
        pcg64.append(np.random.default_rng().random())

    # show histograms

    _ , axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
    axs[0].hist(twister, bins=n_bins, color  = 'b', label = "twister")
    axs[0].legend()
    axs[1].hist(pcg64, bins=n_bins, color  = 'r', label = "pcg64")
    axs[1].legend()
    plt.show()

    twister_count = 0
    pcg64_count = 0
    # check equanation xi < xi+1
    for i in range(N-1):
        if twister[i] < twister[i+1]:
            twister_count += 1
        if pcg64[i] < pcg64[i + 1]:
            pcg64_count += 1

    print(f'N = {N}')
    print(f'dla pcg64 rownanie spełnia {pcg64_count} liczb\n')
    print(f'dla twister rownanie spełnia {twister_count} liczb\n')
    # test

    #Frequency (Monobit) Test

    twister_bit_string = ""
    pcg64_bit_string = ""
    for i in pcg64:
        pcg64_bit_string += binary(i)

    for i in twister:
        twister_bit_string += binary(i)

    frequency(pcg64_bit_string)
    frequency(twister_bit_string)

# test testu
print(frequency("1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"))

# for n in N:
#     test_generators(n)


# Generowanie liczb z rokladu normalnego
#  rozklad normalny:

NX = []
NY = []
for i in range(-10000,10000):
    NX.append(4*i/10000)
    NY.append((1/math.sqrt(2*math.pi))*math.exp(-math.pow(4*i/10000,2)/2))

plt.plot(NX,NY,'bo',markersize=1)
plt.show()

for n in N:
    X = []
    Y = []
    for i in range(n):

        while True:
            X1 = random()
            X2 = random()

            V1 = (float) (2*X1 - 1)
            V2 = (float) (2*X2 - 1)

            R = math.sqrt(math.fabs(V1*V1 - V2*V2))
            if R  < 1:
                break

        X.append(math.sqrt((-2)*math.log(X1))*(V1/R))
        Y.append(math.sqrt((-2)*math.log(X1))*(V2/R))

    _ , axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
    axs[0].hist(X, bins=10, color  = 'b', label = "twister")
    axs[0].plot(NX,np.array(NY)*n,'ro',markersize=1)
    # axs[0].plot(X,Y,'bo',markersize=1)
    axs[0].legend()
    axs[1].hist(Y, bins=10, color  = 'r', label = "pcg64")
    axs[1].plot(NX,np.array(NY)*n,'bo',markersize=1)
    axs[1].legend()
    plt.show()

    # testy shapiro-wilka
    WX = stats.shapiro(X)
    print(WX)
    WY = stats.shapiro(Y)
    print(WY)


# Wyznaczanie PI metoda monte carlo

def monte_carlo(n,visualize = True):

    in_circle_x = []
    in_circle_y = []

    out_circle_x = []
    out_circle_y = []

    for i in range(n):
        x = np.random.uniform(-1,1)
        y = np.random.uniform(-1,1)

        if x*x + y*y <= 1:
            in_circle_x.append(x)
            in_circle_y.append(y)
        else:
            out_circle_x.append(x)
            out_circle_y.append(y)

    if visualize:
        plt.plot(in_circle_x,in_circle_y,'ro',markersize=1)
        plt.plot(out_circle_x,out_circle_y,'bo',markersize=1)
        plt.show()

    return (4*len(in_circle_x)/n)

print(monte_carlo(10))
print(monte_carlo(100))
print(monte_carlo(1000))
print(monte_carlo(10000))
print(monte_carlo(100000))
print(monte_carlo(1000000))


# blad bezwzgledny a n

X = []
Y = []
for i in range(100,10000,10):
    Y.append(math.fabs(monte_carlo(i,visualize=False)-math.pi))
    X.append(i)

plt.plot(X,Y,'bo',markersize=1)

plt.show()




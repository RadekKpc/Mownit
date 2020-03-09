import numpy as np
from numpy import float32,power,float64
import matplotlib.pyplot as pyplot
import time

v = float32(0.53125)
numbers = [v]*10**7

def blad_wzgledny(number,result):
    return (number - result) / number

def blad_bezwzgledny(number,result):
    return (number - result)

# zad 1.1, 1.4
def tradycyjne_sumowanie(numbers):
    result = float32(0.0)
    blad_talbe = []

    start = time.time()
    c = 0
    for i in numbers:
        result = result + i
        if c%25000 == 0:
            blad_talbe.append(blad_wzgledny(v*(c + 1),result))
        c += 1
    end = time.time()
    tradycyjne_time =end - start
    print("Czas tradycyjnego",tradycyjne_time)
    pyplot.plot(blad_talbe)
    pyplot.show()

    return result

# zad 1.4
def tree_sum(numbers):
    if len(numbers) == 0:
        return float32(0.0)
    if len(numbers) == 1:
        return numbers[0]
    if len(numbers) == 2:
        return numbers[0] + numbers[1]

    return tree_sum(numbers[ :int(len(numbers)/2 )]) + tree_sum(numbers[ int(len(numbers)/2): ])

# zad 2
def kahan(numbers):
    suma = float32(0.0)
    err = float32(0.0)

    for i in numbers:
        y = i - err
        temp = suma + y
        err = (temp - suma) - y
        suma = temp

    return suma

# zad 1.2
print("TRADYCYJNE SUMOWANIE")
first = tradycyjne_sumowanie(numbers)

print("Blad wzgledny",blad_wzgledny(5312500,first))
print("Blad bezwzgledny",blad_bezwzgledny(5312500,first))
print()
# zad 1.5
print("TREE SUM")
start = time.time()
tree_numbers_sum = tree_sum(numbers)
end = time.time()
tree_time = end - start

print("Blad wzgledny",blad_wzgledny(5312500,tree_numbers_sum))
print("Blad bezwzgledny",blad_bezwzgledny(5312500,tree_numbers_sum))
print("Czas tree sum",tree_time)
print()

# zad 2.1
print("KAHAN SUM")
start = time.time()
kahan_sum = kahan(numbers)
end = time.time()
kahan_time = end - start

print("Blad wzgledny",blad_wzgledny(5312500,kahan_sum))
print("Blad bezwzgledny",blad_bezwzgledny(5312500,kahan_sum))
print("Czas Kahana", kahan_time)
print()
# zad 1.6
# tree_sum dziala woniej gdyż jest to algorytm oc zasie O(n*log(n))
# podczas gdy tradycyjne sumowanie to O(n)

# zad 2.2
#Ponieważ eliminuje błąd utraty low-order bitów,
#za kazdym razem jest wyliczany err czyli bity ktore zostaly utracone w sumowaniu duzej liczby i malej
#bity te są dodawane w nastepnym obiegu petli do kolejenj liczby

# zad 2.3
#Sumowanie rekurencyjne zajumje wiecej czasu gdyn ma zlozonosc O(n*log(n))
#podczas gdy algorytm Kahana ma czas liniowy

# zad 3
def dzeta(s,n,reverse,doublePrecision):

    if reverse:

        if doublePrecision:
            step = float64(-1.0)
        else:
            step = float32(-1.0)

        start = n
    else:
        if doublePrecision:
            step = float64(1.0)
            start = float64(1.0)
        else:
            step = float32(1.0)
            start = float32(1.0)

    if doublePrecision:
        sum = float64(0.0)
    else:
        sum = float32(0.0)

    for i in range(0,50):

        if doublePrecision:
            y = float64(1.0)/np.power(start,s)
        else:
            y = float32(1.0)/np.power(start,s)

        sum = sum + y
        start = start + step

    return sum

def eta(s,n,reverse,doublePrecision):

    if reverse:
        if doublePrecision:
            step = float64(-1.0)
        else:
            step = float32(-1.0)
        start = n
    else:
        if doublePrecision:
            step = float64(1.0)
            start = float64(1.0)
        else:
            step = float32(1.0)
            start = float32(1.0)

    if doublePrecision:
        sum = float64(0.0)
    else:
        sum = float32(0.0)

    for i in range(0,50):

        if(i%2==0):
            if doublePrecision:
                y = -float64(-1.0)/np.power(start,s)
            else:
                y = -float32(-1.0)/np.power(start,s)
        else:
            if doublePrecision:
                y = -float64(1.0)/np.power(start,s)
            else:
                y = -float32(1.0)/np.power(start,s)

        sum = sum + y
        start = start + step

    return sum

sfloat32 = [float32(2.0),float32(3.6667),float32(5.0),float32(7.2),float32(10.0)]
sfloat64 = [float64(2.0),float64(3.6667),float64(5.0),float64(7.2),float64(10.0)]

nfloat32 = [float32(50.0),float32(100.0),float32(200.0),float32(500.0),float32(1000.0)]
nfloat64 = [float64(50.0),float64(100.0),float64(200.0),float64(500.0),float64(1000.0)]

print("ZAD3 DZETA")
for i in range(0,5):
    for j in range(0,5):
        print()
        print("Pojedyncza precyzja s=",sfloat32[i],"n=",nfloat32[j]," : ",dzeta(sfloat32[i],nfloat32[j],False,False))
        print("Pojedyncza precyzja revers s=",sfloat32[i],"n=",nfloat32[j]," : ",dzeta(sfloat32[i],nfloat32[j],True,False))
        print("Podwujna precyzja s=",sfloat64[i],"n=",nfloat64[j]," : ",dzeta(sfloat64[i],nfloat64[j],False,True))
        print("Podwujna precyzja revers s=",sfloat64[i],"n=",nfloat64[j]," : ",dzeta(sfloat64[i],nfloat64[j],False,True))

print("ZAD3 ETA")
for i in range(0,5):
    for j in range(0,5):
        print()
        print("Pojedyncza precyzja s=",sfloat32[i],"n=",nfloat32[j]," : ",eta(sfloat32[i],nfloat32[j],False,False))
        print("Pojedyncza precyzja revers s=",sfloat32[i],"n=",nfloat32[j]," : ",eta(sfloat32[i],nfloat32[j],True,False))
        print("Podwujna precyzja s=",sfloat64[i],"n=",nfloat64[j]," : ",eta(sfloat64[i],nfloat64[j],False,True))
        print("Podwujna precyzja revers s=",sfloat64[i],"n=",nfloat64[j]," : ",eta(sfloat64[i],nfloat64[j],False,True))

# Dla sumowania z reversem dostajemy bledne wyniki,
# bez reversu jest dokladniej,
# ak widac float64 jest dokladniejszy od float32,
# ktrego wynik siega 10^-7, float64 siega do 10^-16

# zad 4
def odwzorowanie(x0,r,n,doublePrecision):

    for i in range(0,n):

        if doublePrecision:
            result = r*x0*(float64(1.0) - x0)
        else:
            result = r*x0*(float32(1.0) - x0)

        x0 = result

    return x0

# 4.A

x = []
y = []

r = float32(1.0)
while r <= float32(4.0):
    xzero = float32(0.0)
    while xzero <= float32(1.0):
        val = odwzorowanie(xzero,r,100,False)
        y.append(val)
        x.append(r)
        xzero = xzero + float32(0.02)
    r = r + float32(0.005)

pyplot.plot(x,y,'ro',markersize=1)
pyplot.axis([1.0, 4.0, 0.0, 1.0])
pyplot.show()

# 4.B
x = []
y = []

r = float64(3.75)
while r <= float64(3.8):
    xzero = float64(0.0)
    while xzero <= float64(1.0):
        val = odwzorowanie(xzero,r,100,True)
        y.append(val)
        x.append(r)
        xzero = xzero + float64(0.02)
    r = r + float64(0.005)


pyplot.plot(x,y,'bo',markersize=1)
pyplot.axis([3.75, 3.8, 0.0, 1.0])
pyplot.show()

x = []
y = []

r = float32(3.75)
while r <= float32(3.8):
    xzero = float32(0.0)
    while xzero <= float32(1.0):
        val = odwzorowanie(xzero,r,100,False)
        y.append(val)
        x.append(r)
        xzero = xzero + float32(0.02)
    r = r + float32(0.005)

pyplot.plot(x,y,'ro',markersize=1)

pyplot.axis([3.75, 3.8, 0.0, 1.0])
pyplot.show()

# 4.C

r = float32(4.0)
delta = 1e-5
n_max = 1000000
x0 = float32(0.0)

print("ZAD 4C\n")

while x0 <= float32(1.0):
    k = x0
    l = 0
    while k > delta and l<n_max:
        result = r*k*(float32(1.0) - k)
        k = result
        l = l + 1
    print("X0=",x0,"liczba iteracji:",l)
    x0 = x0 + float32(0.05)

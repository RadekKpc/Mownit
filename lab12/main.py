import sys
import numpy as np
import matplotlib.pyplot as plt
import math


def runge_kutta_order_4(f, t, x, h, n):

    ta = t
    for j in range(1,n + 1):
        if t != 0:
            k1 = h*f(t,x)
            k2 = h*f(t + 0.5*h, x + 0.5*k1)
            k3 = h*f(t + 0.5*h, x + 0.5*k2)
            k4 = h*f(t + h, x + k3)

            x = x + (1.0 / 6.0 )*(k1 + 2*k2 + 2* k3 + k4)
        t = t + h
    return t,x




# prawidlowe rozwiazanie
x = []
y = []
for i in np.arange(-1,1,0.001):
    x.append(i)
    y.append(i*math.asin(i))
plt.plot(x,y,'bo',markersize=1)
plt.show()

# nasze rozwiazanie
x = []
y = []
t = 0
x0 = 0
for j in np.arange(-1,1,0.01):
    n = (int) (math.fabs((j-t)/(math.pow(2,-7))))
    dz = (math.fabs((j-t)/(math.pow(2,-7))))
    h = (j-t)/dz
    a, b = runge_kutta_order_4( (lambda t,x: x/t + t*(1/math.cos(x/t))) ,t ,x0 ,h ,n)
    x.append(a)
    y.append(b)

plt.plot(x,y,'ro',markersize=1)
plt.show()

# dla t = 1
n = (int) (math.fabs((1-t)/(math.pow(2,-7))))
h = (1-t)/n
print("Wynik z rungego_kutty:")
print(runge_kutta_order_4( (lambda t,x: x/t + t*(1/math.cos(x/t))) ,t ,x0 ,h ,n))
print("Dokładny wynik:")
print(math.asin(1))

# c
for h in [0.015, 0.02, 0.025, 0.03]:
    x = []
    y = []
    t = 0
    x0 = 0
    for j in np.arange(0,3,0.001):
        n = (int) (math.fabs((j-t)/h))
        dz = (math.fabs((j-t)/h))
        if dz != 0:
            h = (j-t)/dz
            a, b = runge_kutta_order_4( (lambda t,x: 100*(math.sin(t) - x)) ,t ,x0 ,h ,n)
            x.append(a)
            y.append(b)

    print("Dla h = ",h)
    plt.plot(x,y,'go',markersize=1)
    plt.show()

# It needs four evaluations of the function f per step. Since it is equivalent to a Taylor series
# method of order 4, it has truncation error of order O(h5). The small number of function
# evaluations and high-order truncation error account for its popularity
#  zad 2

def signum(h):
    if h > 0:
        return 1
    if h < 0:
        return -1

    return 0

def runge_kutta_45(f,t,x,h):
    k1 = h*f(t,x)
    k2 = h*f(t + 0.25*h,x + 0.25*k1)
    k3 = h*f(t + 0.375*h,x + 0.09375*k1 + 0.28125*k2)
    k4 = h*f(t + 12/13*h,x + 1932/2197*k1 - 7200/2197*k2 + 7296/2197*k3)
    k5 = h*f(t + h, x + 439/216*k1 - 8*k2 + 3680/513*k3 - 845/4104*k4)
    k6 = h*f(t + 0.5*h, x + -8/27*k1 + 2*k2 - 3544/2565*k3 + 1859/4104*k4 - 0.275*k5)

    x4 = x + 25/216*k1 + 1408/2565*k3 + 2197/4104*k4 - 0.2*k5
    x = x + 16/135*k1 + 6656/12825*k3 + 28561/56430*k4 - 0.18*k5 + 2/55*k6
    t = t + h
    e = math.fabs(x - x4)
    return x,t,e

a = 1.0
b = 1.5625
h = (b -a)/1000
x = 2.0
t = a
f = lambda t,x : 2.0 + (x - t - 1.0)**2
for k in range(1,1000):
    x,t,e = runge_kutta_45(f,t,x,h)
print(x,t,e)
# 3.19293 7699.
# print("elo")

def adaptive_runge_kutta(f,t,x,h,tb,itmax,emax,emin,hmin,hmax):
    delta = 0.5*0.00001
    iflag = 1
    k = 0
    while k <= itmax:
        k = k + 1
        if math.fabs(h) < hmin:
            h = hmin* signum(h)

        if math.fabs(h) > hmax:
            h = hmax* signum(h)

        d = math.fabs(tb - t)

        if d <= math.fabs(h):
            iflag = 0
            if d <= delta* max(math.fabs(tb),math.fabs(t)):
                break
            h = signum(h)*d

        xsave = x
        tsave = t

        x,t,e = runge_kutta_45(f,t,x,h)
        if iflag == 0:
            break
        if e < emin:
            h = 2*h
        if e > emax:
            h = h/2
            x = xsave
            t = tsave
            k = k -1

    return t,x

X = []
Y = []
a = 0.0
tb = 10.0
x = 0.0
h = 0.01
t = 0.0
itmax = 1000
emax = 0.00001
emin = 0.00000001
hmax = 1.0
hmin = 0.000001
f = lambda t,x: 3 + 5*math.sin(t) + 0.2*x
print(adaptive_runge_kutta(f,a,x,h,tb,itmax,emax,emin,hmin,hmax))


f_direct = lambda x: math.pow(x,3) - (9/2)*math.pow(x,2) + (13/2)*x
print(f_direct(0.5))

# X = []
# Y = []

tb = 0.5
x = 6.0
t = 3.0

h = -0.000000001
itmax = 1000
emax = 0.000000001
emin = 0.0000000001
hmax = 1.0
hmin = 0.000000001
f = lambda t,x: 3*(x/t) + (9/2)*t - 13
print(adaptive_runge_kutta(f,t,x,h,tb,itmax,emax,emin,hmin,hmax))


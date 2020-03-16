import numpy as np
from numpy import float32,power,float64
import matplotlib.pyplot as pyplot
import math
from scipy.interpolate import interp1d
#np.linalg.slove()
#np.vander()
# wzor lagranrza, metoda newtona do interpolacji

# zad 1

def func(x):
    return 1/(1 + x**2)


delta = -5
range_len = 10

for n in [5,10,16]:
    x_point = delta
    y = []
    x = []
    while x_point<=5 :
        x.append(x_point)
        y.append(func(x_point))
        x_point = x_point + range_len/n

    x = np.array(x)
    y = np.array(y)
    van = np.vander(x,n+1,increasing = True)
    a = np.linalg.solve(van,y)
    x_axis = -5
    x_plot = []
    y_plot = []
    y_arx_plot = []
    delta_func = []
    while x_axis <= 5:
        x_plot.append(x_axis)
        y_plot.append(func(x_axis))
        val = 0
        for (i,r) in enumerate(a):
            val = val + r * (x_axis **i)

        y_arx_plot.append(val)
        delta_func.append(func(x_axis) - val)
        x_axis += 0.01
# 1ab
    pyplot.plot(x_plot,y_plot,'bo',markersize=1)
    pyplot.plot(x_plot,y_arx_plot,'ro',markersize=1)
    pyplot.plot(x_plot,delta_func,'yo',markersize=1)
    pyplot.show()

# zad 2

n = 15
start = -5
end = 5
czybyszew_points = []
for k in range(1,n+1):
    czybyszew = 0.5*(start + end) + 0.5*(end - start)*math.cos(((2*k-1)/(2*n))*math.pi)
    czybyszew_points.append(czybyszew)

delta = -5
range_len = 10


y = []
x = []
for (i,c) in enumerate(czybyszew_points):
    x.append(c)
    y.append(func(c))

x = np.array(x)
y = np.array(y)
van = np.vander(x,n,increasing = True)
a = np.linalg.solve(van,y)
x_axis = -5
x_plot = []
y_plot = []
y_arx_plot = []
delta_func = []
while x_axis <= 5:
    x_plot.append(x_axis)
    y_plot.append(func(x_axis))
    val = 0
    for (i,r) in enumerate(a):
        val = val + r * (x_axis **i)

    y_arx_plot.append(val)
    delta_func.append(func(x_axis) - val)
    x_axis += 0.01

pyplot.plot(x_plot,y_plot,'bo',markersize=1)
pyplot.plot(x_plot,y_arx_plot,'ro',markersize=1)
pyplot.plot(x_plot,delta_func,'yo',markersize=1)
pyplot.show()

# zad 3

a = 5
b = 1

def x_func(t):
    return a*math.cos(t)

def y_func(t):
    return b*math.sin(t)

x = []
y = []
t = 0
while t <= 2*math.pi:
    x.append(x_func(t))
    y.append(y_func(t))
    t += 0.01

pyplot.plot(x,y,'bo',markersize=1)
pyplot.show()


def cube_spline_interpolate_elipse(n):
    r = np.linspace(0,2*math.pi,n)
    sx = interp1d(r,list(map(x_func,r)),kind='cubic')
    sy = interp1d(r,list(map(y_func,r)),kind='cubic')
    x = []
    y = []
    for t in np.linspace(0, 2 * np.pi, 1000):
        x.append(sx(t))
        y.append(sy(t))
    pyplot.plot(x,y,'bo',markersize=1)
    pyplot.show()

cube_spline_interpolate_elipse(10)

cube_spline_interpolate_elipse(30)

cube_spline_interpolate_elipse(5)



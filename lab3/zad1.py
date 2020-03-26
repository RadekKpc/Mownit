import math
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
# showing 3d plot
def show_3d_plot(X,Y,Z,label):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.scatter(X, Y, Z, c='b', marker='o',s=1)

    # Create cubic bounding box to simulate equal aspect ratio
    max_range = np.array([np.amax(X)-np.amin(X), np.amax(Y)-np.amin(Y), np.amax(Z)-np.amin(Z)]).max()
    Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(np.amax(X)+np.amin(X))
    Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(np.amax(Y)+np.amin(Y))
    Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(np.amax(Z)+np.amin(Z))
    for xb, yb, zb in zip(Xb, Yb, Zb):
        ax.plot([xb], [yb], [zb], 'w')

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    fig.suptitle(label)
    plt.grid()
    plt.show()

def show_3d_plot_matrix(matrix,axis,label):
    X=[val[0] for val in matrix]
    Y=[val[1] for val in matrix]
    Z=[val[2] for val in matrix]
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.scatter(X, Y, Z, c='b', marker='o',s=1)

    a_x=[val[0] for val in axis]
    a_y=[val[1] for val in axis]
    a_z=[val[2] for val in axis]

    ax.scatter(a_x, a_y, a_z, c='r', marker='o',s=1)

    # Create cubic bounding box to simulate equal aspect ratio
    max_range = np.array([np.amax(X)-np.amin(X), np.amax(Y)-np.amin(Y), np.amax(Z)-np.amin(Z)]).max()
    Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(np.amax(X)+np.amin(X))
    Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(np.amax(Y)+np.amin(Y))
    Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(np.amax(Z)+np.amin(Z))
    # Comment or uncomment following both lines to test the fake bounding box:
    for xb, yb, zb in zip(Xb, Yb, Zb):
        ax.plot([xb], [yb], [zb], 'w')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    fig.suptitle(label)
    plt.grid()
    plt.show()

# 1.1
T = np.arange(0,math.pi,0.1)
S = np.arange(0,2*math.pi,0.05)

X = []
Y = []
Z = []
for i,t in enumerate(T):
    for j,s in enumerate(S):
        X.append(math.sin(t)*math.cos(s))
        Y.append(math.sin(s)*math.sin(t))
        Z.append(math.cos(t))

show_3d_plot(X,Y,Z,'wykres sfery jednostkowej')
sphere_matrix = [list(a) for a in zip(X, Y, Z)]

# 1.2

A1 =  np.array([[2,3,1],[1,1,3],[4,0,1]])
A2 =  np.array([[1,2,1],[0,2,0],[0,2,1]])
A3 =  np.array([[1,0,0.5],[0,1.5,0],[0,0,0.5]])

A = [A1,A2,A3]
ax_x = [[a,0,0] for a in np.arange(-4,4,0.1)]
ax_y = [[0,a,0] for a in np.arange(-4,4,0.1)]
ax_z = [[0,0,a] for a in np.arange(-4,4,0.1)]

elipse_1 = np.matmul(sphere_matrix,A1)
elipse_2 = np.matmul(sphere_matrix,A2)
elipse_3 = np.matmul(sphere_matrix,A3)

E = [elipse_1,elipse_2,elipse_3]

show_3d_plot_matrix(elipse_1,[],"Elipse 1")
show_3d_plot_matrix(elipse_2,[],"Elipse 2")
show_3d_plot_matrix(elipse_3,[],"Elipse 3")

# 1.3

for (i,a) in enumerate(A):
    ax_x = [[a,0,0] for a in np.arange(-4,4,0.1)]
    ax_y = [[0,a,0] for a in np.arange(-4,4,0.1)]
    ax_z = [[0,0,a] for a in np.arange(-4,4,0.1)]

    axis = [ax_x,ax_y,ax_z]
    out = []
    u, s, vh = np.linalg.svd(a)
    u.shape, s.shape, vh.shape
    for os in axis:
        m1 = list(np.matmul(os,np.dot(u * s, vh)))
        out.append(m1)

    show_3d_plot_matrix(list(E[i]),out[0]+out[1]+out[2],'Elipsa '+str(i+1)+' z osiami')

#1.4
# Znajdź taką macierz Ai, aby stosunek jej największej i najmniejszej
# wartości osobliwej był większy od 100. Narysuj odpowiadającą jej elipsoidę.

s = [1,1]
while max(s)/min(s) < 100:
    random_matrix = []
    for a in range(3):
        random_matrix.append([])
        for b in range(3):
            random_matrix[a].append(random.randint(0,5))
    u, s, vh = np.linalg.svd(random_matrix)
    u.shape, s.shape, vh.shape


elipse_4 = list(np.matmul(sphere_matrix,random_matrix))
show_3d_plot_matrix(elipse_4,[],"Macierz z stosunkiem skrajnych wartosci szczegolnych rownym 100")
print(random_matrix)

# 1.5
# dla A1
A1 =  np.array([[2,3,1],[1,1,3],[4,0,1]])
u, s, vh = np.linalg.svd(A1)
u.shape, s.shape, vh.shape
sigma = np.diag(s)
# S*Vt
elipse_5 = np.dot(sphere_matrix,vh)
show_3d_plot_matrix(elipse_5,[],"S*Vt")
# SEVt
elipse_6 = np.dot(sphere_matrix,np.dot(sigma,vh))
show_3d_plot_matrix(elipse_6,[],"S*E*Vt")
# SUEVt
elipse_7 = np.dot(sphere_matrix,np.dot(u,np.dot(sigma,vh)))
show_3d_plot_matrix(elipse_7,[],"S*U*E*Vt")
# S*A1
show_3d_plot_matrix(elipse_1,[],"Elipsa 1")

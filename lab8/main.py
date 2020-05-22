import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
import random
epsilon = 0.0000001
inteartions = 99999

def norm(vec):
    suma = 0
    for i in vec:
        suma += i
    return suma


def power_finding(size,A):
    x0 = np.array([1 for i in range(size)])
    x0 = np.array(x0/norm(x0))
    out = False

    for i in range(inteartions):

        x1 = np.dot(A,x0)
        x2 = x1/norm(x1)

        if np.linalg.norm(x2 - x0) < epsilon:
            out = True
        x0 = x2
        if out:
            break

    return x0/norm(x0)

# zad1

def page_rank(G):
    V = len(G.nodes())
    if(V <= 0):
        return

    A = nx.to_numpy_array(G)
    for e in G.edges():
        n = 0
        for a in A[e[0]]:
            if a > 0:
                n += 1
        A[e[0]][e[1]]/= n

    A = np.transpose(A)
    return power_finding(V,A)

def label_rank(G,rank):
    for i,g in enumerate(G.nodes()):
        G.nodes[i]['rank'] = rank[i]
    return G

def show_graph(G):
    labels = nx.get_node_attributes(G, 'rank')
    for i,e in enumerate(labels):
        labels[i] = round(labels[i],4)


    pos = nx.circular_layout(G)
    nx.draw(G, pos=pos,
    node_size=300, with_labels=True)
    for i,e in enumerate(labels):
        x = pos[i][0]
        y= pos[i][1]
        plt.text(x,y+0.1,s = str(labels[i]),bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
    plt.show()

def get_full_graph(v):
    G = nx.DiGraph()
    G.add_nodes_from([i for i in range(v)],rank = 0)
    for i in range(v):
        for j in range(v):
            G.add_edge(i,j)
    return G

def get_graph(v):
    G = nx.DiGraph()
    G.add_nodes_from([i for i in range(v)],rank = 0)
    for i in range(v):
        for j in range(v):
            G.add_edge(i,j)

    for i in range(8*v):
        x = random.randint(0,v)
        y = random.randint(0,v)
        if (x,y) in G.edges():
            G.remove_edges_from([(x,y)])

    return G

G = nx.DiGraph()
G.add_nodes_from([0,1,2],rank = 0)
G.add_edge(0,1)
G.add_edge(1,2)
G.add_edge(2,0)
G.add_edge(0,2)

rank = page_rank(G)
G = label_rank(G,rank)
print(rank)
show_graph(G)

G = get_full_graph(11)
rank = page_rank(G)
G = label_rank(G,rank)
print(rank)
show_graph(G)

G = get_graph(12)
rank = page_rank(G)
G = label_rank(G,rank)
print(rank)
show_graph(G)

G = get_graph(13)
rank = page_rank(G)
G = label_rank(G,rank)
print(rank)
show_graph(G)

# zadanie 2
def page_rank_2(G,E,d):
    V = len(G.nodes())
    if(V <= 0):
        return

    A = nx.to_numpy_array(G)
    for e in G.edges():
        n = 0
        for a in A[e[0]]:
            if a > 0:
                n += 1
        A[e[0]][e[1]]/= n

    for i,a in enumerate(A):
        for j,b in enumerate(a):
            A[i][j] *= d

    for i,a in enumerate(A):
        for j,b in enumerate(E):
            A[i][j] += (1-d)*E[j]

    A = np.transpose(A)
    return power_finding(V,A)


def open_graph(garph_file):
    G = nx.DiGraph()
    with open(garph_file) as f:
        v, e = [int(x) for x in next(f).split()]
        edges = [[int(x) for x in line.split()] for line in f]

    G.add_nodes_from([i for i in range(v)],rank =0)
    G.add_edges_from(edges)
    return G, v

G = nx.DiGraph()
G.add_nodes_from([0,1,2,3],rank = 0)
G.add_edge(0,1)
G.add_edge(1,2)
G.add_edge(2,0)
G.add_edge(0,2)
G.add_edge(3,2)
v = 4
e = [1/v for i in range(0,v)]
print(e)
rank = page_rank_2(G,e,0.85)
G = label_rank(G,rank)
print(rank)
show_graph(G)

G, v = open_graph('email-Eu-core.txt')
e = [1/v for i in range(0,v)]
rank = page_rank_2(G,e,0.85)

G, v = open_graph('p2p-Gnutella08.txt')
e = [1/v for i in range(0,v)]
rank = page_rank_2(G,e,0.85)
for i,e in enumerate(rank):
    print(f"node: {i} : {e}")
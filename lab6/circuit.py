import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


# https://www.intmath.com/matrices-determinants/6-matrices-linear-equations.php
def show_graph(G):
    # To show arrows
    G = G.to_directed()

    ebunch = []

    for i,e in enumerate(G.edges):
        u, v = e
        if (u,v) not in ebunch and (v,u) not in ebunch:
            ebunch.append((u,v))

    G.remove_edges_from(ebunch)
    pos = nx.planar_layout(G)

    nx.draw_planar(G, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=pos, with_labels=True, font_weight='bold', edge_labels=labels)
    plt.show()


def show_matrix(mat):
    for i in mat:
        for j in i:
            print(j, end=' ')
        print()
    print()


def find_current_kirchhoff(R_load, V_load):
    N = int(max([x[0] for x in R_load] + [x[1] for x in R_load]) + 1)
    K = len(R_load)

    R = nx.Graph()
    R.add_nodes_from([x for x in range(N)])
    for e in R_load:
        R.add_edge(int(e[0]), int(e[1]), weight=e[2])

    direct = [[0 for i in range(N)] for x in range(N)]
    resistance = [[0 for i in range(N)] for x in range(N)]
    voltage = [[0 for i in range(N)] for x in range(N)]
    edges = {}
    equations = []
    m_row = 0
    right_side = []

    # zakladamy ze jak wczytujemy 1 2 8 too prad plynie od 1 do 2 z rezystancja 8

    for i, e in enumerate(R_load):
        direct[int(e[0])][int(e[1])] = 1
        direct[int(e[1])][int(e[0])] = -1
        resistance[int(e[0])][int(e[1])] = e[2]
        resistance[int(e[1])][int(e[0])] = -e[2]
        # Indexing edges
        edges[(e[0], e[1])] = i
        edges[(e[1], e[0])] = i

    for e in V_load:
        voltage[int(e[0])][int(e[1])] = e[2]
        voltage[int(e[1])][int(e[0])] = -e[2]

    # II Kirchoff law
    cycles = nx.cycle_basis(R)

    for cycle in cycles:
        sum_voltage = 0
        equations.append([0 for x in range(K)])
        for i, node in enumerate(cycle):
            node_1 = cycle[i]
            node_2 = cycle[((i + 1) % len(cycle))]
            edge = edges[(node_1, node_2)]
            sum_voltage += voltage[node_1][node_2]
            equations[m_row][edge] = resistance[node_1][node_2]

        m_row += 1
        right_side.append(sum_voltage)

    # I Kirchoff law
    for n, node in enumerate(direct):
        equations.append([0 for x in range(K)])
        right_side.append(0)
        for n2, node_2 in enumerate(node):
            if node_2 != 0:
                equations[m_row][edges[(n, n2)]] = node_2
        m_row += 1

    print("Równania macierzowe")
    show_matrix(equations)
    print("Wektor napieć:")
    print(right_side)

    solution, x, y, z = np.linalg.lstsq(equations, right_side)
    print("Rozwiązanie:")
    print(solution)

    for (a, b) in R.edges:
        R[a][b]['weight'] = round(solution[edges[(a, b)]], 5)

    return R


def open_graph(file_with_resistance, file_with_voltage):
    with open(file_with_resistance) as f:
        w, h = [float(x) for x in next(f).split()]
        R_load = [[float(x) for x in line.split()] for line in f]

    with open(file_with_voltage) as f:
        w, h = [float(x) for x in next(f).split()]
        V_load = [[float(x) for x in line.split()] for line in f]

    return R_load, V_load

#
R, V = open_graph('circuit_resistance.txt', 'curcuit_voltage.txt')
G = find_current_kirchhoff(R, V)
show_graph(G)

R, V = open_graph('cube_resistance.txt', 'cube_voltage.txt')
G = find_current_kirchhoff(R, V)
show_graph(G)

R, V = open_graph('2_random_with_bridge.txt', '2_random_with_bridge_voltage.txt')
G = find_current_kirchhoff(R, V)
show_graph(G)

R, V = open_graph('2d_sieve_resistance.txt', '2d_sieve_voltage.txt')
G = find_current_kirchhoff(R, V)
show_graph(G)
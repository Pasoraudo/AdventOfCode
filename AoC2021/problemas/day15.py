import networkx as nx
from copy import deepcopy
import time

def parte1(data):
    return caminoMasSeguro(data)

def parte2(data):
    aux = deepcopy(data)
    for veces in range(4):
        num = 0
        for line in aux:
            data[num] += [(i + veces) % 9 + 1 for i in line]
            num += 1
    aux = deepcopy(data)
    for veces in range(4):
        for line in aux:
            data.append([(i + veces) % 9 + 1 for i in line])
    return caminoMasSeguro(data)

def caminoMasSeguro(data):
    G = nx.DiGraph()
    rows = len(data)
    cols = len(data[0])
    for x in range(cols):
        for y in range(rows):
            G.add_node((x, y))
    for x in range(cols):
        for y in range(rows):
            if x < cols - 1:
                G.add_weighted_edges_from([((x, y), (x + 1, y), data[y][x + 1])])
            if y < rows - 1:
                G.add_weighted_edges_from([((x, y), (x, y + 1), data[y + 1][x])])
            if x > 0:
                G.add_weighted_edges_from([((x, y), (x - 1, y), data[y][x - 1])])
            if y > 0:
                G.add_weighted_edges_from([((x, y), (x, y - 1), data[y - 1][x])])
    start, end = (0, 0), (cols - 1, rows - 1)
    return nx.dijkstra_path_length(G, source=start, target=end)

def leerDatos():
    with open("./data/day15", 'r') as f:
        data = [[int(i) for i in line] for line in f.read().split('\n')]
    return data

def main():
    data = leerDatos()
    print('Los resultados del dia 15')
    print("Parte 1:", parte1(data))
    print("Parte 2:", parte2(data))

import networkx as nx


def graph_decoder(map):
    grafo = nx.Graph()
    nC = 0
    nF = 0

    for i in map:
        for j in i:
            if j == "#":
                l = []
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        for z in range(-1, 2):
                            l.append(((nF, nC, 0), (nF + x, nC + y, z)))
                grafo.add_edges_from(l)
            nC += 1
        nF += 1
        nC = 0
    #nx.draw(grafo)
    #plt.show()




def main():
    address = "./data/day17"
    file = open(address, "r")
    map = file.read().split("\n")
    file.close()
    G = graph_decoder(map)
    #problems = {1: best_bus, 2: t_time}
    #prob = int(input("¿Problema 1 o 2?\n"))
    #print("El resultado es: ", problems[prob](timestamp, data))

main()
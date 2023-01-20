import Laby_generator_wgrah as lg
import matplotlib.pyplot as plt
import dijkstra as dj
import pyplot_lab 
import sys 
import comparaison as cp

def main():

    n = 95
    sys.setrecursionlimit(20000)

    # dico, graph = lg.Laby_DictLaby_Graph(n,1,n,1)
    # entrance, exit = lg.entrance_exit(n)
    # sol_classique = dj.dijkstra_classic(graph,entrance,exit)
    # sol_bidij = dj.dijkstra_bidirect(graph,entrance,exit)

    # cp.recup_donnees("donnees_dij.txt.txt",sol_classique[2],len(sol_classique[-1]),n,n)
    # cp.recup_donnees("donnees_bidij.txt.txt",sol_bidij[2],len(sol_bidij[3]+sol_bidij[4]),n,n)
    cp.plot_comparaison("donnees_dij.txt.txt","donnees_bidij.txt.txt")
    plt.show()


main()

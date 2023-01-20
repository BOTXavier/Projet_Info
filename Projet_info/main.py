import Laby_generator_wgrah as lg
import matplotlib.pyplot as plt
import dijkstra as dj
import pyplot_lab 
import sys 
import comparaison as cp

def main():

    n = 5
    sys.setrecursionlimit(n**2)
    dico, graph = lg.Laby_DictLaby_Graph(n,1,n,1)
    entrance, exit = lg.entrance_exit(n)
    sol_classique = dj.dijkstra_classic(graph,entrance,exit)

    cp.recup_donnees("C:\Etude\Info\Projet_Info\Projet_Info-1\Projet_info\donnees_dij.txt",sol_classique[2],len(sol_classique[-1]))
    cp.recup_donnees("donnees_bidij.txt",sol_classique[2],len(sol_classique[-1]+sol_classique[-2]))


main()

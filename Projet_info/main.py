import Laby_generator_wgrah as lg
import matplotlib.pyplot as plt
import dijkstra as dj
import pyplot_lab 
import sys 

def main():
    n = 20
    sys.setrecursionlimit(20000) # pour pouvoir ne pas se limiter à n=31
    
    nbCycles=8
    #ATTENTION a utiliser pour test seulement, car crée un nouveau laby
    g,G=lg.Laby_DictLaby_Graph(n,1,nbCycles, 1) #(n,t,nbCycles,w) 
    
    pyplot_lab.plot_laby(G,g) 
    r = dj.dijkstra_classic(G,1,n**2)
    pyplot_lab.plot_soluce(r,n)
    print(f'le chemin le plus court est {r}')
    plt.show()
    

main()

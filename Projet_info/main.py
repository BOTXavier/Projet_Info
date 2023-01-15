import Laby_generator_wgrah as lg
import matplotlib.pyplot as plt
import dijkstra as dj
import pyplot_lab 


def main():
    n = 5
    G = lg.Laby_Graph(n,1,1) 
    g = lg.laby_dict(n,1) 
    pyplot_lab.plot_laby(G,g,lab=False) 
    r = dj.dijkstra_classic(G,1,n**2)
    pyplot_lab.plot_soluce(r,n)
    print(f'le chemin le plus court est {r}')
    plt.show()
    

main()

import Laby_generator_wgrah as lg
import dijkstra as dj
import pyplot_lab 


def main():
    
    pyplot_lab.plot(18,1,1)
    
    G=lg.Laby_Graph(5,1,1)
    r=dj.dijkstra_classic(G,1,24)
    print(f'le chemin le plus court est {r}')

main()

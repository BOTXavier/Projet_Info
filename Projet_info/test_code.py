import dijkstra 
import Laby_generator_wgrah as lg
import pyplot_lab as plt_lab
import matplotlib.pyplot as plt

dico = lg.laby_dict(10, 0)
laby = lg.Laby_Graph(dico, 1)
sol = dijkstra.dijkstra_classic(laby, 1, 100)
plt_lab.plot_laby(laby, dico)
plt_lab.plot_soluce(sol,10)
#plt.show()


coord_visite = plt_lab.graph_to_plot(sol, 10)

import dijkstra 
import Laby_generator_wgrah as lg
import pyplot_lab as plt_lab
import matplotlib.pyplot as plt

dico = lg.laby_dict(10, 0)
laby = lg.Laby_Graph(dico, 1)
sol = dijkstra.dijkstra_bidirect(laby, 1, 100)
entrance, exit = lg.entrance_exit(10)
#plt_lab.plot_laby(laby, dico, entrance, exit)
#plt_lab.plot_soluce(sol,10)
#plt.show()

#visite = sol[2]
#figure = plt.figure()
#plt_lab.coloriage(figure, visite, 10)

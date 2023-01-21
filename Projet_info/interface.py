import pyplot_lab
import Laby_generator_wgrah as lg
import wgraph
import dijkstra as dj
import matplotlib.pyplot as plt 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QSpinBox, QGridLayout
import comparaison as cp
maze = wgraph.laby(None,None,50,None,None,None)

class Fenetre(QWidget):
    def __init__(self,title: str):
        QWidget.__init__(self)
        self.setWindowTitle(str(title))
        # activation du suivi du mouvement de la souris
        self.setMouseTracking(True)

    def closeWindow(self):
        self.close()


class spindemo(QWidget):
   def __init__(self, title: str, parent = None):
      super(spindemo, self).__init__(parent) 
      self.title = title  
      layout = QVBoxLayout()
      self.l1 = QLabel(str(title))
      layout.addWidget(self.l1)
      self.sp = QSpinBox()
      self.sp.setRange(0,60)		
      layout.addWidget(self.sp)
      self.sp.valueChanged.connect(self.valuechange)
      self.setLayout(layout)
            
		
   def valuechange(self):
      self.l1.setText(str(self.title)+ ":" + str(self.sp.value()))


def appui_bouton_gen_laby():
    maze.cote = cote_laby.sp.value()
    maze.cycle = nb_cycle.sp.value()
    maze.dico, maze.Graph = lg.Laby_DictLaby_Graph(maze.cote,1,maze.cycle,1) #(n,t,nbCycles,w)
    maze.entrance, maze.exit = lg.entrance_exit(maze.cote)
    pyplot_lab.plot_laby(maze.Graph,maze.dico,maze.entrance, maze.exit,None,maze.cote, None,None, False, False, "Labyrinthe",None)   
    fen1.closeWindow()
    fen2.show()
    plt.show() 
    
    
def appui_bouton_dijsktra_classique():
    """
    lance l'algo dijkstra classique et l'affiche par dessus le laby
    """
    plt.close()
    maze.bidij = False
    maze.solution = dj.dijkstra_classic(maze.Graph,maze.entrance,maze.exit)
    pyplot_lab.plot_laby(maze.Graph,maze.dico,maze.entrance, maze.exit, maze.solution[0], maze.cote, maze.solution[3],None, True, False,"Solution par dijkstra classique",maze.solution[1]) 
    print("Le temps de calcul pour le dijkstra classique est de :" + str(maze.solution[2]))


def appui_bouton_dijsktra_bidirectionnel():   
    """
    lance l'algo dijkstra bidirectionnel et l'affiche par dessus le laby
    """
    plt.close()
    maze.bidij = True
    maze.solution = dj.dijkstra_bidirect(maze.Graph,maze.entrance,maze.exit)
    pyplot_lab.plot_laby(maze.Graph,maze.dico,maze.entrance, maze.exit, maze.solution[0], maze.cote, maze.solution[3],maze.solution[4], True, False,"Solution par dijkstra bidirectionnel",maze.solution[1])
    print("Le temps de calcul pour le dijkstra bidirectionnel est de :" + str(maze.solution[2]))
    print("Le nombre des cases visitées est :" + str(len(maze.solution[3])))


def appui_bouton_home():
    """
    Retourne à la fenêtre 1 qui permet de générer un labyrinthe
    """
    fen2.closeWindow()
    plt.close()
    fen1.show()


def appui_bouton_afficher_case():
    """
    Affiche les cases parcourues par l'algorithme
    """
    plt.close()
    if maze.bidij:
        x = maze.solution[4]
    else : 
        x = None
    pyplot_lab.plot_laby(maze.Graph,maze.dico,maze.entrance, maze.exit, maze.solution[0], maze.cote, maze.solution[3], x, True, True,"Cases parcourues",maze.solution[1])


def appui_bouton_afficher_graph():
    cp.plot_comparaison("donnees_dij.txt","donnees_bidij.txt")
    plt.show()


app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)

sys.setrecursionlimit(maze.cote**2) # pour pouvoir ne pas se limiter à n=31

#parametrage fenetre home 
fen1 = Fenetre("Home")
cote_laby = spindemo("Côté du labyrinthe")
cote_laby.sp.setRange(1,60)
nb_cycle = spindemo("Nombre de cycles du labyrinthe")
nb_cycle.sp.setRange(0,60**2)
#definition du bouton afficher comparaison algo 
bouton_afficher_graph = QPushButton("Afficher la courbe de comparaison")
bouton_afficher_graph.clicked.connect(appui_bouton_afficher_graph)
bouton_gen_laby = QPushButton("générer un labyrinthe")
bouton_gen_laby.clicked.connect(appui_bouton_gen_laby)

#on organise les differents éléments dans le layout
layout = QGridLayout()
layout.addWidget(cote_laby,0,0)
layout.addWidget(bouton_gen_laby,1,0)
layout.addWidget(nb_cycle,0,1)
layout.addWidget(bouton_afficher_graph,1,1)
fen1.setLayout(layout)
fen1.show()

#parametrage fenetre laby
fen2 = Fenetre("laby")
layout2 = QGridLayout()

# definition du bouton permettant d'utiliser l'algo de dijsktra
bouton_dijsktra_classique = QPushButton("Dijsktra")
bouton_dijsktra_classique.clicked.connect(appui_bouton_dijsktra_classique)
layout2.addWidget(bouton_dijsktra_classique,0,0)

# definition du bouton permettant d'utiliser l'algo de dijsktra bidirectionnel
bouton_dijsktra_bidirectionnel = QPushButton("Dijsktra bidirectionnel")
bouton_dijsktra_bidirectionnel.clicked.connect(appui_bouton_dijsktra_bidirectionnel)
layout2.addWidget(bouton_dijsktra_bidirectionnel,0,1)

# definition du bouton permettant d'afficher les cases
bouton_afficher_case = QPushButton("Afficher les cases parcourues")
bouton_afficher_case.clicked.connect(appui_bouton_afficher_case)
layout2.addWidget(bouton_afficher_case,0,3)

# définition du bouton permettant de retourner au menu
bouton_home = QPushButton("Home")
bouton_home.clicked.connect(appui_bouton_home)
layout2.addWidget(bouton_home,1,0)


fen2.setLayout(layout2)

app.exec_()

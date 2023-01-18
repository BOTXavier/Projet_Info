import pyplot_lab
import Laby_generator_wgrah as lg
import wgraph
import dijkstra as dj
import matplotlib.pyplot as plt 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSpinBox, QGridLayout

maze = wgraph.laby(None,None,None,None)

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
      self.sp.setRange(0,90)		
      layout.addWidget(self.sp)
      self.sp.valueChanged.connect(self.valuechange)
      self.setLayout(layout)
            
		
   def valuechange(self):
      self.l1.setText(str(self.title)+ ":" + str(self.sp.value()))



def appui_bouton_gen_laby():
    maze.cote = cote_laby.sp.value()
    maze.cycle = nb_cycle.sp.value()
    maze.dico, maze.Graph = lg.Laby_DictLaby_Graph(maze.cote,1,1,maze.cycle) #(n,t,w,nbCycles)
    pyplot_lab.plot_laby(maze.Graph,maze.dico,lab=False)   
    fen1.closeWindow()
    fen2.show()
    plt.show() 
    
    
def appui_bouton_dijsktra_classique():
    """
    lance l'algo dijkstra classique et l'affiche par dessus le laby
    """
    plt.close()
    r= dj.dijkstra_classic(maze.Graph,1,maze.cote**2)
    pyplot_lab.plot(maze.Graph,maze.dico,r,maze.cote,"Solution par dijkstra classique")
    #print(f'le chemin le plus court est {r}')
    plt.show()

def appui_bouton_dijsktra_bidirectionnel():   
    """
    lance l'algo dijkstra bidirectionnel et l'affiche par dessus le laby
    """
    plt.close()
    r= dj.dijkstra_bidirect(maze.Graph,1,maze.cote**2)
    pyplot_lab.plot(maze.Graph,maze.dico,r,maze.cote,"Solution par dijkstra bidirectionnel")
    #print(f'le chemin le plus court est {r}')
    plt.show()


def appui_bouton_home():
    """
    Retourne à la fenêtre 1 qui permet de générer un labyrinthe
    """
    fen2.closeWindow()
    plt.close()
    fen1.show()


app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)

sys.setrecursionlimit(20000) # pour pouvoir ne pas se limiter à n=31

#parametrage fenetre home 
fen1 = Fenetre("Home")
cote_laby = spindemo("Côté du labyrinthe")
nb_cycle = spindemo("Nombre de cycles du labyrinthe")
bouton_gen_laby = QPushButton("générer un labyrinthe")
bouton_gen_laby.clicked.connect(appui_bouton_gen_laby)
layout = QGridLayout()
layout.addWidget(cote_laby,0,0)
layout.addWidget(bouton_gen_laby,1,0)
layout.addWidget(nb_cycle,0,1)
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

# définition du bouton permettant de retourner au menu
bouton_home = QPushButton("Home")
bouton_home.clicked.connect(appui_bouton_home)
layout2.addWidget(bouton_home,1,0)


fen2.setLayout(layout2)

app.exec_()

import pyplot_lab
import Laby_generator_wgrah as lg
import dijkstra as dj
import matplotlib.pyplot as plt 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSpinBox


class Fenetre(QWidget):
    def __init__(self,title):
        QWidget.__init__(self)
        self.setWindowTitle(str(title))

        # activation du suivi du mouvement de la souris
        self.setMouseTracking(True)

    def closeWindow(self):
        self.close()


class spindemo(QWidget):
   def __init__(self, title, parent = None):
      super(spindemo, self).__init__(parent)
      
      layout = QVBoxLayout()
      self.l1 = QLabel(str(title))
      layout.addWidget(self.l1)
      self.sp = QSpinBox()
      self.sp.setRange(2,45)
		
      layout.addWidget(self.sp)
      self.sp.valueChanged.connect(self.valuechange)
      self.setLayout(layout)
      self.setWindowTitle("SpinBox demo")
      
		
   def valuechange(self):
      self.l1.setText("côté du labyrinthe:" +str(self.sp.value()))



def appui_bouton_gen_laby():
    global n, G
    n = value.sp.value()
    G = lg.Laby_Graph(n,1,1) 
    g = lg.laby_dict(n,1) 
    pyplot_lab.plot_laby(G,g,lab=False)    
    fen1.closeWindow()
    fen2.show()
    return (G,g,n)
    
    
def appui_bouton_dijsktra():
    global n, G
    r= dj.dijkstra_classic(G,1,n**2)
    print("Le chemin de sortie est :")
    print(r)


def appui_bouton_home():
    fen2.closeWindow()
    plt.close()
    fen1.show()
    
app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)


#parametrage fenetre home 
fen1 = Fenetre("Home")
value = spindemo("côté du labyrinthe")
bouton_gen_laby = QPushButton("générer un labyrinthe")
bouton_gen_laby.clicked.connect(appui_bouton_gen_laby)
layout = QHBoxLayout()
layout.addWidget(value)
layout.addWidget(bouton_gen_laby)

fen1.setLayout(layout)
fen1.show()

#parametrage fenetre laby
fen2 = Fenetre("laby")
bouton_dijsktra = QPushButton("Dijsktra")
bouton_dijsktra.clicked.connect(appui_bouton_dijsktra)
bouton_home = QPushButton("Home")
bouton_home.clicked.connect(appui_bouton_home)
layout2 = QVBoxLayout()
layout3 = QHBoxLayout()
layout3.addWidget(bouton_dijsktra)
layout3.addWidget(bouton_home)


#layout3.addLayout(layout2)
fen2.setLayout(layout3)


app.exec_()
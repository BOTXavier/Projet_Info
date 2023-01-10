import pyplot_lab
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
      self.sp.setRange(2,42)
		
      layout.addWidget(self.sp)
      self.sp.valueChanged.connect(self.valuechange)
      self.setLayout(layout)
      self.setWindowTitle("SpinBox demo")
      
		
   def valuechange(self):
      self.l1.setText("côté du labyrinthe:" +str(self.sp.value()))



def appui_bouton1():
    n = value.sp.value()
    pyplot_lab.plot(n,1,1)
    

    
app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)

fen = Fenetre("Home")
value = spindemo("côté du labyrinthe")

bouton1 = QPushButton("générer un labyrinthe")
bouton1.clicked.connect(appui_bouton1)


layout = QHBoxLayout()
layout.addWidget(bouton1)
layout.addWidget(value)

fen.setLayout(layout)
fen.show()

app.exec_()
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QVBoxLayout
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtCore import Qt, QByteArray
import re


def charger_svg_colore(chemin_fichier, couleur="white"):
    with open(chemin_fichier, "r") as f:
        contenu = f.read()
    
    contenu = re.sub(r'fill="[^"]*"', f'fill="{couleur}"', contenu)
    
    widget = QSvgWidget()
    widget.load(QByteArray(contenu.encode()))
    return widget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IHM")
        self.resize(1920, 1080)
        self.setStyleSheet("background-color: black; color: white; font-size: 30pt;")

        container = QWidget()
        grid = QGridLayout(container)

        for col in range(8):
            grid.setColumnStretch(col, 1)

        for row in range(5):
            grid.setRowStretch(row, 1)

        # Ligne 0
        # Dans ta cellule (par exemple ligne 0, colonne 0)
        sous_layout = QVBoxLayout()

        label_haut = charger_svg_colore("svg/warning0.svg", "yellow")
        label_bas = QLabel("230V")

        label_haut.setFixedSize(100, 100)

        # label_haut.setStyleSheet("font-size: 40pt;")
        label_bas.setStyleSheet("font-size: 50pt;")

        # label_haut.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        label_bas.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        sous_layout.addWidget(label_haut)
        sous_layout.addWidget(label_bas)

        grid.addLayout(sous_layout, 0, 0)

        zone2 = QLabel("Zone 2")
        zone2.setStyleSheet("border: 1px solid white;")
        grid.addWidget(zone2, 1, 7)

        zone3 = QLabel("Zone 3")
        zone3.setStyleSheet("border: 1px solid white;")
        grid.addWidget(zone3, 2, 2)

        # Ligne 1
        zone4 = QLabel("Zone 4")
        zone4.setStyleSheet("border: 1px solid white;")
        grid.addWidget(zone4, 1, 0)

        zone5 = QLabel("Zone 5")
        zone5.setStyleSheet("border: 1px solid white;")
        grid.addWidget(zone5, 1, 1)

        zone6 = QLabel("Zone 6")
        zone6.setStyleSheet("border: 1px solid white;")
        grid.addWidget(zone6, 1, 3)
        ###
        zonea = QLabel("Zone A")
        zonea.setStyleSheet("border: 1px solid white;")
        grid.addWidget(zonea, 1, 4)

        zoneb = QLabel("Zone B")
        zoneb.setStyleSheet("border: 1px solid white;")
        grid.addWidget(zoneb, 1, 5)

        ###
        zone9 = QLabel("Zone 9")
        zone9.setStyleSheet("border: 1px solid white;")
        grid.addWidget(zone9, 4, 7)

        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import readText
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from ui import wmain

def mainWindow():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(50, 50, 200, 200)
    win.setWindowTitle("Main")
    label= QtWidgets.QLabel(win)
    label.setText("Wtf")
    label.move(10,10)
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Beve = QtWidgets.QMainWindow()
    ui = wmain.Ui_Beve()
    ui.setupUi(Beve)
    Beve.show()
    sys.exit(app.exec_())
                                                                                                                
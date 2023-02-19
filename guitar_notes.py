import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsView
from PyQt6.QtGui import QPainter, QBrush, QPen
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsEllipseItem

class GuitarNotes(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window properties
        self.setWindowTitle('Guitar Notes')
        self.setGeometry(100, 100, 800, 600)

        # Create the guitar neck graphics view
        self.view = QGraphicsView(self)
        self.view.setGeometry(50, 50, 700, 400)

        # Create the guitar neck graphics scene
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 700, 400)

        # Add the guitar neck circles to the scene
        for i in range(6):
            y = (i + 1) * 50
            for j in range(12):
                x = j * 50 + 50
                self.scene.addItem(QGraphicsEllipseItem(x, y, 30, 30))

        # Set the scene for the view
        self.view.setScene(self.scene)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GuitarNotes()
    window.show()
    sys.exit(app.exec())

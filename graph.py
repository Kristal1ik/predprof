import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget


class Canvas(FigureCanvas):
    def __init__(self, parent, x, y):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)
        self.x = [1, 2, 3]
        self.y = [1, 2, 3]
        self.ax.plot(self.x, self.y)
        self.ax.set(xlabel='время (с)', ylabel='угол, \u00B0',
                    title='График заезда')
        self.ax.grid()


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600, 800)
        chart = Canvas(self)


app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())

#   Links followed to make this work
# [ install python using choco / conda ]
# https://stackoverflow.com/questions/67696427/no-module-named-pyqt5-qtchart

import sys
import time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt DonutChart")
        self.setGeometry(100, 100, 680, 500)

        self.create_donut_chart()

        self.show()
        
        time.sleep(1)
        self.chart.series()[0].slices()[0].setValue(25.5)

        # print(self.chart.series()[0].slices()[0].value())

    def create_donut_chart(self):
        self.series = QPieSeries()
        self.series.setHoleSize(0.35)
        self.series.append("Protein 4.28", 4.26)
        slice = QPieSlice()
        slice = self.series.append("Fat 15.6%", 15.6)
        slice.setExploded()
        slice.setLabelVisible()

        self.series.append("Other 23.8", 23.8)
        self.series.append("Carbs", 56.4)

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("DonutChart Example")

        chartview = QChartView(self.chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
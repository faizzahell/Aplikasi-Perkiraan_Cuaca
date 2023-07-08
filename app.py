import sys
from PySide6 import QtCore, QtGui, QtWidgets
from src.MainWindow import Ui_MainWindow
from function import function

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    closed = QtCore.Signal()

    def __init__(self, *args, **kwarg) -> None:
        super(MainWindow, self).__init__(*args, **kwarg)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_update)

    def get_update(self):
        city_name = self.lineEdit.text()
        tempratureCelcius, weatherTranslate, humidity, windSpeed = function.getWeather(city_name)
        self.label_3.setText(str(weatherTranslate).upper())
        self.label_4.setText(str(tempratureCelcius))
        self.label_5.setText(str(humidity))
        self.label_6.setText(str(windSpeed))

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.close.emit()
        return super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

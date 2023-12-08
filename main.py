from PyQt6 import QtWidgets
from logic import *


def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main()



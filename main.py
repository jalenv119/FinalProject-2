<<<<<<< 
from PyQt6 import QtWidgets
from gui import Ui_MainWindow
from logic import LogicController

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main_window = Ui_MainWindow()
    main_window.show()
    logic_controller = LogicController()

    # Connect button signals to methods in the MainWindow class
    for button in main_window.centralwidget.findChildren(QtWidgets.QPushButton):
        if button.text().isdigit() or button.text() in {'+', '-', '*', '/'}:
            button.clicked.connect(main_window.on_button_clicked)

    main_window.ClearButton.clicked.connect(main_window.clear_text)
    main_window.SubmitButton.clicked.connect(main_window.submit_expression)

    sys.exit(app.exec())
=======




























if __name__ == __main__:
  main()
>>>>>>> refs/remotes/origin/main

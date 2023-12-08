from PyQt6.QtWidgets import *
from gui import Ui_MainWindow

class Logic(QMainWindow, Ui_MainWindow):
    pressed_buttons = []
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_text = ''

        self.Number0Button.clicked.connect(self.on_button_clicked)
        self.Number1Button.clicked.connect(self.on_button_clicked)
        self.Number2Button.clicked.connect(self.on_button_clicked)
        self.Number3Button.clicked.connect(self.on_button_clicked)
        self.Number4Button.clicked.connect(self.on_button_clicked)
        self.Number5Button.clicked.connect(self.on_button_clicked)
        self.Number6Button.clicked.connect(self.on_button_clicked)
        self.Number7Button.clicked.connect(self.on_button_clicked)
        self.Number8Button.clicked.connect(self.on_button_clicked)
        self.Number9Button.clicked.connect(self.on_button_clicked)
        self.AdditionButton.clicked.connect(self.on_button_clicked)
        self.SubtractButton.clicked.connect(self.on_button_clicked)
        self.MultiplyButton.clicked.connect(self.on_button_clicked)
        self.DivideButton.clicked.connect(self.on_button_clicked)
        self.ClearButton.clicked.connect(self.on_button_clicked)
        self.SubmitButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        button = self.sender()
        button_text = button.text()

        if button_text == "CLEAR":
            self.clear_text()
        elif button_text == "SUBMIT":
            self.evaluate_expression()
        else:            
            self.pressed_buttons.append(button_text)
            self.update_text()

    def clear_text(self):
        self.pressed_buttons = []
        self.update_text()

    def evaluate_expression(self):
        try:
            expression = "".join(self.pressed_buttons)
            result = eval(expression)
            self.textEdit.clear()
            self.textEdit.setPlainText(f'{result:.2f}')
            self.textEdit.setFocus()
            self.pressed_buttons = [str(result)]  # Store the result as a string
        except Exception as e:
            self.textEdit.setPlainText(str(e))
            self.pressed_buttons = []

    def update_text(self):
        self.textEdit.setPlainText(" ".join(self.pressed_buttons))

    def add(self, values):
        neg_sum = 0
        for num in values:
            if num < 0:
                neg_sum += num
        return neg_sum

    def subtract(self, values):
        pos_diff = None
        for num in values:
            if num > 0:
                if pos_diff is None:
                    pos_diff = num
                else:
                    pos_diff -= num
        if pos_diff is None:
            return 0
        return pos_diff

    def multiply(self, values):
        multi_sum = 1
        no_zeros = False
        for num in values:
            if num != 0:
                multi_sum *= num
                no_zeros = True
        if not no_zeros:
            return 0
        return multi_sum

    def divide(self, values):
        divi_sum = 1
        zeros = 0

        for num in values:
            if num == 0:
                zeros += 1
                if zeros > 1:
                    print('Cannot divide by 0')
                    raise ValueError('Cannot divide by 0') 
            else:
                divi_sum /= num

        if zeros == 1:
            return 0
        return divi_sum
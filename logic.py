from PyQt6 import QtWidgets
from gui import Ui_MainWindow

class Calc:
    def add(values):
        neg_sum = 0
        for num in values:
            if num < 0:
                neg_sum += num
        return neg_sum

    def subtract(values):
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

    def multiply(values):
        multi_sum = 1
        no_zeros = False
        for num in values:
            if num != 0:
                multi_sum *= num
                no_zeros = True
        if not no_zeros:
            return 0
        return multi_sum

    def divide(values):
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

class LogicController:
    def __init__(self, ui):
        self.ui = ui

    def process_input(self, args):
        num_arg = len(args)
        values = []

        if num_arg <= 1 or num_arg <= 3:
            self.show_error('Invalid input.')
            return

        op = args[1]
        if op not in ('add', 'subtract', 'multiply', 'divide'):
            self.show_error('Valid operator names (add, subtract, multiply, divide)')
            return

        for arg in args[2:]:
            try:
                value = float(arg)
                values.append(value)
            except ValueError:
                self.show_error('Invalid input.')
                return

        result = getattr(Calc, op)(values)
        expression = ' '.join(args[2:])
        self.ui.textEdit.setPlainText(f'{expression} = {result:.2f}')

    def show_error(self, message):
        QtWidgets.QMessageBox.critical(None, "Error", message)

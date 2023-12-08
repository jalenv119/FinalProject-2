from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_text = ''


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

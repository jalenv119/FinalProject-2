import formulas 
import sys

class Claculator:
    def __iniit__(self, op, values):
        self.op = op
        self.values = values
    def celcuatlate(self):
        operators = {'add' : formulas.add, 'subtract': formulas.subtract,
                     'multiply': formulas.multiply, 'divide' : formulas.divide,
                     'modulo': formulas.modulo                                          
                     }

def main():
    num_arg = len(sys.argv)

    if num_arg <= 1:
        print('Need to provide operator.')
        sys.exit(1)
    elif num_arg <= 3:
        print('Need to provide at least two values.')
        sys.exit(1)
    elif num_arg > 3:

        op = sys.argv[1]
        if op not in ('add' , 'subtract' , 'multiply', 'divide'):
            print('Valid operator names (add, subtract, multiply, divide)')
            sys.exit(1)
    values = []



    for arg in sys.argv[2:]:
        try:
            value = float(arg)
            values.append(value)
        except ValueError:
            sys.exit(1)
            
       
        if op == 'add':
            result = formulas.add(values)
        elif op == 'subtract':
            result = formulas.subtract(values)
        elif op == 'multiply':
            result = formulas.multiply(values)
        elif op == 'divide':
            result = formulas.divide(values)

    calculator = Claculator(op, values)
    result = calculator.calculate()

    print(f'Answer = {result:.2f}')

       










if __name__ == '__main__':
    main()




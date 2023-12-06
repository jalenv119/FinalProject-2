import formulas 
import sys
import gui

num_arg = len(sys.argv)
values = []

def main():
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

        print(f'Answer = {result:.2f}')

       










if __name__ == '__main__':
    main()



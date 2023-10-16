import argparse
from operator import add, sub, mul, truediv
from functools import reduce

def calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    if not numbers:
        raise SystemExit #these line check if numbers list is empty, and if it is, the program is exited

    operator = {'add': add,
                'sub': sub,
                'mul': mul,
                'div': truediv,
                } #operator is a dictionary that maps operation names to the function from operator module

    return round(reduce(operator[operation], map(float, numbers)), 2) #'reduce' is from functools and applies selected operation to the list of numbers
#operator[operation]: It selects the appropriate operator function based on the provided operation
#map(float, numbers): This part converts each element in the numbers list to a float. 
#reduce(...): The reduce function takes the selected operator function and the list of numbers as arguments and applies the operation cumulatively. 
# For example, if you have a list [2.0, 3.0, 4.0] and the operation is 'add', it calculates 2.0 + 3.0 = 5.0, and then '5.0 + 4.0 = 9.0'.
#the round function is used to round the result of the operation to two decimal places. 

def create_parser():
    parser = argparse.ArgumentParser('A simple calculator') #This line creates an ArgumentParser object named parser and provides a brief description ('A simple calculator') for the parser, which will be displayed when you request help or when you make a mistake in using the command line.
    parser.add_argument('-a', '--add', nargs='*', help='Sums numbers') 
    parser.add_argument('-s', '--sub', nargs='*', help='Subtracts numbers')
    parser.add_argument('-m', '--mul', nargs='*', help='Multiplies numbers')
    parser.add_argument('-d', '--div', nargs='*', help='Divides numbers')

#-a and --add are the short and long argument names, respectively. Users can specify the operation as either -a or --add.
#nargs='*' allows users to provide zero or more values for this argument. These values will be treated as the numbers to be added together.
#help='Sums numbers' provides a brief description of what this argument does, which will be displayed in the help message.
    return parser


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    call_calculator(stdout=True)
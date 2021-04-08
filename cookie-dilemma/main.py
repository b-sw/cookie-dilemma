"""
    Name: main.py
    Purpose: main module

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from test_package.optimize import test_optimize
import sys

ARGC = 7


def main():
    argv = sys.argv[1:]
    """
        0 - seed
        1 - population size
        2 - offspring size
        3 - k value for k-iterations criterion
        4 - dimensionality
        5 - # of runs
        6 - element of [ga, es], Genetic Algorithm or Evolutionary Strategy
    """
    if len(argv) == ARGC:  # Linux OS

        test_optimize(argv)

    else:  # Windows OS

        argv = [100, 20, 20 * 7, 5, 20, 3, 'es']
        # argv = [100, 200, 200, 5, 20, 3, 'ga']
        test_optimize(argv)


if __name__ == '__main__':
    main()

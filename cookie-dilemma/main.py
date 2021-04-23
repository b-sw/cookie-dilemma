"""
    Name: main.py
    Purpose: main module

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from test_package.optimize import test_optimize
import sys

ARGC = 5


def main():
    argv = sys.argv[1:]

    if len(argv) == ARGC:  # Linux OS
        """
            0 - 'es'
            1 - seed
            2 - dimensionality
            3 - # of runs
            4 - k value for k-iterations criterion
        """
        test_optimize(argv)

    else:  # Windows OS

        # argv = ['es', '100', '80', '25', '5']
        argv = ['ga', '100', '5', '25', '5']
        test_optimize(argv)


if __name__ == '__main__':
    main()

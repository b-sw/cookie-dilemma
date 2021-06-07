"""
    Name: main.py
    Purpose: main module

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from test_package.optimize import test_optimize
from test_package.mip import test_mip
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

        # argv = ['es', '100', '10', '10', '5']
        # argv = ['es', '100', '80', '10', '5']
        # test_optimize(argv)
        test_mip()


if __name__ == '__main__':
    main()

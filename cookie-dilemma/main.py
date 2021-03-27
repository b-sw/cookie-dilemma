"""
    Name: main.py
    Purpose: main module

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.optimize import *
from package.eval_func import *


def main():
    eval_func = ObjectiveValue([1, 2, 5, 3, 4, 9, 8, 2, 6, 7])

    storage = run_multiple(eval_func, optimize_by_es)


if __name__ == '__main__':
    main()

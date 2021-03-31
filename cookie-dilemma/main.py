"""
    Name: main.py
    Purpose: main module

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.eval_func import *
from test.eval_func import test_eval
import numpy as np


def main():
    test_eval()
    # eval_func = ObjectiveValue([1, 2, 5, 3, 4, 9, 8, 2, 6, 7])
    # rand_list = np.random.randint(1, high=11, size=50)
    # print(rand_list)
    # eval_func = ObjectiveValue(rand_list)
    #
    # storage = run_multiple(eval_func, optimize_by_es)


if __name__ == '__main__':
    main()

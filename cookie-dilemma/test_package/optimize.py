"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from eval_func import ObjectiveValue
from package.optimize import *


def test_optimize(argv):
    set_params(argv)

    rand_list = np.random.randint(1, high=11, size=PARAMS['dims'])
    print('Grades: {}'.format(rand_list))
    eval_func = ObjectiveValue(rand_list)
    storage = run_multiple(eval_func, optimize, PARAMS['algorithm'])

    print('Mean best score: {}'.format(storage.mean()))

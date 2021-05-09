"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.eval_func import ObjectiveValue
from package.mip import mip_optimize
from package.optimize import *


def test_optimize(argv):
    set_params(argv)

    rand_list = np.random.randint(1, high=11, size=PARAMS['dims'])
    print('Grades: {}'.format(rand_list))
    eval_func = ObjectiveValue(rand_list)

    print('Testing algorithm {} and dims={}..'.format(argv[0], argv[2]))
    optimal_solution = mip_optimize(rand_list)
    scores = run_multiple(eval_func)
    print('Done testing algorithm {} and dims={}'.format(argv[0], argv[2]))

    output = [optimal_solution, min(scores), round(sum(scores)/len(scores), 2), round(float(np.std(scores)), 2)]
    # print('fits: {}\nbest fit: {}\nexpected fit: {}\nstandard deviation: {}'
    #       .format(scores, output[0], output[1], output[2]))

    np.savetxt('output/' + argv[0] + str(argv[2]) + ".csv", output, delimiter=";", fmt='%s')

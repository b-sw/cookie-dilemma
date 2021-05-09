"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.visuals import print_loading_bar
from package.population import *
from package.genetic_algorithm import *
from package.evolutionary_strategy import *

PARAMS = {}
TMP_FLAG = 1


def set_params(argv):
    global PARAMS

    for i in range(1, len(argv)):
        argv[i] = int(argv[i])

    np.random.seed(argv[1])
    random.seed(argv[1])

    PARAMS['dims'] = argv[2]
    PARAMS['runs'] = argv[3]
    PARAMS['k-iter'] = argv[4]
    PARAMS['budget'] = argv[2] * 1000

    if argv[0] == 'es':
        PARAMS['algorithm'] = EvolutionaryStrategy
        PARAMS['population_size'] = 20
        PARAMS['offspring'] = PARAMS['population_size'] * 7
    elif argv[0] == 'ga':
        PARAMS['algorithm'] = GeneticAlgorithm
        PARAMS['population_size'] = PARAMS['dims'] * 10
        PARAMS['offspring'] = PARAMS['population_size']


def run_multiple(eval_func):
    best_evals = []
    for i in range(PARAMS['runs']):
        # print('Run #{}'.format(i + 1))
        print_loading_bar(i, PARAMS['runs'])
        best_eval = run_whole_budget(eval_func)
        best_evals.append(best_eval)
        # print('Best eval in run ' + str(i + 1) + ': {}'.format(best_eval))

    print_loading_bar(PARAMS['runs'], PARAMS['runs'])

    return best_evals


def run_whole_budget(eval_func):
    global TMP_FLAG
    budget = PARAMS['budget']
    best_evals = []

    # while there is still budget for at least single generation
    while budget - (PARAMS['population_size'] + PARAMS['offspring']) > 0:
        best_fit, _, evals, _, best_fits, expected_fits, generation_evals = optimize(eval_func, budget)

        # if TMP_FLAG == 1:
        #     plot_single_run_properties([generation_evals, expected_fits], PARAMS['algorithm'])
        #     plot_single_run_properties([generation_evals, best_fits], PARAMS['algorithm'])
        #     TMP_FLAG = 0

        budget -= evals
        best_evals.append(best_fit)

    return min(best_evals)


def optimize(eval_func, budget):
    population = Population.rand_population(PARAMS['population_size'], eval_func)
    evals = PARAMS['population_size']

    k_best_fit = population.members[BEST_MEMBER].fitness
    k_best_gen = population.generation

    best_fits = []
    expected_fits = []
    generation_evals = []

    while evals + PARAMS['offspring'] < budget \
            and not k_iterations_criterion(k_best_fit, k_best_gen, PARAMS['k-iter'], population):

        best_fits.append(population.members[BEST_MEMBER].fitness)
        expected_fits.append(sum(member.fitness for member in population.members) / PARAMS['population_size'])
        generation_evals.append(evals + PARAMS['offspring'])

        evolve(population, eval_func, PARAMS['algorithm'])
        evals += PARAMS['offspring']

        if population.members[BEST_MEMBER].fitness < k_best_fit:
            k_best_fit = population.members[BEST_MEMBER].fitness
            k_best_gen = population.generation

    # print("optimize| number of evals done before criterion: {}".format(evals))

    return [k_best_fit, k_best_gen, evals, population, best_fits, expected_fits, generation_evals]


def k_iterations_criterion(k_best_fit, k_best_gen, k_value, population):
    if population.generation - k_best_gen >= k_value and k_best_fit <= population.members[BEST_MEMBER].fitness:
        return True
    else:
        return False

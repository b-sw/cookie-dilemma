"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.data_storing import SingleRunStorage, MultipleRunStorage
from package.population import *
from package.genetic_algorithm import *
from package.evolutionary_strategy import *

PARAMS = {}


def set_params(argv):
    global PARAMS

    for i in range(0, len(argv) - 1):
        argv[i] = int(argv[i])
        print(argv[i])

    np.random.seed(argv[0])
    random.seed(argv[0])

    PARAMS['population_size'] = argv[1]
    PARAMS['offspring'] = argv[2]
    PARAMS['k-iter'] = argv[3]
    PARAMS['dims'] = argv[4]
    PARAMS['budget'] = argv[4] * 1000
    PARAMS['runs'] = argv[5]

    if argv[6] == 'es':
        PARAMS['algorithm'] = EvolutionaryStrategy
    elif argv[6] == 'ga':
        PARAMS['algorithm'] = GeneticAlgorithm


def run_multiple(eval_func, optimization_algorithm, strategy):
    multiple_storage = MultipleRunStorage()
    for i in range(PARAMS['runs']):
        print('Run #{}'.format(i + 1))
        single_storage = run_whole_budget(eval_func, optimization_algorithm, strategy)
        best_eval_in_run = single_storage.best_eval_overall
        multiple_storage.best_evals.append(best_eval_in_run)
        print('Best eval in run ' + str(i) + ': {}'.format(best_eval_in_run))

    return multiple_storage


def run_whole_budget(eval_func, optimization_algorithm, strategy):
    budget = PARAMS['budget']
    storage = SingleRunStorage()

    # while there is still budget for at least single generation
    while budget - (PARAMS['population_size'] + PARAMS['offspring']) > 0:
        best_evals, number_of_evals, population = optimization_algorithm(eval_func, strategy, budget)
        budget -= number_of_evals
        storage.add_eval(best_evals[-1])

        # print("best eval: {} | rule fitness: {}".format(best_evals[-1], population.members[BEST_MEMBER].rule_fitness))

    return storage


def optimize(eval_func,  strategy, budget):
    population = Population.rand_population(PARAMS['population_size'], eval_func)

    best_evals = []
    number_of_evals = PARAMS['population_size']

    k_best_fit = population.members[BEST_MEMBER].fitness
    k_best_gen = population.generation

    while number_of_evals + PARAMS['offspring'] < budget \
            and not k_iterations_criterion(k_best_fit, k_best_gen, PARAMS['k-iter'], population):
        best_evals.append(population.members[BEST_MEMBER].fitness)

        evolve(population, eval_func, strategy)
        number_of_evals += PARAMS['offspring']

        if population.members[BEST_MEMBER].fitness < k_best_fit:
            k_best_fit = population.members[BEST_MEMBER].fitness
            k_best_gen = population.generation

        # print("{} best eval: {} | rule penalty: {}".format(population.members[BEST_MEMBER].chromosome,
        #                                                    population.members[BEST_MEMBER].fitness,
        #                                                    population.members[BEST_MEMBER].rule_fitness))

    print("optimize| number of evals done before criterion: {}".format(number_of_evals))

    return [best_evals, number_of_evals, population]


def k_iterations_criterion(k_best_fit, k_best_gen, k_value, population):
    if population.generation - k_best_gen >= k_value and k_best_fit <= population.members[BEST_MEMBER].fitness:
        return True
    else:
        return False

"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from data_storing import SingleRunStorage, MultipleRunStorage
from population import *
from evolutionary_strategy import *

BUDGET = 1000 * 10
K_ITERATIONS = 5
RUNS = 25


def run_multiple(eval_func, optimization_algorithm):
    multiple_storage = MultipleRunStorage()
    for _ in range(RUNS):
        single_storage = run_whole_budget(eval_func, optimization_algorithm)
        best_eval_in_run = single_storage.best_eval_overall
        multiple_storage.best_evals.append(best_eval_in_run)

    return multiple_storage


def run_whole_budget(eval_func, optimization_algorithm):
    budget = BUDGET
    storage = SingleRunStorage()
    while budget - (MU + LAMBDA) > 0:  # while there is still budget for at least single generation
        best_evals, number_of_evals, population = optimization_algorithm(eval_func, budget)
        budget -= number_of_evals
        storage.add_eval([best_evals[-1], population.members[BEST_MEMBER].rule_fitness])

        print("best eval: {} | rule fitness: {}".format(best_evals[-1], population.members[BEST_MEMBER].rule_fitness))

    return storage


def optimize_by_es(eval_func, budget=BUDGET):
    population = Population.rand_population(MU, eval_func)

    best_evals = []
    number_of_evals = MU

    k_best_fit = population.members[BEST_MEMBER].fitness
    k_best_gen = population.generation

    while number_of_evals + LAMBDA < budget \
            and not k_iterations_criterion(k_best_fit, k_best_gen, K_ITERATIONS, population):
        best_evals.append(population.members[BEST_MEMBER].fitness)

        evolve(population, eval_func, EvolutionaryStrategy)

        number_of_evals += LAMBDA

        if population.members[BEST_MEMBER].fitness < k_best_fit:
            k_best_fit = population.members[BEST_MEMBER].fitness
            k_best_gen = population.generation

        # print("{} best eval: {} | rule penalty: {}".format(population.members[BEST_MEMBER].chromosome,
        #                                                    population.members[BEST_MEMBER].fitness,
        #                                                    population.members[BEST_MEMBER].rule_fitness))

    print("optimize_by_es| number of evals done before criterion: {}".format(number_of_evals))

    return [best_evals, number_of_evals, population]


def k_iterations_criterion(k_best_fit, k_best_gen, k_value, population):
    if population.generation - k_best_gen >= k_value and k_best_fit <= population.members[BEST_MEMBER].fitness:
        return True
    else:
        return False

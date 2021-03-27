"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from genotype import Genotype
import random

BOUND_LOWER = 1
BOUND_UPPER = 10
BEST_MEMBER = 0


def evolve(population, eval_func, algorithm):
    selection = algorithm.select(population)
    offspring = algorithm.mate(selection)
    offspring = algorithm.mutate(offspring, eval_func)
    population.members = algorithm.succeed(population, offspring)

    population.generation += 1


class Population:
    generation = 1

    def __init__(self, members):
        self.members = members

    @classmethod
    def rand_population(cls, size, eval_func):
        members = []

        for i in range(size):
            x = [random.randint(BOUND_LOWER,BOUND_UPPER) for x in range(len(eval_func.grades))]
            fitness = eval_func.evaluate(x)
            genotype = Genotype(x, fitness, size)
            members.append(genotype)

        members = sorted(members, key=lambda m: m.fitness)

        return cls(members)

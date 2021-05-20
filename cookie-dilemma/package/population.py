"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.genotype import Genotype
import random

BOUND_LOWER = 1
BOUND_UPPER = 3
BEST_MEMBER = 0


def evolve(population, eval_func, algorithm):
    selection = algorithm.select(population)
    offspring = algorithm.mate(selection)
    offspring = algorithm.mutate(offspring, eval_func)
    population.members = algorithm.succeed(population, offspring)
    # print(len(population.members))

    population.generation += 1
    # print('Chromosome: {} | fitness: {}'.format(population.members[0].chromosome, population.members[0].fitness))
    # print('Chromosome: {} | fitness: {}'.format(population.members[1].chromosome, population.members[1].fitness))
    # print('Chromosome: {} | fitness: {}'.format(population.members[2].chromosome, population.members[2].fitness))
    # print('Chromosome: {} | fitness: {}'.format(population.members[-1].chromosome, population.members[-1].fitness))
    # print('\n')
    # if population.generation % 100 == 0:
    #     print('Generation: {}'.format(population.generation))


class Population:
    generation = 1

    def __init__(self, members):
        self.members = members

    @classmethod
    def rand_population(cls, size, eval_func):
        members = []

        for i in range(size):
            x = [random.randint(BOUND_LOWER, BOUND_UPPER) for x in range(len(eval_func.grades))]
            fitness = eval_func.evaluate(x)
            genotype = Genotype(x, fitness, size)
            members.append(genotype)

        members = sorted(members, key=lambda m: m.fitness)

        return cls(members)

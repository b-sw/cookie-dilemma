"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import random
import numpy as np
from package.genotype import Genotype

MU = 20
LAMBDA = 7 * MU


class EvolutionaryStrategy:
    @staticmethod
    def select(population):
        parents = []
        for _ in range(LAMBDA):
            parents.append(random.choice(population.members))

        return parents

    @staticmethod
    def mate(parents):
        children_genotypes = []
        dims = len(parents[0].chromosome)
        # average with random weight
        for _ in parents:
            chromosome = []
            parent_1 = random.choice(parents)
            parent_2 = random.choice(parents)
            weight = random.uniform(0, 1)

            for i in range(dims):
                chromosome.append(round(weight * parent_1.chromosome[i] + (1 - weight) * parent_2.chromosome[i]))

            genotype = Genotype(chromosome, 0, dims)
            children_genotypes.append(genotype)

        return children_genotypes

    @staticmethod
    def mutate(offspring, eval_func):
        dims = len(offspring[0].chromosome)

        for i in range(len(offspring)):
            for j in range(dims):
                x_j = offspring[i].chromosome[j]
                sigma_j = offspring[i].sigmas[j]
                x_j += (sigma_j * np.random.normal(0, 1))

                # for now boundaries check
                if x_j < 1:
                    x_j = 1
                elif x_j > 10:
                    x_j = 10

                offspring[i].chromosome[j] = round(x_j)

            eval_value = eval_func.evaluate(offspring[i].chromosome)
            # rule_penalty_points = eval_func.rule_penalty_points

            offspring[i].fitness = eval_value
            # offspring[i].rule_fitness = rule_penalty_points

        return offspring

    @staticmethod
    def succeed(population, offspring):
        next_generation = population.members + offspring
        next_generation = sorted(next_generation, key=lambda m: m.fitness)

        return next_generation[:MU]

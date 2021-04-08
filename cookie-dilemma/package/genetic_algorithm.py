"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import random

import numpy as np

from genotype import Genotype

H = 0  # number of generation members = 10 * DIM (set up at select method)
PROB_CROSS = 0.7
PROB_MUT = 0.1


class GeneticAlgorithm:
    @staticmethod
    def select(population):
        global H
        H = len(population.members)

        q_sum = 0
        for member in population.members:
            q_sum += member.fitness
        parents = []
        h = 0

        while h < H:
            rand_member = random.choice(population.members)
            p = random.uniform(0, 1)
            p_s = 1 - rand_member.fitness / q_sum
            if p <= p_s:
                parents.append(rand_member)
                h += 1

        return parents

    @staticmethod
    def mate(parents):
        children_genotypes = []
        dims = len(parents[0].chromosome)

        i = 0
        while i < H:
            p_c = random.uniform(0, 1)

            if p_c <= PROB_CROSS and i < H - 1:
                parents = random.sample(parents, 2)
                rand_cut = random.randint(1, dims - 1)

                chromosomes = [parents[0].chromosome[:rand_cut] + parents[1].chromosome[rand_cut:],
                               parents[1].chromosome[:rand_cut] + parents[0].chromosome[rand_cut:]]

                children = [Genotype(chromosomes[0], 0, dims),
                            Genotype(chromosomes[1], 0, dims)]

                children_genotypes += children
                i += 2

            else:
                children_genotypes.append(random.choice(parents))
                i += 1

        return children_genotypes

    @staticmethod
    def mutate(offspring, eval_func):
        dims = len(offspring[0].chromosome)

        for i in range(len(offspring)):
            p_m = random.uniform(0, 1)

            if p_m <= PROB_MUT:
                for j in range(dims):
                    gene = offspring[i].chromosome[j]
                    gene = round(gene + np.random.normal(0, 1))

                    # boundaries check
                    if gene < 1:
                        gene = 1
                    elif gene > 10:
                        gene = 10

                    offspring[i].chromosome[j] = gene

            eval_value = eval_func.evaluate(offspring[i].chromosome)
            offspring[i].fitness = eval_value

        return offspring

    @staticmethod
    def succeed(population, offspring):
        return sorted(offspring, key=lambda m: m.fitness)

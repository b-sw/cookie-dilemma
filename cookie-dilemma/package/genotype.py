"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import random
import math
import numpy as np

SIGMA_RANGE = 0.1


def next_sigma(sigma, a, dimension):

    b = np.random.normal(0, 1)
    tau = 1 / math.sqrt(2 * dimension)
    tau_prim = 1 / math.sqrt(2 * math.sqrt(dimension))
    sigma_j = sigma * math.exp(tau_prim * a + tau * b)

    return sigma_j


class Genotype:
    def __init__(self, chromosome, fitness, dimension):
        self.chromosome = chromosome
        self.fitness = fitness

        self.sigmas = [random.uniform(1 - SIGMA_RANGE, 1 + SIGMA_RANGE)]

        a = np.random.normal(0, 1)
        for i in range(1, dimension):
            sigma_j = next_sigma(self.sigmas[i - 1], a, dimension)
            self.sigmas.append(sigma_j)

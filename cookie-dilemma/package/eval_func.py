"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import math


class ObjectiveValue:
    def __init__(self, grades):
        self.grades = grades
        self.rule_penalty_points = 0
        self.dimension = len(grades)

    def evaluate(self, chromosome):
        sum_penalty = 0

        for value in chromosome:
            sum_penalty += value

        rule_penalty = 0
        for i in range(0, len(chromosome) - 1):
            dif = chromosome[i] - chromosome[i + 1]

            epsilon = self.dimension

            if self.grades[i] > self.grades[i + 1] and dif <= 0:
                # if math.fabs(dif) > 32:
                #     rule_penalty += math.pow(2, 32)
                # else:
                #     rule_penalty += epsilon*math.pow(2, math.fabs(dif))
                rule_penalty += 10 * (math.fabs(dif) + 1)

            elif self.grades[i] < self.grades[i + 1] and dif >= 0:
                # if dif > 32:
                #     rule_penalty += math.pow(2, 32)
                # else:
                #     rule_penalty += epsilon*math.pow(2, dif)
                rule_penalty += 10 * (math.fabs(dif) + 1)

        self.rule_penalty_points = rule_penalty

        return sum_penalty + rule_penalty

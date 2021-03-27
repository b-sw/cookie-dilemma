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

    def evaluate(self, chromosome):
        sum_penalty = 0

        for value in chromosome:
            sum_penalty += value

        rule_penalty = 0
        for i in range(0, len(chromosome) - 1):
            dif = chromosome[i] - chromosome[i + 1]

            epsilon = 2

            if self.grades[i] > self.grades[i + 1] and dif <= 0:
                if dif == 0:
                    rule_penalty += epsilon
                elif math.fabs(dif) > 32:
                    rule_penalty += math.pow(2, 32)
                else:
                    rule_penalty += (epsilon + math.pow(2, math.fabs(dif)))
            elif self.grades[i] < self.grades[i + 1] and dif >= 0:
                if dif == 0:
                    rule_penalty += epsilon
                elif dif > 32:
                    rule_penalty += math.pow(2, 32)
                else:
                    rule_penalty += (epsilon + math.pow(2, dif))

        self.rule_penalty_points = rule_penalty

        return sum_penalty + rule_penalty

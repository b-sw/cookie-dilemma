"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import math


def find_longest_ascending_sequence(element_list):
    compare = 0
    sequence_length_forward = 0
    sequence_length_backwards = 0

    max_length_sequence = 1

    for element in element_list:
        if element > compare:
            sequence_length_forward += 1
            if max_length_sequence < sequence_length_forward:
                max_length_sequence = sequence_length_forward
        else:
            sequence_length_forward = 1
        compare = element

    compare = 0

    for element in reversed(element_list):
        if element > compare:
            sequence_length_backwards += 1
            if max_length_sequence < sequence_length_backwards:
                max_length_sequence = sequence_length_backwards
        else:
            sequence_length_backwards = 1
        compare = element

    return max_length_sequence


class ObjectiveValue:
    def __init__(self, grades):
        self.grades = grades
        self.rule_penalty_points = 0
        self.dimension = len(grades)

    def evaluate(self, chromosome):
        sum_penalty = 0

        for value in chromosome:
            sum_penalty += value

        longest_consecutive_sequence = find_longest_ascending_sequence(chromosome)

        rule_penalty = 0
        for i in range(0, len(chromosome) - 1):
            dif = chromosome[i] - chromosome[i + 1]

            if self.grades[i] > self.grades[i + 1] and dif <= 0:
                # if math.fabs(dif) > 32:
                #     rule_penalty += math.pow(2, 32)
                # else:
                #     rule_penalty += epsilon*math.pow(2, math.fabs(dif))
                rule_penalty += longest_consecutive_sequence * (math.fabs(dif) + 1)

            elif self.grades[i] < self.grades[i + 1] and dif >= 0:
                # if dif > 32:
                #     rule_penalty += math.pow(2, 32)
                # else:
                #     rule_penalty += epsilon*math.pow(2, dif)
                rule_penalty += longest_consecutive_sequence * (math.fabs(dif) + 1)

        self.rule_penalty_points = rule_penalty

        return sum_penalty + rule_penalty



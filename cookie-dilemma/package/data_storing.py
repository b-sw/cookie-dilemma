"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
FITNESS = 0
PENALTY = 1


class SingleRunStorage:
    def __init__(self):
        self.best_eval_in_run = []
        self.best_eval_overall = None

    def add_eval(self, best_eval):
        self.best_eval_in_run.append(best_eval)

        if self.best_eval_overall is None:
            self.best_eval_overall = best_eval
        elif best_eval < self.best_eval_overall:
            self.best_eval_overall = best_eval


class MultipleRunStorage:
    def __init__(self):
        self.best_evals = []

    def mean(self):
        mean = 0
        for element in self.best_evals:
            mean += element

        mean /= len(self.best_evals)
        return mean

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
        elif best_eval[FITNESS] < self.best_eval_overall[FITNESS]:
            self.best_eval_overall = best_eval
        elif best_eval[FITNESS] == self.best_eval_overall[FITNESS] and \
                best_eval[PENALTY] < self.best_eval_overall[PENALTY]:
            self.best_eval_overall = best_eval


class MultipleRunStorage:
    def __init__(self):
        self.best_evals = []

    def mean(self):
        # todo
        pass

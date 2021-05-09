"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import pulp as pl

from package.eval_func import ObjectiveValue


def mip_optimize(problem):
    solution = []

    for i in range(len(problem)):
        solution.append(pl.LpVariable('s' + str(i), 1, 10, pl.LpInteger))

    # define the problem
    prob = pl.LpProblem("cookie-dilemma", pl.LpMinimize)

    # objective function - maximize value of objects in knapsack
    prob += sum(solution)

    # constraints
    for i in range(1, len(problem)):
        if problem[i] > problem[i - 1]:
            prob += solution[i] - solution[i - 1] >= 1
        if problem[i] < problem[i - 1]:
            prob += solution[i] - solution[i - 1] <= -1

    prob.solve(pl.PULP_CBC_CMD(msg=0))
    # status = prob.solve()  # solve using the default solver, which is cbc
    # print(pl.LpStatus[status])  # print the human-readable status

    # print the values
    # for element in solution:
    #     print(pl.value(element))

    return sum(pl.value(element) for element in solution)

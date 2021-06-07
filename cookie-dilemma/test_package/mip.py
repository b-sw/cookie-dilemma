import numpy as np

from package.mip import mip_optimize


def test_mip():
    problem = np.random.randint(1, high=11, size=10)
    print("--------------------------------")
    print("Testing MIP solver for problem: ", problem)
    print("--------------------------------")
    optimal_solution = mip_optimize(problem)
    print("--------------------------------")
    print("Done testing MIP solver. Optimal solution is: ", optimal_solution)
    print("--------------------------------")

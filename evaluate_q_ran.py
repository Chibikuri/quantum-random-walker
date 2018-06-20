import quantum_random_walker as qran
import numpy as np

class evaluate:
    def evaluation():
        for i in range(10):
            result = []
            var = qran.random_walker.random_walk_sim()
            result.append(var)
        print(np.mean(result))


if __name__ == "__main__":
    evaluate.evaluation()

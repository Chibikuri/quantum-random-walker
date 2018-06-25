import quantum_random_walker as qran
import classical_random_walker as cran
import numpy as np

class evaluate:
    def q_evaluation():
        qresult = []
        for i in range(100):
            qvar = qran.random_walker.random_walk_sim()
            qresult.append(qvar)
            print(qvar)
        print(np.mean(qresult), np.min(np.abs(qresult)), np.max(np.abs(qresult)))

    def c_evaluation():
        cresult = []
        for j in range(100):
            cvar = cran.cal_random.random_walker()
            cresult.append(cvar)
            print(cvar)
        print(np.mean(cresult), np.min(np.abs(cresult)), np.max(np.abs(cresult)))



if __name__ == "__main__":
    evaluate.q_evaluation()
    evaluate.c_evaluation()

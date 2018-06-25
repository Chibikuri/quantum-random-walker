from qis_sim import Quantum_culc as qcl
#import matplotlib.pyplot as plt
import numpy as np


class random_walker:
    @classmethod
    def random_walk_sim(self):
        x = 0
        y = 0
        n = 1000
        x_value = [t for t in range(n)]
        y_value = []
        for i in range(n):
            result = qcl.culc()
            if result["00"] > result["11"]:
                y = y + 1
            elif result["00"] == result["11"]:
                y = y
            else:
                y = y - 1
            x = x + 1
            y_value.append(y)
        #print(x, y, y_value.index(0))
        #plt.plot(x_value, y_value, color = "red")
        #plt.plot([0, n], [0, 0], color = "blue", linestyle = "dashed")
        #plt.show()
        return np.mean(y_value)



if __name__ == "__main__":
    #res = qcl.culc()
    #print(res["00"])
    random_walker.random_walk_sim()

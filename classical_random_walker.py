import random
import numpy as np
import matplotlib.pyplot as plt

class cal_random:
    def random_walker():
        x = 0
        y = 0
        n = 1000
        x_data = [t for t in range(n)]
        y_data = []
        for i in range(n):
            ran1 = random.randint(0, 1000)
            ran2 = random.randint(0, 1000)
            if ran1 > ran2:
                y = y + 1
            elif ran1 == ran2:
                y = y
            else:
                y = y - 1
            y_data.append(y)
            x = x + 1
        try:
            print(x, y, y_data.index(0))
            #plt.plot(x_data, y_data, color = "blue")
            #plt.plot([0, n], [0, 0], linestyle="dashed")
            #plt.show()
            return y_data, n
        except:
            print(x, y)

if __name__ == "__main__":
    cal_random.random_walker()

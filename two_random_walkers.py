#import matplotlib.pyplot as plt
#import classical_random_walker as cran
#import quantum_random_walker as qran

class make_graph:
    def draw_graph():
        #q_result = qran.random_walker.random_walk_sim()
        #c_result = cran.cal_random.random_walker()
        #if q_result[1] != c_result[1]:
        #    print("please put the same number n.")
        #    return 0
        #else:
        #    x_ = [c for c in range(q_result[1])]
        #    return 1, x_

        #t = make_graph.error()
        #if t == 0:
        #    pass
        #else:
        q_result = qran.random_walker.random_walk_sim()
        c_result = cran.cal_random.random_walker()
        print(q_result, c_result)
        x_ = [count for count in range(1000)]
        #plt.plot(x_, q_result, color="red")
        #plt.plot(x_, c_result, color="blue")
        #plt.plot([0, 1000], [0, 0], linestyle="dashed")
        #plt.show()

if __name__ == "__main__":
    make_graph.draw_graph()

import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

from numba import jit
from multiprocessing import pool
from output import output2File
from config import *
from EvolutionGame2 import EvolutionGameProcess
from player import playersInit, players
from alive_progress import alive_bar

random.seed(seed_value)
np.random.seed(seed_value)
os.environ['PYTHONHASHSEED'] = str(seed_value)


if __name__ == '__main__':
    figure = [plt.subplot(2, 2, i+1) for i in range(4)]
    xPoint = np.array(i for i in np.arange(1, 2, 0.1))
    yPoint = np.zeros((5, 3, 3, 20))
    # [g][p][NOCs][b]:

    for i in range(len(glist)):
        for j in range(len(blist)):
            for k in range(len(plist)):
                fc = [0., 0.]  # ER, SF
                for _Graph in range(DiffGraph):
                    Matrix_ER = nx.to_numpy_matrix(nx.erdos_renyi_graph(N, ER_p))
                    Matrix_SF = nx.to_numpy_matrix(nx.barabasi_albert_graph(N, m))

                    playersInit()
                    fc[0] += EvolutionGameProcess(Matrix_ER, "PD", glist[i], blist[j], plist[k])  # 均为囚徒博弈
                    playersInit()
                    fc[1] += EvolutionGameProcess(Matrix_SF, "PD", glist[i], blist[j], plist[k])

                for NOCs in range(2):
                    fc[NOCs] /= DiffGraph
                    yPoint[i][k][NOCs][j] = fc[NOCs]
                    output2File("output.txt", "a", "g:{}; b:{}; p:{}; NOCs:{}; fc:{}"
                                .format(glist[i], blist[j], plist[k], NOCs, fc[NOCs]))

    for g in range(len(glist)):
        for i in range(4):
            figure[i].plot(xPoint, yPoint[g][0 if i % 2 == 0 else 1][0 if i < 2 else 1], label="g = {}".format(glist[g]))
    plt.savefig('./temporal_network.jpg')
    plt.show()

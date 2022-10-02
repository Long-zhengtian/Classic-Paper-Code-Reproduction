import random
import networkx as nx
import networkt as nt
import matplotlib.pyplot as plt
import numpy as np
import os

from numba import jit
from multiprocessing import pool
from output import output2File
from config import *
from EvolutionGame import EvolutionGameProcess
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

    for _Graph in range(DiffGraph):
        Matrix_ER = nt.erdos_renyi_graph(N, ER_p)
        Matrix_SF = nt.barabasi_albert_graph(N, m, m)
        for i in range(len(glist)):  # 每个snapshot的演化次数
            for j in range(len(blist)):  # 囚徒困境中的背叛者优势，横坐标
                for k in range(len(plist)):  # 随机删边的概率
                    playersInit()
                    yPoint[i][k][0][j] += EvolutionGameProcess(Matrix_ER, "PD", glist[i], blist[j], plist[k])  # 均为囚徒博弈
                    playersInit()
                    yPoint[i][k][1][j] += EvolutionGameProcess(Matrix_SF, "PD", glist[i], blist[j], plist[k])

    yPoint /= DiffGraph

    for NOCs in range(2):
        for i in range(len(glist)):
            for j in range(len(blist)):
                for k in range(len(plist)):
                    output2File("output.txt", "a", "g:{}; b:{}; p:{}; NOCs:{}; fc:{}".format(glist[i], blist[j], plist[k], NOCs, yPoint[i][k][NOCs][j]))

    for g in range(len(glist)):
        for i in range(4):
            figure[i].plot(xPoint, yPoint[g][0 if i % 2 == 0 else 1][0 if i < 2 else 1], label="g = {}".format(glist[g]))
    plt.savefig('./temporal_network.jpg')
    plt.show()

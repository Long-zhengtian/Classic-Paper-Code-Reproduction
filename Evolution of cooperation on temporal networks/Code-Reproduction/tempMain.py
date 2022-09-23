import copy
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

from config import *
from EvolutionGame import EvolutionGameProcess
from player import playersInit
from alive_progress import alive_bar

random.seed(seed_value)
np.random.seed(seed_value)
os.environ['PYTHONHASHSEED'] = str(seed_value)


def run(NOCs, game, bORr):
    with alive_bar(int(G/g), force_tty=True) as bar:
        for _ in range(int(G/g)):
            snapshot = copy.deepcopy(NOCs)
            for e in snapshot.edges():  # 以概率p随机删边
                if p > random.random():
                    snapshot.remove_edge(e[0], e[1])
            return EvolutionGameProcess(snapshot, game, bORr)


if __name__ == '__main__':

    xPoint = [[] for _ in range(4)]  # 0: ER,PD; 1: ER,SG; 2: SF,PD; 3: SF,SG
    yPoint = [[] for _ in range(4)]
    for i in range(DiffGraph):
        ER_NOCs = nx.erdos_renyi_graph(N, ER_p)
        SF_NOCs = nx.barabasi_albert_graph(N, m)
        Graph_b = 0
        Graph_r = 0
        for _b in np.arange(1, 1.2, 0.025):
            playersInit()
            xPoint[0].append(_b)
            fc = run(ER_NOCs, "PD", _b)
            if i == 0:
                yPoint[0].append(fc)
            else:
                yPoint[0][Graph_b] += fc

            playersInit()
            xPoint[2].append(_b)
            fc = run(SF_NOCs, "PD", _b)
            if i == 0:
                yPoint[2].append(fc)
            else:
                yPoint[2][Graph_b] += fc
            Graph_b += 1
        for _r in np.arange(0.001, 1, 0.1):
            playersInit()
            xPoint[1].append(_r)
            fc = run(ER_NOCs, "SG", _r)
            if i == 0:
                yPoint[1].append(fc)
            else:
                yPoint[1][Graph_r] += fc

            playersInit()
            xPoint[3].append(_r)
            fc = run(SF_NOCs, "SG", _r)
            if i == 0:
                yPoint[3].append(fc)
            else:
                yPoint[3][Graph_r] += fc
            Graph_r += 1
    for i in range(4):
        yPoint[i] /= DiffGraph

    plt.ion()
    plt.figure(figsize=(16, 10))

    plt.subplot(2, 2, 1)
    plt.plot(xPoint[0], yPoint[0], marker='o', ms=5)
    plt.title("Prisoner’s Dilemma")

    plt.subplot(2, 2, 2)
    plt.plot(xPoint[0], yPoint[0], marker='o', ms=5)
    plt.title("Snowdrift Game")

    plt.subplot(2, 2, 3)
    plt.plot(xPoint[0], yPoint[0], marker='o', ms=5)
    plt.xlabel("b")

    plt.subplot(2, 2, 4)
    plt.plot(xPoint[0], yPoint[0], marker='o', ms=5)
    plt.xlabel("c")

    plt.savefig('./PDAndSG.jpg')
    plt.show()

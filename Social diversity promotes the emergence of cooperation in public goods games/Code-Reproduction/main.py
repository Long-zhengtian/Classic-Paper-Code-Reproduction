import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from config import *
from player import players, playersInit
from PGGE import PGGEProcess

if __name__ == '__main__':
    fig = plt.figure()
    plt.ylabel("frequnency of cooperators")

    for eta in np.arange(0.2, 1.1, 0.1):  # 正规化的增强因子 r = eta * (k + 1)
        r = eta * (2 * m + 1)
        SumGraphG = 0
        SumGraphI = 0
        for _ in range(DiffGraph):  # 重构10次图
            playersInit()
            regular_NOCs = nx.random_regular_graph(2*m, N)  # 构建一个含有N个节点，每个节点2*m度的规则图
            SumGraphG += PGGEProcess(regular_NOCs, True, r)
            SumGraphI += PGGEProcess(regular_NOCs, False, r)
        SumGraphG /= DiffGraph
        ax1 = plt.subplot(2, 2, 1)
        plt.plot(eta, SumGraphG, marker='o', ms=3)
        print("Regular_NOCs, eta: {}; SumGraphG: {}".format(eta, SumGraphG))

        SumGraphI /= DiffGraph
        ax2 = plt.subplot(2, 2, 2)
        plt.plot(eta, SumGraphI, marker='o', ms=3)
        print("Regular_NOCs, eta: {}; SumGraphI: {}".format(eta, SumGraphI))

        SumGraphG = 0
        SumGraphI = 0
        for _ in range(DiffGraph):
            playersInit()
            sf_NOCs = nx.barabasi_albert_graph(N, m)  # 使用BA模型构建一个含有N个节点的无标度网络，每次添加m个边
            SumGraphG += PGGEProcess(sf_NOCs, True, r)
            SumGraphI += PGGEProcess(sf_NOCs, False, r)
        SumGraphG /= DiffGraph
        ax3 = plt.subplot(2, 2, 3)
        plt.plot(eta, SumGraphG, marker='*', ms=3)
        print("SF_NOCs, eta: {}; SumGraphG: {}".format(eta, SumGraphG))

        SumGraphI /= DiffGraph
        ax4 = plt.subplot(2, 2, 4)
        plt.plot(eta, SumGraphI, marker='*', ms=3)
        print("SF_NOCs, eta: {}; SumGraphI: {}".format(eta, SumGraphI))

    plt.savefig('./PGG.jpg')
    plt.show()


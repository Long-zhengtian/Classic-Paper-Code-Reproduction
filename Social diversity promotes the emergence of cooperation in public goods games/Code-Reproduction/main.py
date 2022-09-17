import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from output import output2File
from config import *
from PGGE import PGGEProcess

if __name__ == '__main__':
    fig = plt.figure()
    plt.ylabel("frequnency of cooperators")
    xpoint = []
    ypointG = []
    ypointI = []
    for eta in np.arange(0.2, 1.1, 0.05):  # 正规化的增强因子 r = eta * (k + 1)
        xpoint.append(eta)
        r = eta * (2 * m + 1)
        SumGraphG = 0
        SumGraphI = 0
        for _ in range(DiffGraph):  # 重构图
            regular_NOCs = nx.random_regular_graph(2*m, N)  # 构建一个含有N个节点，每个节点2*m度的规则图
            SumGraphG += PGGEProcess(regular_NOCs, True, r)
            SumGraphI += PGGEProcess(regular_NOCs, False, r)

        SumGraphG /= DiffGraph
        ypointG.append(SumGraphG)
        output2File("output.txt", "a", "Regular_NOCs, eta: {}; SumGraphG: {}".format(eta, SumGraphG))

        SumGraphI /= DiffGraph
        ypointI.append(SumGraphI)
        output2File("output.txt", "a", "Regular_NOCs, eta: {}; SumGraphI: {}".format(eta, SumGraphI))

    ax1 = plt.subplot(2, 1, 1)
    plt.plot(xpoint, ypointG, marker='o', ms=5)
    ax2 = plt.subplot(2, 1, 2)
    plt.plot(xpoint, ypointI, marker='o', ms=5)

    ypointI.clear()
    ypointG.clear()
    for eta in np.arange(0.2, 1.1, 0.05):  # 正规化的增强因子 r = eta * (k + 1)
        r = eta * (2 * m + 1)
        SumGraphG = 0
        SumGraphI = 0
        for _ in range(DiffGraph):
            sf_NOCs = nx.barabasi_albert_graph(N, m)  # 使用BA模型构建一个含有N个节点的无标度网络，每次添加m个边
            SumGraphG += PGGEProcess(sf_NOCs, True, r)
            SumGraphI += PGGEProcess(sf_NOCs, False, r)
        SumGraphG /= DiffGraph
        ypointG.append(SumGraphG)
        output2File("output.txt", "a", "SF_NOCs, eta: {}; SumGraphG: {}".format(eta, SumGraphG))

        SumGraphI /= DiffGraph
        ypointI.append(SumGraphI)
        output2File("output.txt", "a", "SF_NOCs, eta: {}; SumGraphI: {}".format(eta, SumGraphI))

    ax1 = plt.subplot(2, 1, 1)
    plt.plot(xpoint, ypointG, marker='*', ms=5)
    ax2 = plt.subplot(2, 1, 2)
    plt.plot(xpoint, ypointI, marker='*', ms=5)

    plt.savefig('./PGG1.jpg')
    plt.show()


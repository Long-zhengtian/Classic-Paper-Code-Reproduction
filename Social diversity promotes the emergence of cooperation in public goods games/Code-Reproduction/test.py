import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from output import output2File
from config import *
from PGGE import PGGEProcess
from decimal import Decimal

if __name__ == '__main__':
    fig = plt.figure()
    plt.ylabel("frequnency of cooperators")
    xpoint = []
    ypointI = []

    for eta in np.arange(0.2, 1.1, 0.05):  # 正规化的增强因子 r = eta * (k + 1)
        r = eta * (2 * m + 1)
        SumGraphG = 0
        SumGraphI = 0
        for _ in range(DiffGraph):
            sf_NOCs = nx.barabasi_albert_graph(N, m)  # 使用BA模型构建一个含有N个节点的无标度网络，每次添加m个边
            SumGraphI += PGGEProcess(sf_NOCs, False, r)

        SumGraphI /= DiffGraph
        ypointI.append(SumGraphI)
        output2File("output.txt", "a", "SF_NOCs, eta: {}; SumGraphI: {}".format(eta, SumGraphI))

    ax2 = plt.subplot(2, 1, 2)
    plt.plot(xpoint, ypointI, marker='*', ms=5)

    plt.savefig('./PGGtest.jpg')
    plt.show()


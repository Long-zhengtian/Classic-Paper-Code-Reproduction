import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from player import playersInit
from config import *
from EvolutionGame import EvolutionGameProcess
from output import output2File


if __name__ == '__main__':
    fig = plt.figure()
    plt.ylabel("frequnency of cooperators")
    xpoint = []
    ypoint = []

    for _k in [4, 16, 32, 64]:
        regular_ring_NOCs = nx.watts_strogatz_graph(N, _k, 0)  # 构建一个含有N个节点，每个节点k度的规则环形图（最近邻耦合网络）
        # regular_ring_NOCs = nx.random_regular_graph(_k, N)  # 构建一个含有N个节点，每个节点k度的规则图
        print("regular_ring_NOCs, PD")
        xpoint.clear()
        ypoint.clear()
        for _b in np.arange(1, 1.2, 0.025):
            output2File("output.txt", "w", "regular_ring_NOCs, PD")
            playersInit()
            fc = EvolutionGameProcess(regular_ring_NOCs, "PD", _b)
            print("k: {}; b: {}; fc:{} ".format(_k, _b, fc))
            xpoint.append(_b)
            ypoint.append(fc)

        ax1 = plt.subplot(2, 2, 1)
        plt.title("Prisoner’s Dilemma")
        plt.plot(xpoint, ypoint, marker = 'o', ms = 3, label = "z = {}".format(_k))

        print("regular_ring_NOCs, SG")
        xpoint.clear()
        ypoint.clear()
        for _r in np.arange(0.001, 1, 0.1):
            output2File("output.txt", "w", "regular_ring_NOCs, SG")
            playersInit()
            fc = EvolutionGameProcess(regular_ring_NOCs, "SG", _r)
            print("k: {}; r: {}; fc:{} ".format(_k, _r, fc))
            xpoint.append(_r)
            ypoint.append(fc)

        ax2 = plt.subplot(2, 2, 2)
        plt.title("Snowdrift Game")
        plt.plot(xpoint, ypoint, marker = 'o', ms = 3, label = "z = {}".format(_k))
        plt.legend(loc = 'upper right')

    for _m in [2, 4, 8]:
        sf_NOCs = nx.barabasi_albert_graph(N, _m)  # 使用BA模型构建一个含有N个节点的无标度网络，每次添加m个边
        print("sf_NOCs, PD")
        xpoint.clear()
        ypoint.clear()
        for _b in np.arange(1, 2, 0.1):    
            output2File("output.txt", "w", "sf_NOCs, PD")
            playersInit()
            fc = EvolutionGameProcess(sf_NOCs, "PD", _b)
            print("m: {}; b: {}; fc:{} ".format(_m, _b, fc))
            xpoint.append(_b)
            ypoint.append(fc)

        plt.plot(xpoint, ypoint, marker = 'o', ms = 3, label = "z = {}".format(2*_m))

        
    plt.savefig('./PDAndSG2.jpg')
    plt.show()

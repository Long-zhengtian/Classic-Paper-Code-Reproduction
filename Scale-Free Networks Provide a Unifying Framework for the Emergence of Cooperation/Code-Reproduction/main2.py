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

    for _k in [4]:
        # regular_ring_NOCs = nx.watts_strogatz_graph(N, _k, 0)  # 构建一个含有N个节点，每个节点k度的规则环形图（最近邻耦合网络）
        regular_ring_NOCs = nx.random_regular_graph(_k, N)  # 构建一个含有N个节点，每个节点k度的规则图
        print("regular_ring_NOCs, PD")
        xpoint.clear()
        ypoint.clear()
        for _b in np.linspace(0, 100, 11):
            output2File("output.txt", "w", "regular_ring_NOCs, PD")
            playersInit()
            fc = EvolutionGameProcess(regular_ring_NOCs, "PD", _b)
            print("k: {}; b: {}; fc:{} ".format(_k, _b, fc))
            xpoint.append(_b)
            ypoint.append(fc)

        plt.title("Prisoner’s Dilemma")
        plt.plot(xpoint, ypoint, marker='o', ms=3, label="z = {}".format(_k))
        plt.legend(loc='upper right')

        with open('./result/result.txt', 'w') as f:
            for i in range(len(xpoint)):
                f.write(str(xpoint[i]) + ' ' + str(ypoint[i]) + '\n')
    plt.savefig('./PDAndSG2.jpg')
    plt.show()

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from player import players, playersInit
from config import *
from EvolutionGame import EvolutionGameProcess
from output import output2File

def draw():  # 结果绘图
    # nx.draw(regular_NOCs, nx.spectral_layout(regular_NOCs),with_labels=True,node_size=10)
    # plt.show()
    # nx.draw(sf_NOCs, nx.spectral_layout(sf_NOCs),with_labels=True,node_size=50)
    # plt.show()
    pass

if __name__ == '__main__':
    for _k in [4, 16, 32, 64]:
        regular_NOCs = nx.random_regular_graph(_k, N)  # 构建一个含有N个节点，每个节点k度的规则图
        for _b in np.arange(1, 1.2, 0.025):
            output2File("output.txt", "w", "regular_NOCs, PD")
            playersInit()
            EvolutionGameProcess(regular_NOCs, "PD", _b)
            
        for _r in np.arange(0, 1, 0.1):
            output2File("output.txt", "a", "regular_NOCs, SG")
            playersInit()
            EvolutionGameProcess(regular_NOCs, "SG", _r)
    
    for _m in [2, 4, 8]:
        sf_NOCs = nx.barabasi_albert_graph(N, _m)  # 使用BA模型构建一个含有N个节点的无标度网络，每次添加m个边
        for _b in np.arange(1, 2, 0.1):    
            output2File("output.txt", "a", "sf_NOCs, PD")
            playersInit()
            EvolutionGameProcess(sf_NOCs, "PD", _b)
        for _r in np.arange(0, 1, 0.1):
            output2File("output.txt", "a", "sf_NOCs, SG")
            playersInit()
            EvolutionGameProcess(sf_NOCs, "SG", _r)



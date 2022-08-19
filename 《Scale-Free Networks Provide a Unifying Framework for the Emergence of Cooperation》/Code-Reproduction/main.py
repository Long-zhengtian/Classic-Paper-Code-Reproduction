import networkx as nx
import matplotlib.pyplot as plt
from player import players, playersInit
from config import *
from EvolutionGame import EvolutionGameProcess


def draw():  # 结果绘图
    nx.draw(regular_NOCs, nx.spectral_layout(regular_NOCs),with_labels=True,node_size=40)
    plt.show()
    # nx.draw(sf_NOCs, nx.spectral_layout(sf_NOCs),with_labels=True,node_size=50)
    # plt.show()

if __name__ == '__main__':
    regular_NOCs = nx.random_regular_graph(k, N)  # 构建一个含有N个节点，每个节点k度的规则图
    # print("regular_NOCs, PD")
    playersInit()
    EvolutionGameProcess(regular_NOCs, "PD")
    # print("regular_NOCs, SG")
    playersInit()
    EvolutionGameProcess(regular_NOCs, "SG")

    sf_NOCs = nx.barabasi_albert_graph(N, m)  # 使用BA模型构建一个含有N个节点的无标度网络，每次添加m个边
    # print("sf_NOCs, PD")
    playersInit()
    EvolutionGameProcess(sf_NOCs, "PD")
    # print("sf_NOCs, SG")
    playersInit()
    EvolutionGameProcess(sf_NOCs, "SG")

    # draw()


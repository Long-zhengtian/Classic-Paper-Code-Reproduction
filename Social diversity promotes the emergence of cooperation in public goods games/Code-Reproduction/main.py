import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from config import *
from player import players, playersInit
from PGGE import PGGEProcess

if __name__ == '__main__':
    for eta in np.arange(0.2, 1.1, 0.1):  # 正规化的增强因子 r = eta * (k + 1)
        r = eta * (2 * m + 1)
        for _ in range(DiffGraph):  # 重构10次图
            playersInit()
            regular_NOCs = nx.random_regular_graph(2*m, N)  # 构建一个含有N个节点，每个节点2*m度的规则图
            PGGEProcess(regular_NOCs, True, r)
            # PGGEProcess(regular_NOCs, False, r)

            playersInit()
            sf_NOCs = nx.barabasi_albert_graph(N, m)  # 使用BA模型构建一个含有N个节点的无标度网络，每次添加m个边
            PGGEProcess(sf_NOCs, True, r)
            # PGGEProcess(sf_NOCs, False, r)



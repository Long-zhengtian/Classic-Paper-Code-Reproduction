import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from player import players, playersInit
from config import *
from EvolutionGame import EvolutionGameProcess
from output import output2File

# if __name__ == '__main__':

# for _m in [2]: #[2, 4, 8]:
#     sf_NOCs = nx.barabasi_albert_graph(N, _m)  # 使用BA模型构建一个含有N个节点的无标度网络，每次添加m个边
#     # xx =nx.spectral_layout(sf_NOCs)
#     # nx.draw(sf_NOCs,xx,with_labels=True,node_size=30)
#     # plt.show()
#     # for id in range(N):
#     #     print("id's adj: ", end="")
#     #     print(sf_NOCs.adj[id])
#     print("sf_NOCs, PD")
#     for _b in np.arange(1, 2, 0.1):    
#         playersInit()
#         fc = EvolutionGameProcess(sf_NOCs, "PD", _b)
#         print("m: {}; b: {}; fc:{} ".format(_m, _b, fc))
#     print("sf_NOCs, SG")
#     for _r in np.arange(0.001, 1, 0.1):
#         playersInit()
#         fc = EvolutionGameProcess(sf_NOCs, "SG", _r)
#         print("m: {}; r: {}; fc:{} ".format(_m, _r, fc))
        
for _k in [64]: #[4, 16, 32, 64]:
    regular_NOCs = nx.random_regular_graph(_k, N)  # 构建一个含有N个节点，每个节点k度的规则图
    print("regular_NOCs, PD")
    for _b in np.arange(1, 1.2, 0.025):
        output2File("output.txt", "a", "regular_NOCs, PD")
        playersInit()
        fc = EvolutionGameProcess(regular_NOCs, "PD", _b)
        print("k: {}; b: {}; fc:{} ".format(_k, _b, fc))
    
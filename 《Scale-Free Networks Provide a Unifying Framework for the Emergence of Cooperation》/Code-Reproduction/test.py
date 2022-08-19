import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from player import players, playersInit
from config import *
from EvolutionGame import EvolutionGameProcess
from output import output2File

def draw():  # 结果绘图
    
    pass

# if __name__ == '__main__':
fig = plt.figure()
xpoint = []
ypoint = []
for _k in [2]: #[4, 16, 32, 64]:
    regular_NOCs = nx.random_regular_graph(_k, N)  # 构建一个含有N个节点，每个节点k度的规则图
    print("regular_NOCs, PD")
    xpoint.clear()
    ypoint.clear()
    for _b in np.arange(1, 1.5, 0.025):
        output2File("output.txt", "w", "regular_NOCs, PD")
        playersInit()
        Temp = 0
        for id in range(N):
            if players[id].strategy:
                Temp += 1
        output2File("output.txt", "a", "Temp: {}".format(Temp))
        fc = EvolutionGameProcess(regular_NOCs, "PD", _b)
        print("k: {}; b: {}; fc:{} ".format(_k, _b, fc))
        xpoint.append(_b)
        ypoint.append(fc)

plt.title("Prisoner’s Dilemma")
plt.plot(xpoint, ypoint)

plt.show()
    
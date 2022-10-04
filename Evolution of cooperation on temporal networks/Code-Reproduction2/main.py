import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

from output import output2File
from config import *
from EvolutionGame import EvolutionGameProcess
from player import playersInit, players

random.seed(seed_value)
np.random.seed(seed_value)
os.environ['PYTHONHASHSEED'] = str(seed_value)


if __name__ == '__main__':
    plt.figure(figsize=(12, 9))
    xPoint = np.array([i for i in range(G1)])
    yPoint = np.zeros((5, 3, 3, G1))  # [g][p][NOCs][time]:

    for i in range(len(glist)):  # 每个snapshot的演化次数
        for j in range(len(blist)):  # 囚徒困境中的背叛者优势，横坐标
            for k in range(len(plist)):  # 随机删边的概率
                playersInit()
                yPoint[i][k][0] = EvolutionGameProcess("ER", glist[i], blist[j], plist[k])  # 均为囚徒博弈
                playersInit()
                yPoint[i][k][1] = EvolutionGameProcess("SF", glist[i], blist[j], plist[k])
                # print(glist[i], blist[j], plist[k], yPoint[i][k][0][j], yPoint[i][k][1][j])

    for g in range(len(glist)):
        for i in range(4):
            subfig = 22 * 10 + i + 1
            plt.subplot(subfig)
            plt.plot(xPoint, yPoint[g][0 if i % 2 == 0 else 1][0 if i < 2 else 1],
                           label="g = {}".format(glist[g]))
            if i == 0:
                plt.title("p=0.3")
                plt.ylabel("ER")
            elif i == 1:
                plt.title("p=0.8")
                plt.legend(loc='upper right')
            elif i == 2:
                plt.xlabel("time")
                plt.ylabel("SF")
            else:
                plt.xlabel("time")
    plt.savefig('./temporal_network'+str(N)+'N'+str(G1)+'G1_Time' + str(G1) + '.jpg')
    plt.show()

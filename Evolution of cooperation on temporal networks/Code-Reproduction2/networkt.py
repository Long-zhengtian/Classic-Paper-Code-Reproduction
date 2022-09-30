import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt
import time
import math

from numba import jit, njit

test_list = np.array((3, 2, 4, 1, 5, 85), dtype=np.int64)
test_n = 10000


@njit
def random_pick_one(p):
    choose_array = []
    for index in range(len(p)):
        for i in range(p[index]):
            choose_array.append(index)
    choice_node = np.random.choice(np.array(choose_array))
    return choice_node


@njit
def random_pick_many(size, p):  # 根据权重p，抽取size个元素，返回下标
    picklist = []
    prob = p.copy()
    for i in range(size):
        picked = random_pick_one(prob)
        picklist.append(picked)
        prob[picked] = 0
    return np.array(picklist)


@njit
def barabasi_albert_graph(N, m, m0):  # BA模型无标度网络
    if m0 is None:
        m0 = m
    BAmat = np.zeros((N, N), dtype=np.int64)
    m0list = np.zeros(1, dtype=np.int64)
    degrees = np.zeros(N, dtype=np.int64)
    for i in range(1, m0):  # 前m0个节点随机连接m0-1条边
        friend = np.random.choice(m0list)
        BAmat[i, friend] = BAmat[friend, i] = 1
        m0list = np.append(m0list, i)
    for i in range(m0):
        degrees[i] = np.count_nonzero(BAmat[i])
    for i in range(m0, N):  # 后来添加的节点需要满足生长和优先依附原则
        choice_node = random_pick_many(m, degrees[:i])
        for j in choice_node:
            BAmat[i, j] = BAmat[j, i] = 1
        for j in range(i+1):
            degrees[j] = np.count_nonzero(BAmat[j])
    return BAmat


@njit
def erdos_renyi_graph(N, p):  # ER随机图，N个节点
    ERmat = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        for j in range(i):
            if p > random.random():
                ERmat[i, j] = ERmat[j, i] = 1
    return ERmat


# mm = erdos_renyi_graph(test_n, 0.5)
# nn = nx.from_numpy_array(mm)
# degrees = np.zeros(test_n, dtype=np.int64)
# for i in range(test_n):
#     degrees[i] = np.count_nonzero(mm[i])
# print(degrees)


# start = time.time()
# ba = barabasi_albert_graph(test_n, 3, 5)
# end = time.time()
# print(end-start)
#
# start = time.time()
# na = nx.barabasi_albert_graph(test_n, 3)
# end = time.time()
# print(end-start)
#
# degrees = np.zeros(test_n, dtype=np.int64)
# for i in range(test_n):
#     degrees[i] = np.count_nonzero(ba[i])
# # print(degrees)
#
# sum_deg = np.zeros(test_n, dtype=np.int64)
# for i in range(test_n):
#     sum_deg[degrees[i]] += 1
# print(sum_deg)
# xpoint = []
# ypoint = []
# for i in range(1, test_n):
#     if sum_deg[i] != 0:
#         xpoint.append(math.log(i))
#         ypoint.append(math.log(sum_deg[i]))
#
# print(xpoint)
# print(ypoint)
# plt.scatter(xpoint, ypoint)
# plt.show()





# nn = nx.from_numpy_array(ba)
# print(nn)

# nn = nx.barabasi_albert_graph(50, 2)
# pos = nx.spectral_layout(nn)
# # draw the regular graphy
# nx.draw(nn, pos, with_labels = False, node_size = 30)
# plt.show()

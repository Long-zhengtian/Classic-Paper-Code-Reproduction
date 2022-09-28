import numpy as np
import random
from numba import jit, njit


def preferAttachProportionalToDegree():  # 生长和优先依附原则
    pass


def barabasi_albert_graph(n, m, m0):  # BA模型无标度网络
    if m0 is None:
        m0 = m



def erdos_renyi_graph():  # ER随机图
    pass

# class GraphT:
#     def __init__(self, n):  # 节点数量
#         self.__Graph = np.zeros((n, n))  # 一个np数组用来存储图，私有实例变量
#         self.__size = n
#
#     def __str__(self):
#         pass
#
#     def graph(self):
#         return self.__Graph
#
#     def adjs(self, index):  # 返回index节点的邻居
#         return np.nonzero(self.__Graph[index])
#
#     def edgesNum(self):  # 边的数量（非0边）
#         return np.count_nonzero(self.__Graph)
#
#     def edgesList(self):  # 枚举所有的边
#         return np.nonzero(self.__Graph)
#
#     def add_edge(self, xid, yid, weight=1):
#         self.__Graph[xid, yid] = weight
#
#     def remove_edge(self, xid, yid):
#         self.__Graph[xid, yid] = 0
#
#
# class RandomRegularGraphT(GraphT):
#     pass
#
#
# class BarabasiAlbertGraphT(GraphT):
#     def __init__(self, n, m):  # 节点数量n，每次加边m
#         super().__init__(n)
#
#     def prefer_attach_proportional_to_degree(self):
#         pass
#
#
#
# x = GraphT(3)
# x.add_edge(1, 2, 3)
# y = BarabasiAlbertGraphT(4, 2)
# print(y.graph())

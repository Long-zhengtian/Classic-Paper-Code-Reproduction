import networkx as nx
import numpy as np
Matrix_ER = nx.to_numpy_matrix(nx.erdos_renyi_graph(10, 0.7))

print(type(Matrix_ER))
# ma = Matrix_ER.copy()
#
# ma[0][0] = 2
# print(Matrix_ER)
# print(ma)
#
# [row, col] = ma.shape
# print(row)
# print(col)
# for x in range(row):
#     for y in range(col):
#         ma[x, y] = x*10+y
#
# print(ma)
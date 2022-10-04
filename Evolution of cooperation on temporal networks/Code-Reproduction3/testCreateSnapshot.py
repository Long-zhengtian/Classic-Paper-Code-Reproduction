import copy
import random
import networkx as nx
from config import *
import matplotlib.pyplot as plt

SF_NOCs = nx.barabasi_albert_graph(20, m)
ER_NOCs = nx.erdos_renyi_graph(20, ER_p)
plt.figure()
nx.write_gpickle(SF_NOCs, "./testSnapshot/SFNOCs_" + str(20) + "N_" + str(m) + "m_" + ".gpickle")
nx.draw(SF_NOCs, with_labels=True)
plt.savefig("./testSnapshot/SFNOCs_" + str(20) + "N_" + str(m) + "m_" + ".png")
plt.clf()
nx.write_gpickle(ER_NOCs, "./testSnapshot/ERNOCs_" + str(20) + "N_" + str(ER_p) + "P_" + ".gpickle")
nx.draw(ER_NOCs, with_labels=True)
plt.savefig("./testSnapshot/ERNOCs_" + str(20) + "N_" + str(ER_p) + "P_" + ".png")
plt.clf()
for prob in [0.3, 0.8]:
    for i in range(100):  # 构建100个SF子网络，节点个数为N
        for NOCs in [SF_NOCs, ER_NOCs]:
            snapshot = copy.deepcopy(NOCs)
            for e in snapshot.edges():
                if prob > random.random():
                    snapshot.remove_edge(e[0], e[1])
            print(snapshot)
            # snapshotMat = nx.to_numpy_matrix(snapshot)
            if NOCs == SF_NOCs:
                name = "./testSnapshot/SFNOCs_" + str(20) + "N_" + str(m) + "m_" + str(prob) + "prob_" + str(i)
            elif NOCs == ER_NOCs:
                name = "./testSnapshot/ERNOCs_" + str(20) + "N_" + str(ER_p) + "P_" + str(prob) + "prob_" + str(i)
            else:
                name = "./testSnapshot/Error.txt"
            nx.write_gpickle(snapshot, name + ".gpickle")
            nx.draw(snapshot, with_labels=True)
            plt.savefig(name + ".png")
            plt.clf()


# print(nx.read_gpickle("./Snapshot/SFNOCs_" + str(N) + "N_" + str(m) + "m_" + ".gpickle"))
# print(nx.read_gpickle("./Snapshot/ERNOCs_" + str(N) + "N_" + str(ER_p) + "P_" + ".gpickle"))
#
# for prob in [0.3, 0.8]:
#     for i in range(100):  # 构建100个SF子网络，节点个数为N
#         for NOCs in [SF_NOCs, ER_NOCs]:
#             if NOCs == SF_NOCs:
#                 name = "./Snapshot/SFNOCs_" + str(N) + "N_" + str(m) + "m_" + str(prob) + "prob_" + str(i) + ".gpickle"
#             elif NOCs == ER_NOCs:
#                 name = "./Snapshot/ERNOCs_" + str(N) + "N_" + str(ER_p) + "P_" + str(prob) + "prob_" + str(i) + ".gpickle"
#             else:
#                 name = "./Snapshot/Error.txt"
#             print(nx.read_gpickle(name))

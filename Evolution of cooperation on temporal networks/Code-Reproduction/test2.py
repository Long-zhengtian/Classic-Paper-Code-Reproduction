import networkx   as nx
import numpy      as np
import random     as rnd
import multiprocessing
from multiprocessing import Pool
from functools import partial

# Generates random graph
def gen_rnd_graph(nv, ne):
    G = nx.gnm_random_graph(nv, ne, seed=None, directed=False)

    for s, t in G.edges():
        G[s][t]['weight'] = rnd.random()

    return G


# Generates random time-varying graph
def gen_time_graph(nv, ne, ng):
    # Initialise list of graphs
    l = []

    for i in range(ng):
        gi = gen_rnd_graph(nv, ne)
        l.append(gi)

    return l


# Computes adjacency matrix for snaphot of time-varying graph
def adj_mtrx(Gk,a):
    Ak = nx.to_numpy_array(Gk, weight=1)  # weight parameter make sure adj is 1 instead of actual weight
    print(Gk.degree[1])
    return Ak


def main():
    num_of_processes = multiprocessing.cpu_count() // 2
    print('num_of_process={}'.format(num_of_processes))

    # -----------------------------------------------------------------------
    # Specify constants
    # -----------------------------------------------------------------------
    NV = 10  # no. of vertices
    NE = 15  # no. of edges
    NG = 3  # no. of snapshot graphs

    # -----------------------------------------------------------------------
    # Generate random time-varying graph
    # -----------------------------------------------------------------------
    # Gt2 = nx.erdos_renyi_graph(100, 0.6)
    Gt = gen_time_graph(NV, NE, NG)
    print(Gt)
    with Pool(num_of_processes) as p:
        pt = partial(adj_mtrx, a=1)
        At = p.map(pt, Gt)

    # for k in range(NG):
    #     print(Gt[k].edges())
    #     print(At[k])
    #     print('==========')


if __name__ == '__main__':
    main()
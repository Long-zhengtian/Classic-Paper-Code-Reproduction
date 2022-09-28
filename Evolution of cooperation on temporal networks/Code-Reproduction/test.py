import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

import pathos
from pathos.multiprocessing import ProcessPool as Pool
#import multiprocessing
#from multiprocessing import pool, process
from config import *
from EvolutionGame import EvolutionGameProcess
from player import playersInit, players
from alive_progress import alive_bar
from functools import partial

random.seed(seed_value)
np.random.seed(seed_value)
os.environ['PYTHONHASHSEED'] = str(seed_value)


if __name__ == '__main__':
    num_processes = pathos.multiprocessing.cpu_count() - 2  # 使用核心数
    pool = Pool(processes=num_processes)  # 实例化进程池

    for _g in [10, 100, 1000, G1+G2]:
        for _b in np.arange(1, 2, 0.1):
            for _p in [0.3, 0.8]:
                fc_ER = fc_SF = 0.0
                for _Graph in range(DiffGraph):
                    NOCs_ER = nx.erdos_renyi_graph(N, ER_p)
                    NOCs_SF = nx.barabasi_albert_graph(N, m)

                    pt = partial(EvolutionGameProcess, Game="PD", bORr=_b, prob=_p, g=_g)
                    NOCs_list = [NOCs_ER, NOCs_SF]
                    fc1, fc2 = pool.map(pt, NOCs_list)
                    fc_ER += fc1
                    fc_SF += fc2
                    # fc_ER += EvolutionGameProcess(NOCs_ER, "PD", _b, _p, _g)  # 均为囚徒博弈
                    # fc_SF += EvolutionGameProcess(NOCs_SF, "PD", _b, _p, _g)
                fc_ER /= DiffGraph
                fc_SF /= DiffGraph

    pool.close()
    pool.join()
    plt.savefig('./temporal_network_multi.jpg')
    plt.show()


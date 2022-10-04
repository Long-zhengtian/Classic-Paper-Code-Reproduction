import numpy as np

seed_value = 2022
N = 500  # 种群节点数量
m = 5  # BA模型参数
ER_p = 0.02  # ER图参数
G1 = 4000  # 一共前置演化G1轮
G2 = 2000  # 平衡后，演化G2轮
# g = 10  # 一个snapshot演化的轮数
DiffGraph = 1  # 跑DiffGraph个不同的图，取平均值
EG_Rounds = 10  # 每个图跑MeanStep次
glist = [10, 100, 1000, G1+G2]  # glist = [10, 100, 1000, G1+G2]
blist = [i for i in np.arange(1, 2, 0.1)]  # blist = [i for i in np.arange(1, 2, 0.1)]
plist = [0.3, 0.5, 0.8]  # plist = [0.3, 0.8]


class PayOff_PD:  # 囚徒博弈的得失情况
    def __init__(self, b=1.5):
        self.T = b
        self.R = 1
        self.P = 0
        self.S = 0


class PayOff_SG:  # 雪堆博弈的得失情况
    def __init__(self, r=0.5):
        beta = (1 / r + 1)/2
        self.T = beta
        self.R = beta - 0.5
        self.P = 0
        self.S = beta - 1

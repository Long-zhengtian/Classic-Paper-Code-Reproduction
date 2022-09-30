import numpy as np

seed_value = 2022
N = 250  # 种群节点数量
m = 3  # BA模型参数
ER_p = 0.4  # ER图参数
G1 = 3000  # 一共前置演化G1轮
G2 = 200  # 平衡后，演化G2轮
# g = 10  # 一个snapshot演化的轮数
DiffGraph = 5  # 跑DiffGraph个不同的图，取平均值
EG_Rounds = 5  # 每个图跑MeanStep次
glist = [10, 100, 1000, G1+G2]
blist = [i for i in np.arange(1, 2, 0.1)]
plist = [0.3, 0.8]


class PayOff:  # 囚徒博弈的得失情况
    def __init__(self, b=1.5):
        self.T = b
        self.R = 1
        self.P = 0
        self.S = 0


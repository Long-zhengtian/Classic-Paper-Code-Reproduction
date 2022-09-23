seed_value = 2022
N = 400  # 种群节点数量
m = 3  # BA模型参数
ER_p = 0.6  # ER图参数
G = 10000  # 一共演化G轮
# g = 10  # 一个snapshot演化的轮数
DiffGraph = 10  # 跑DiffGraph个不同的图，取平均值


class PayOff_PD():  # 囚徒博弈的得失情况
    def __init__(self, b=1.5):
        self.T = b
        self.R = 1
        self.P = 0
        self.S = 0


class PayOff_SG():  # 雪堆博弈的得失情况
    def __init__(self, r=0.5):
        beta = (1 / r + 1)/2
        self.T = beta
        self.R = beta - 0.5
        self.P = 0
        self.S = beta - 1

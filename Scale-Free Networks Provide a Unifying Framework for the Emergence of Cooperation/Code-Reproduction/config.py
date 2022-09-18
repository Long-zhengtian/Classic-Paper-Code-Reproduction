# b = 1.5  # 要求b>1
# beta = 1.5  # 要求beta>1 beta = (1/r +1 )/2
# k = 4  # 规则图的度
N = 300  # 节点数量
# m = 2  # BA模型每次加入m条边 z=2m
PreStep = 2000  # 演化轮数
CalStep = 200  # 演化PreStep后，进行CalStep步，计算均值
MeanStep = 10  # MeanStep次游戏取均值
class PayOff_PD():  # 囚徒博弈的得失情况
    def __init__(self, b = 1.5):
        self.T = b
        self.R = 1
        self.P = 0
        self.S = 0

class PayOff_SG():  # 雪堆博弈的得失情况
    def __init__(self, r = 0.5):
        beta = (1/r +1 )/2
        self.T=beta
        self.R=beta-0.5
        self.P=0
        self.S=beta-1


b = 1.5  # 要求b>1
beta = 1.5  # 要求beta>1
k = 4  # 规则图的度
N = 10000  # 节点数量
m = 10  # BA模型每次加入m条边
PreStep = 10000  # 演化轮数
CalStep = 1000  # 演化PreStep后，进行CalStep步，计算均值

class PayOff_PD():  # 囚徒博弈的得失情况
    T=b
    R=1
    P=0
    S=0

class PayOff_SG():  # 雪堆博弈的得失情况
    T=beta
    R=beta-0.5
    P=0
    S=beta-1
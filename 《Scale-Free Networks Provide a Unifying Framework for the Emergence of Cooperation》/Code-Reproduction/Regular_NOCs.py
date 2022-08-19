from config import *
class PayOff():
    def __init__(self, T = 0, R = 0, P = 0, S = 0):
        self.T = T
        self.R = R 
        self.P = P 
        self.S = S 

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

print(PayOff_PD.R)


# class PayOff():
#     def __init__(self, T = 0, R = 0, P = 0, S = 0):
#         self.T = T
#         self.R = R 
#         self.P = P 
#         self.S = S 
#     def __call__(self):
#         return self.T, self.R, self.P, self.S

# class PayOff_PD(PayOff):  # 囚徒博弈的得失情况
#     def __init__(self):
#         PayOff(b, 1, 0, 0)

# class PayOff_SG(PayOff):  # 雪堆博弈的得失情况
#     def __init__(self):
#         PayOff(beta, beta-0.5, 0, beta-1)
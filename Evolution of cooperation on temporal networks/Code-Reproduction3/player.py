import random
from config import *


class Player:  # 博弈双方对象
    def __init__(self, index, strategy, AccPayOffs=0):
        self.index = index  # 序号
        self.strategy = strategy  # 选择的博弈策略，True表示合作，False表示对抗
        self.newStrategy = strategy  # 策略更新
        self.AccPayOffs = AccPayOffs  # 累计报酬

    def __str__(self):
        return "Index: {}; Strategy: {}; AccPayOffs: {}".format(self.index, self.strategy, self.AccPayOffs)


players = []


def playersInit():
    players.clear()
    C_num = D_num = 0
    for index in range(N):
        if random.random() > 0.5:
            C_num += 1
            TempPlayer = Player(index, True, 0)
        else:
            D_num += 1
            TempPlayer = Player(index, False, 0)
        players.append(TempPlayer)
        if C_num == N/2:
            for index2 in range(N-C_num-D_num):
                players.append(Player(index2+index+1, False, 0))
            return
        if D_num == N/2:
            for index2 in range(N-C_num-C_num):
                players.append(Player(index2+index+1, True, 0))
            return

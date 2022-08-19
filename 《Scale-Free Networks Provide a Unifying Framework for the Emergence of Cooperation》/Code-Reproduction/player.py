import random
from config import *
from output import output2File

class Player():  # 博弈双方对象
    def __init__(self, index, strategy, newStrategy, AccPayOffs = 0):
        self.index = index  # 序号
        self.strategy = strategy  # 选择的博弈策略，True表示合作，False表示对抗
        self.newStrategy = strategy  # 策略更新
        self.AccPayOffs = AccPayOffs  # 累计报酬
    def __str__(self):
        return ("Index: {}; Strategy: {}; AccPayOffs: {}".format(self.index, self.strategy, self.AccPayOffs))


players = []

def playersInit():
    random.seed(0)
    output2File("output.txt", "a", "Init: players")
    players.clear()    
    for index in range(N):
        TempPlayer = Player(index, True if random.random() > 0.5 else False, 0)
        players.append(TempPlayer)  
        # print(TempPlayer)  

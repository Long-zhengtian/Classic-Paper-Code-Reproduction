import random
from player import players 
from config import * 
from output import output2File

def play(x, y, _PayOff):  # 双方进行博弈，返回收益  x,y为index
    if players[x].strategy and players[y].strategy:  # 都合作
        return _PayOff.R
    elif players[x].strategy and not players[y].strategy:
        return _PayOff.S
    elif not players[x].strategy and players[y].strategy:
        return _PayOff.T
    else :  # 都对抗
        return _PayOff.P

def strategyUpdate(x, y, _PayOff, Game, NOCs):  # 策略的更新过程
    if players[y].AccPayOffs > players[x].AccPayOffs:
        D = _PayOff.T-_PayOff.S if Game == "PD" else _PayOff.T-_PayOff.P
        k_max = max(NOCs.degree[x], NOCs.degree[y])
        UpdateProbability = (players[y].AccPayOffs - players[x].AccPayOffs) / (D * k_max)
        # print("Py-Px: {}; D: {}; k_max: {}; UpdateProbability: {}".format(players[y].AccPayOffs - players[x].AccPayOffs, D, k_max, UpdateProbability))
        if UpdateProbability > random.random():
            players[x].newStrategy = players[y].strategy
            return 
    players[x].newStrategy = players[x].strategy 
            
def EvolutionGameStep(NOCs, Game, bORr):  # 一轮演化过程
    if Game == "PD":
        _PayOff = PayOff_PD(bORr)
    elif Game == "SG":
        _PayOff = PayOff_SG(bORr)
    else:
        print("Error: GameType {} does not exit".format(Game))
        return
    # 博弈收益
    for id in range(N):
        for friend in NOCs.adj[id]:
            players[id].AccPayOffs += play(id, friend, _PayOff)
    # 策略更新
    for id in range(N):
        friend = random.choice(list(NOCs.adj[id]))
        strategyUpdate(id, friend, _PayOff, Game, NOCs)
    
    Temp = 0
    for id in range(N):
        players[id].strategy = players[id].newStrategy
        if players[id].strategy:
            Temp += 1
        # output2File("output.txt", "a", "players[{}]: {}".format(id, players[id]))
        
    output2File("output.txt", "a", "TempCooperators: {}".format(Temp))

def EvolutionGameProcess(NOCs, Game, bORr):
    # 前置演化博弈过程，保证到达博弈平衡状态
    for _ in range(PreStep):
        EvolutionGameStep(NOCs, Game, bORr)

    # 计算博弈平衡状态下的均值
    fc = 0
    for _ in range(CalStep):
        EvolutionGameStep(NOCs, Game, bORr)
        fcTemp = 0
        for id in range(N):
            # print(players[id].strategy, end = "")
            if players[id].strategy:
                fcTemp += 1
        # print()
        fc+=fcTemp / N
        # print(fcTemp/N, end = "")
        # print()
    
    fc /= CalStep
    return fc    
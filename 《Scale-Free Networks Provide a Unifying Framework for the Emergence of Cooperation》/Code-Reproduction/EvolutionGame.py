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
        k_max = max(NOCs.degree[x],NOCs.degree[y])
        UpdateProbability = (players[y].AccPayOffs - players[x].AccPayOffs) / (D * k_max)
        if UpdateProbability > random.random():
            players[y].newStrategy = players[x].strategy 
            
def EvolutionGameStep(NOCs, Game):  # 一轮演化过程
    if Game == "PD":
        _PayOff = PayOff_PD
    elif Game == "SG":
        _PayOff = PayOff_SG
    else:
        print("Error: GameType {} does not exit".format(Game))
        return
    # 博弈收益
    for id in range(N):
        for friend in NOCs.adj[id]:
            players[id].AccPayOffs += play(id, friend, _PayOff)
    # 策略更新
    for id in range(N):
        for friend in NOCs.adj[id]:
            strategyUpdate(id, friend, _PayOff, Game, NOCs)
    
    for id in range(N):
        players[id].strategy = players[id].newStrategy
        # output2File("output.txt", "a", "players[{}]: {}".format(id, players[id]))

def EvolutionGameProcess(NOCs, Game):
    for step in range(PreStep):
        EvolutionGameStep(NOCs, Game)

    output2File("output.txt", "a", "END!")
    for id in range(N):
        output2File("output.txt", "a", "players[{}]: {}".format(id, players[id]))
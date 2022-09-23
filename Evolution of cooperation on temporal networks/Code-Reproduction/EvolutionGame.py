import random
import copy
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
    else:  # 都对抗
        return _PayOff.P


def strategyUpdate(x, y, _PayOff, Game, NOCs):  # 策略的更新过程
    if players[y].AccPayOffs > players[x].AccPayOffs:
        D = _PayOff.T-_PayOff.S if Game == "PD" else _PayOff.T-_PayOff.P
        k_max = max(NOCs.degree[x], NOCs.degree[y])
        UpdateProbability = (players[y].AccPayOffs - players[x].AccPayOffs) / (D * k_max)
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
    for _id in range(N):
        if NOCs.degree[_id] != 0:
            for friend in NOCs.adj[_id]:
                players[_id].AccPayOffs += play(_id, friend, _PayOff)
    # 策略更新
    for _id in range(N):
        if NOCs.degree[_id] != 0:
            friend = random.choice(list(NOCs.adj[_id]))
            strategyUpdate(_id, friend, _PayOff, Game, NOCs)
    
    Temp = 0
    for _id in range(N):
        players[_id].AccPayOffs = 0  # 每轮都要清零一次
        players[_id].strategy = players[_id].newStrategy
        if players[_id].strategy:
            Temp += 1
    output2File("output.txt", "a", "TempCooperators: {}".format(Temp))
    return Temp / N


def EvolutionGameProcess(NOCs, Game, bORr):
    fc = 0
    for _ in range(g):
        fc = EvolutionGameStep(NOCs, Game, bORr)
    return fc  # 只传递回当前snapshot运行最后一次的合作频率


def temporal_network(NOCs, Game, bORr, prob, g):
    for _i in range(G):
        snapshot = copy.deepcopy(NOCs)
        for e in snapshot.edges():  # 以概率p随机删边
            if prob > random.random():
                snapshot.remove_edge(e[0], e[1])
        for _j in range(_i, min(_i+g, G)):
            pass
        _fc = EvolutionGameProcess(snapshot, Game, bORr)

import random
import copy
import string
import tqdm
import networkx
# import taichi as ti
# import taichi.math as tm
# from numba import jit
from player import players, playersInit
from config import * 
from output import output2File
from alive_progress import alive_bar


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
        return 0

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
    
    Temp = int(0)
    for _id in range(N):
        players[_id].AccPayOffs = 0  # 每轮都要清零一次
        players[_id].strategy = players[_id].newStrategy
        if players[_id].strategy:
            Temp += 1
    # output2File("output.txt", "a", "TempCooperators: {}".format(Temp))
    return Temp / N


def EvolutionGameProcess(NOCs, Game, g, bORr, prob):
    fc = 0.
    with alive_bar(EG_Rounds * (G1 + G2), force_tty=True) as bar:
        for _ in range(EG_Rounds):
            GTemp = 0.
            for _i in range(G1+G2):
                bar()
                snapshot = copy.deepcopy(NOCs)
                for e in snapshot.edges():  # 以概率p随机删边
                    if prob > random.random():
                        snapshot.remove_edge(e[0], e[1])
                for _j in range(_i, min(_i+g, G1+G2)):
                    mean = EvolutionGameStep(snapshot, Game, bORr)
                    if _j > G1:
                        GTemp += mean
                _i += g - 1
            GTemp /= G2
            fc += GTemp
    fc /= EG_Rounds
    return fc

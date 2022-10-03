import random

import networkx as nx
import math
from player import players
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


def strategyUpdate(x, y, _PayOff, NOCs):  # 策略的更新过程
    if players[y].AccPayOffs > players[x].AccPayOffs:
        D = _PayOff.T - _PayOff.S
        k_max = max(NOCs.degree[x], NOCs.degree[y])
        UpdateProbability = (players[y].AccPayOffs - players[x].AccPayOffs) / (D * k_max)
        if UpdateProbability > random.random():
            players[x].newStrategy = players[y].strategy
            return
    players[x].newStrategy = players[x].strategy


def EvolutionGameStep(NOCs, bORr):  # 一轮演化过程
    _PayOff = PayOff_PD(bORr)

    # 博弈收益
    for _id in range(N):
        if NOCs.degree[_id] != 0:
            for friend in NOCs.adj[_id]:
                players[_id].AccPayOffs += play(_id, friend, _PayOff)
    # 策略更新
    for _id in range(N):
        if NOCs.degree[_id] != 0:
            friend = random.choice(list(NOCs.adj[_id]))
            strategyUpdate(_id, friend, _PayOff, NOCs)

    Temp = int(0)
    for _id in range(N):
        players[_id].AccPayOffs = 0  # 每轮都要清零一次
        players[_id].strategy = players[_id].newStrategy
        if players[_id].strategy:
            Temp += 1
    # output2File("output.txt", "a", "TempCooperators: {}".format(Temp))
    return Temp / N


def readSnapshot(Rounds, g, NOCs, prob):
    name = "./Snapshot/" + str(NOCs) + "NOCs_" + str(N) + "N_"
    if NOCs == "SF":
        name += str(m) + "m_"
    else:  # ER
        name += str(ER_p) + "P_"
    if g == G1 + G2:  # 静态网络
        name += ".gpickle"
    else:
        name += str(prob) + "prob_" + str(Rounds // g) + ".gpickle"
    # print(name)
    return nx.read_gpickle(name)


def EvolutionGameProcess(NOCs, g, bORr, prob):
    fc = 0.
    snapshot = nx.empty_graph()
    GameBalanceStart = 0.
    GameBalanceEnd = 0.
    with alive_bar(EG_Rounds * (G1 + G2), force_tty=True) as bar:
        for _ in range(EG_Rounds):
            GTemp = 0.
            for _i in range(G1 + G2):
                bar()
                if _i % g == 0:
                    snapshot = readSnapshot(_i, g, NOCs, prob)
                mean = EvolutionGameStep(snapshot, bORr)
                if _i > G1:
                    GTemp += mean
                if _i == G1:
                    GameBalanceStart = mean
                if _i == G1 + G2 - 1:
                    GameBalanceEnd = mean
            GTemp /= G2
            fc += GTemp
            if abs(GameBalanceEnd - GameBalanceStart) > 0.1:
                print("NO BALANCE!{}".format(GameBalanceEnd-GameBalanceStart))
    fc /= EG_Rounds
    return fc

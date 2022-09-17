"""
public goods games evolution 公共品博弈演化
"""

import random
from config import *
from player import players, playersInit
from alive_progress import alive_bar


def PGG(x, NOCs, GorI, r):  # 以x为中心展开公共品博弈
    GoodsPool = 0  # 公共池
    if GorI:  # Fixed per game
        cost = c * players[x].strategy  # strategy = 1 or 0
        players[x].AccPayOffs -= cost
        GoodsPool += cost
        for y in NOCs.adj[x]:
            cost = c * players[y].strategy
            players[y].AccPayOffs -= cost
            GoodsPool += cost
    else:  # Fixed per individual
        cost = (c / (NOCs.degree[x] + 1)) * players[x].strategy
        players[x].AccPayOffs -= cost
        GoodsPool += cost
        for y in NOCs.adj[x]:
            cost = (c / (NOCs.degree[y] + 1)) * players[y].strategy
            players[y].AccPayOffs -= cost
            GoodsPool += cost

    players[x].AccPayOffs += r * GoodsPool / (NOCs.degree[x] + 1)
    for y in NOCs.adj[x]:
        players[y].AccPayOffs += r * GoodsPool / (NOCs.degree[x] + 1)


def strategyUpdate(x, NOCs):  # 策略更新
    y = random.choice(list(NOCs.adj[x]))
    if players[y].AccPayOffs > players[x].AccPayOffs:

        MaxPayOffs = players[x].AccPayOffs
        for _id in NOCs.adj[x]:
            MaxPayOffs = max(MaxPayOffs, players[_id].AccPayOffs)
        M = MaxPayOffs - players[x].AccPayOffs

        UpdateProbability = (players[y].AccPayOffs - players[x].AccPayOffs) / M
        if UpdateProbability > random.random():
            players[x].newStrategy = players[y].strategy
            return
    players[x].newStrategy = players[x].strategy


def PGGEStep(NOCs, GorI, r):  # 一步博弈演化, 返回这代的合作比
    for _id in range(N):  # 博弈
        PGG(_id, NOCs, GorI, r)

    for _id in range(N):  # 演化
        strategyUpdate(_id, NOCs)

    TempC = 0
    for _id in range(N):  # 本代结束，策略更新以及收益清零
        players[_id].strategy = players[_id].newStrategy
        TempC += players[_id].strategy
        players[_id].AccPayOffs = 0
    return TempC / N


def PGGEProcess(NOCs, GorI, r):
    # 公共品博弈演化过程  GorI表示fixed cost per game or fixed cost per individual, True表示Game
    playersInit()

    print("PreStep: ")
    with alive_bar(PreStep, force_tty=True) as bar:
        for _ in range(PreStep):  # 前置演化过程
            PGGEStep(NOCs, GorI, r)
            bar()

    print("Cal: ")
    SumMean = 0
    with alive_bar(MeanStep * CalStep, force_tty=True) as bar:
        for _mean in range(MeanStep):
            SumCal = 0
            # print("MeanStep: {}".format(_mean))
            for _cal in range(CalStep):
                SumCal += PGGEStep(NOCs, GorI, r)
                bar()
            SumCal /= CalStep
            SumMean += SumCal
    SumMean /= MeanStep
    return SumMean

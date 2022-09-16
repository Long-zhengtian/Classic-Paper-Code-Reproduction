"""
public goods games evolution 公共品博弈演化
"""

import random
from config import *
from player import players


def PGG(x, NOCs, GorI, r):  # 以x为中心展开公共品博弈，此处代码可以优化，似乎有些问题？
    GoodsPool = 0  # 公共品
    if GorI:  # game
        cost = AllCost * players[x].strategy
        players[x].AccPayOffs -= cost
        GoodsPool += cost
        for y in NOCs.adj[x]:
            cost = AllCost * players[y].strategy
            players[y].AccPayOffs -= cost
            GoodsPool += cost
    else:  # individual
        cost = AllCost / (NOCs.degree[x] + 1) * players[x].strategy
        players[x].AccPayOffs -= cost
        GoodsPool += cost
        for y in NOCs.adj[x]:
            cost = AllCost / (NOCs.degree[y] + 1) * players[y].strategy
            players[y].AccPayOffs -= cost
            GoodsPool += cost


def strategyUpdate(x, NOCs):  # 策略更新
    y = random.choice(list(NOCs.adj[x]))
    if players[y].AccPayOffs > players[x].AccPayOffs:
        # 正则化 未完成
        k_max = max(NOCs.degree[x], NOCs.degree[y])
        UpdateProbability = (players[y].AccPayOffs - players[x].AccPayOffs) / (k_max)
        # print("Py-Px: {}; D: {}; k_max: {}; UpdateProbability: {}".format(players[y].AccPayOffs - players[x].AccPayOffs, D, k_max, UpdateProbability))
        if UpdateProbability > random.random():
            players[x].newStrategy = players[y].strategy
            return
    players[x].newStrategy = players[x].strategy


def PGGEStep(NOCs, GorI, r):  # 一步博弈演化
    for id in range(N):  # 清零AccPayOffs
        players[id].AccPayOffs = 0

    for id in range(N):  # 博弈
        PGG(id, NOCs, GorI, r)

    for id in range(N):  # 演化
        strategyUpdate(id, NOCs)

    TempC = 0
    for id in range(N):  # 策略更新
        players[id].strategy = players[id].newStrategy
        if players[id].strategy:
            TempC += 1
    return TempC


def PGGEProcess(NOCs, GorI, r):
    # 公共品博弈演化过程  GorI表示fixed cost per game or fixed cost per individual, True表示Game
    for _ in range(PreStep):  # 前置演化过程
        PGGEStep(NOCs, GorI, r)
        print("PreStep: {}".format(_))

    SumMean = 0
    for _mean in range(MeanStep):
        SumCal = 0
        for _cal in range(CalStep):
            SumCal += PGGEStep(NOCs, GorI, r)
        SumCal /= CalStep
        SumMean += SumCal
    SumMean /= CalStep
    return SumMean

import random
from player import players 
from config import * 
from output import output2File
from alive_progress import alive_bar
from math import exp
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
    try:
        prob = 1 / (1 + exp(-1 * s * (players[y].AccPayOffs - players[x].AccPayOffs)))
    except OverflowError:
        prob = 1 if players[y].AccPayOffs > players[x].AccPayOffs else 0

    if prob > random.random():
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
        players[id].AccPayOffs = 0  # 每轮都要清零一次
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
    output2File("output.txt", "a", "TempCooperators: {}".format(Temp))
    return Temp / N


def EvolutionGameProcess(NOCs, Game, bORr):
    meanTemp = 0
    with alive_bar(MeanStep * (PreStep + CalStep), force_tty=True) as bar:
        for mean in range(MeanStep):
            # 前置演化博弈过程，保证到达博弈平衡状态
            for _ in range(PreStep):
                fc = EvolutionGameStep(NOCs, Game, bORr)
                bar()
            # 计算博弈平衡状态下的均值
            fc = 0
            for _ in range(CalStep):
                fc += EvolutionGameStep(NOCs, Game, bORr)
                bar()
            fc /= CalStep
            # print(meanTemp, end="")
            meanTemp += fc
        meanTemp /= MeanStep
    # print()
    return meanTemp
